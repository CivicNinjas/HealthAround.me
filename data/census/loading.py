#!/usr/bin/env python
'''Load Census Data'''
from collections import namedtuple
from csv import reader
from struct import unpack
from urllib import urlretrieve
from zipfile import ZipFile
import logging
import os.path

from boundaryservice.models import Boundary

logger = logging.getLogger(__name__)


class CensusLoader(object):
    census_url = 'http://www2.census.gov/acs2012_5yr/summaryfile/'
    table_lookup_name = 'Sequence_Number_and_Table_Number_Lookup.txt'
    table_lookup_url = census_url + table_lookup_name
    data_url = (
        census_url + '2008-2012_ACSSF_By_State_By_Sequence_Table_Subset/')
    cache_folder = os.path.join(os.path.dirname(__file__), 'cache')
    model = 'data.models.Census'

    GEO_ALL = 0
    GEO_TRACTS = 1
    GEO_DOMAINS = (
        (GEO_ALL, 'All_Geographies_Not_Tracts_Block_Groups'),
        (GEO_TRACTS, 'Tracts_Block_Groups_Only'))

    STATES = (
        ('al', 'Alabama'),
        ('ak', 'Alaska'),
        ('az', 'Arizona'),
        ('ar', 'Arkansas'),
        ('ca', 'California'),
        ('co', 'Colorado'),
        ('ct', 'Connecticut'),
        ('de', 'Delaware'),
        ('dc', 'District Of Columbia'),
        ('fl', 'Florida'),
        ('ga', 'Georgia'),
        ('hi', 'Hawaii'),
        ('id', 'Idaho'),
        ('il', 'Illinois'),
        ('in', 'Indiana'),
        ('ia', 'Iowa'),
        ('ks', 'Kansas'),
        ('ky', 'Kentucky'),
        ('la', 'Louisiana'),
        ('me', 'Maine'),
        ('md', 'Maryland'),
        ('ma', 'Massachusetts'),
        ('mi', 'Michigan'),
        ('mn', 'Minnesota'),
        ('ms', 'Mississippi'),
        ('mo', 'Missouri'),
        ('mt', 'Montana'),
        ('ne', 'Nebraska'),
        ('nv', 'Nevada'),
        ('nh', 'New Hampshire'),
        ('nj', 'New Jersey'),
        ('nm', 'New Mexico'),
        ('ny', 'New York'),
        ('nc', 'North Carolina'),
        ('nd', 'North Dakota'),
        ('oh', 'Ohio'),
        ('ok', 'Oklahoma'),
        ('or', 'Oregon'),
        ('pa', 'Pennsylvania'),
        ('pr', 'Puerto Rico'),
        ('ri', 'Rhode Island'),
        ('sc', 'South Carolina'),
        ('sd', 'South dakota'),
        ('tn', 'Tennessee'),
        ('tx', 'Texas'),
        ('us', 'United States'),
        ('ut', 'Utah'),
        ('vt', 'Vermont'),
        ('va', 'Virginia'),
        ('wa', 'Washington'),
        ('wv', 'West Virginia'),
        ('wi', 'Wisconsin'),
        ('wy', 'Wyoming'),
    )

    SUMMARY_LEVEL_TO_BOUNDARY_SET_SLUGS = (
        ('040', 'states'),
        ('050', 'counties'),
        ('140', 'census-tracts'),
        ('150', 'census-block-groups'),
    )

    def __init__(self, table_ids, states, **kwargs):
        '''Initialize the Census Loader

        Keyword arguments:
        - table_ids - a list of U.S. census table IDs (such as 'B23121')
        '''

        self.table_ids = table_ids
        self.states = states
        self._seq_defs = None

    def cached_path(self, url, path):
        local_path = os.path.join(self.cache_folder, path)
        if not os.path.exists(local_path):
            logger.info("Downloading %s from %s...", local_path, url)
            filename, headers = urlretrieve(url, local_path)
            logger.info("...Downloaded")
            assert filename == local_path
        return local_path

    def open_snatnl(self):
        '''Return the Sequence Number and Table Number Lookup file'''
        snatnl_path = self.cached_path(
            self.table_lookup_url, self.table_lookup_name)
        logger.info("Reading from %s", snatnl_path)
        return open(snatnl_path, 'rb')

    def state_url(self, state_abbr, geo_type):
        full_state = dict(self.STATES)[state_abbr].replace(' ', '')
        return (
            self.census_url +
            '2008-2012_ACSSF_By_State_By_Sequence_Table_Subset/' +
            full_state + '/')

    def state_data_url(self, state_abbr, geo_type):
        geo_path = dict(self.GEO_DOMAINS)[geo_type]
        return self.state_url(state_abbr, geo_type) + geo_path + '/'

    def geo_url(self, state_abbr, geo_type):
        return (
            self.state_data_url(state_abbr, geo_type) +
            'g20125{}.txt'.format(state_abbr))

    def geo_path(self, state_abbr, geo_type):
        return 'g20125{}.{}.txt'.format(state_abbr, geo_type)

    def open_geo(self, state_abbr, geo_type):
        '''Return the geographic info file for the state'''
        geo_path = self.cached_path(
            self.geo_url(state_abbr, geo_type),
            self.geo_path(state_abbr, geo_type))
        logger.info("Reading from %s", geo_path)
        return open(geo_path, 'rb')

    def sequence_zip_url(self, state_abbr, geo_type, seq):
        return (
            self.state_data_url(state_abbr, geo_type) +
            '20125{}{:04d}000.zip'.format(state_abbr, int(seq)))

    def sequence_zip_path(self, state_abbr, geo_type, seq):
        return '20125{}{:04d}000.{}.zip'.format(state_abbr, int(seq), geo_type)

    def sequence_filename(self, state_abbr, seq, data_type='e'):
        return '{}20125{}{:04d}000.txt'.format(data_type, state_abbr, int(seq))

    def open_sequence_data(self, state_abbr, geo_type, seq, data_type='e'):
        seq_zip_path = self.cached_path(
            self.sequence_zip_url(state_abbr, geo_type, seq),
            self.sequence_zip_path(state_abbr, geo_type, seq))
        z = ZipFile(seq_zip_path, 'r')
        seq_filename = self.sequence_filename(state_abbr, seq, data_type)
        logger.info("Reading %s from %s", seq_filename, seq_zip_path)
        return z.open(seq_filename)

    def seq_defs(self):
        '''Parse the SNATNL, finding sequence numbers for desired table IDs

        SNATNL = Sequence Number and Table Number Lookup

        Return is a dict, with the sequence number as key ('0001'), and the
        values being data about the file (include table IDs, column defs).
        If a sequence file does not include a requested table ID, it is not
        included in the return dict.
        '''

        def text_or_none(text):
            stext = text.strip()
            return stext or None

        def int_or_none(text):
            stext = text.strip()
            if stext:
                return int(stext)
            else:
                return None

        def int_or_float_or_none(text):
            stext = text.strip()
            if '.' in stext:
                return float(stext)
            elif stext:
                return int(stext)
            else:
                return None

        if not self._seq_defs:
            sd = {}
            snatnl_file = self.open_snatnl()
            snatnl_reader = reader(snatnl_file)
            first = True
            for row in snatnl_reader:
                file_id = row[0]
                # Is it the header row?
                if first:
                    assert file_id == 'File ID'
                    first = False
                    continue
                else:
                    assert file_id == 'ACSSF'

                # Is it one of the requested tables?
                table_id = row[1]
                if table_id not in self.table_ids:
                    continue

                # Get / create the sequence data
                seq_num = row[2]
                sd_data = sd.setdefault(seq_num, {
                    'columns': {
                        0: 'file_id',
                        1: 'file_type',
                        2: 'state',
                        3: 'char_iter',
                        4: 'seq_num',
                        5: 'rec_num',
                    },
                    'tables': {}})

                # Parse as regular row
                line_num = int_or_float_or_none(row[3])
                start_pos = int_or_none(row[4])
                total_cells_in_table = text_or_none(row[5])
                total_cells_in_seq = int_or_none(row[6])
                table_title = text_or_none(row[7])
                subject_area = text_or_none(row[8])
                if start_pos and total_cells_in_table:
                    # Table descriptor, i.e.
                    # ACSSF,B01001,0002, ,7,49 CELLS, ,SEX BY AGE,Age-Sex
                    assert not line_num, line_num
                    assert start_pos
                    assert table_title
                    assert subject_area
                    sd_data['tables'].setdefault(table_id, {}).update(
                        title=table_title,
                        subject_area=subject_area,
                        start_pos=start_pos)
                elif isinstance(line_num, int):
                    # Data item descriptor, i.e.
                    # ACSSF,B01001,0002,1, ,, ,Total:,
                    assert not start_pos, start_pos
                    assert not total_cells_in_table, total_cells_in_table
                    assert not total_cells_in_seq, total_cells_in_seq
                    assert not subject_area, subject_area
                    start_pos = sd_data['tables'][table_id]['start_pos']
                    column = start_pos + line_num - 2
                    name = '{}_{:03d}'.format(table_id, line_num)
                    sd_data['columns'][column] = name
                    sd_data['tables'][table_id].setdefault(
                        'items', {})[name] = table_title
                else:
                    # Extra table information, i.e.
                    # ACSSF,B00002,0001, , ,, ,Universe:  Housing units,
                    assert not start_pos, start_pos
                    assert table_title
                    assert not subject_area, subject_area
                    sd_data['tables'][table_id].setdefault(
                        'extra', []).append(table_title)

                # Add value type
                table_defs = self.table_ids[table_id]
                valtype = table_defs.get('valtype', 'integer')
                sd_data['tables'][table_id]['valtype'] = valtype

            self._seq_defs = sd

        return self._seq_defs

    @staticmethod
    def to_title(raw_title):
        '''Convert a string to a title'''
        keep_lower = ('to', 'a', 'the', 'by', 'of', 'is')
        raw_title_bits = raw_title.lower().strip().split()
        title_bits = []
        for bit in raw_title_bits:
            if title_bits and bit in keep_lower:
                title_bits.append(bit)
            else:
                title_bits.append(bit.title())
        return ' '.join(title_bits)

    def model_declaration(self):
        '''Get Django model declaration for selected columns'''

        # Gather table data
        tables = {}
        seq_defs = self.seq_defs()
        for sdef in seq_defs.values():
            for table_id, params in sdef['tables'].items():
                t_def = tables.setdefault(table_id, {})
                t_def['title'] = self.to_title(params['title'])
                t_def['valtype'] = params['valtype']
                items = t_def.setdefault('items', [])
                items.extend([(n, t) for n, t in params['items'].items()])

        mname = self.model.split('.')[-1]
        decl = ["""\
from django.db import models
from boundaryservice.models import Boundary


class {}(models.Model):
    '''Selected items from U.S. Census 5-Year Summary for Boundary'''

    class Meta:
        verbose_name_plural = "census"
        app_label = "data"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    logical_num = models.IntegerField(help_text='Logical record number')\
""".format(mname)]

        for table_id in sorted(tables.keys()):
            decl.append("")
            params = tables[table_id]
            heading = params['title']
            if len(heading) < 64:
                decl.append("    # {} - {}".format(table_id, heading))
            else:
                comment_bits = ["    #", table_id, "-"]
                for bit in heading.split():
                    comment_bits.append(bit)
                    if len(' '.join(comment_bits)) > 71:
                        comment_bits.pop(-1)
                        decl.append(' '.join(comment_bits))
                        comment_bits = ["    #         ", bit]
                if comment_bits:
                    decl.append(' '.join(comment_bits))

            first = True
            for name, title in sorted(params['items']):
                valtype = params['valtype']
                if valtype == 'integer':
                    decl.append("""\
    {}E = models.IntegerField(
        blank=True, null=True,""".format(name))
                elif valtype.startswith('decimal:'):
                    _, dec_params = valtype.split(':', 1)
                    max_digits, decimal_places = dec_params.split(',', 1)
                    decl.append("""\
    {}E = models.DecimalField(
        max_digits={}, decimal_places={}, blank=True, null=True,""".format(
                        name, max_digits, decimal_places))

                if first:
                    if title.lower() == heading.lower():
                        help_text = title
                    else:
                        help_text = heading + ': ' + title
                    first = False
                else:
                    help_text = title
                help_text = help_text.replace("'", "\\'")
                if len(help_text) < 59:
                    decl.append(
                        "        help_text='{}')".format(help_text))
                else:
                    decl.append("        help_text=(")
                    help_bits = []
                    for bit in help_text.split():
                        help_bits.append(bit)
                        if len(' '.join(help_bits)) > 63:
                            help_bits.pop(-1)
                            decl.append(
                                ' '*12 + "'" + ' '.join(help_bits) + "'")
                            help_bits = [' ' + bit]
                    if help_bits:
                        decl.append(' '*12 + "'" + ' '.join(help_bits) + "'))")
                    else:
                        decl.append(' '*12 + "))")

        return '\n'.join(decl)

    def import_data(self):
        seq_defs = self.seq_defs()
        for state in self.states:
            # Geography is same for both domains
            self.load_geography_state_domain(state, self.GEO_ALL)
            for domain, _ in self.GEO_DOMAINS:
                for seq_num in sorted(seq_defs.keys()):
                    seq_def = seq_defs[seq_num]
                    self.load_sequence_data(
                        state, domain, seq_num, seq_def, 'e')

    def load_geography_state_domain(self, state, domain):
        fmt = (
            '6s2s3s2s7ssss2s2s3s5s5s6ss5s4s5ss3s5s5s5s3s5sss5s3s5s5s5s2s3s'
            '3s6s3s5s5s5s5s5sss6s5s5s5s40s1000s6s1s43s')
        fields = (
            'FILEID, STUSAB, SUMLEVEL, COMPONENT, LOGRECNO, US, REGION,'
            ' DIVISION, STATECE, STATE, COUNTY, COUSUB, PLACE, TRACT BLKGRP,'
            ' CONCIT, AIANHH, AIANHHFP, AIHHTLI, AITSCE, AITS, ANRC, CBSA,'
            ' CSA, METDIV, MACC, MEMI, NECTA, CNECTA, NECTADIV, UA, BLANK1,'
            ' CDCURR, SLDU, SLDL, BLANK2, BLANK3, ZCTA5, SUBMCD, SDELM,'
            ' SDSEC, SDUNI, UR, PCI, BLANK4, BLANK5, PUMA5, BLANK6, GEOID,'
            ' NAME, BTTR, BTBG, BLANK7')

        Geography = namedtuple('GeoLine', fields)
        boundary_set_slug = dict(self.SUMMARY_LEVEL_TO_BOUNDARY_SET_SLUGS)
        added, existing, skipped = (0, 0, 0)
        for count, line in enumerate(self.open_geo(state, domain)):
            gl = Geography._make(unpack(fmt, line.rstrip('\n')))
            bs_slug = boundary_set_slug.get(gl.SUMLEVEL)
            if bs_slug and gl.COMPONENT == '00':
                _, external_id = gl.GEOID.strip().split('US')
                new = self.add_geo_record(
                    gl.STUSAB, gl.LOGRECNO, external_id, bs_slug)
                if new:
                    added += 1
                else:
                    existing += 1
            else:
                skipped += 1
        logger.info(
            "%s geographies processed (%s added, %s existing, %s skipped)",
            count, added, existing, skipped)

    def add_geo_record(self, state_abbr, logical_num, external_id, bs_slug):
        from data.models import Census
        boundary = Boundary.objects.get(external_id=external_id)
        assert boundary.set.slug == bs_slug
        c, created = Census.objects.get_or_create(
            state_abbr=state_abbr, logical_num=logical_num, boundary=boundary)
        return created

    def load_sequence_data(
            self, state, domain, seq_num, seq_def, data_type='e'):
        seq_data_file = self.open_sequence_data(state, domain, seq_num)
        seq_reader = reader(seq_data_file)
        item_count, items_skipped, rows_updated, rows_skipped = (0, 0, 0, 0)
        assert_cols = {
            'file_id': 'ACSSF',
            'file_type': '2012{}5'.format(data_type),
            'state': state,
            'char_iter': '000',
            'seq_num': seq_num
        }

        for count, row in enumerate(seq_reader):
            data = dict()
            logical_num = None
            for col, name in seq_def['columns'].items():
                if name in assert_cols:
                    assert assert_cols[name] == row[col], row[col]
                elif name == 'rec_num':
                    logical_num = row[col]
                elif row[col] in ['', '.']:
                    items_skipped += 1
                else:
                    data[name + data_type.upper()] = row[col]
            assert logical_num, row
            assert logical_num.isdigit(), logical_num
            if data:
                updated = self.add_seq_data(state, logical_num, data)
            else:
                updated = 0
            assert updated in [0, 1]
            if updated:
                rows_updated += 1
                item_count += len(data)
            else:
                rows_skipped += 1
        logger.info(
            "%s data rows processed (%s updated with %s data points,"
            " %s rows skipped, %s empty items)",
            count, rows_updated, item_count, rows_skipped, items_skipped)

    def add_seq_data(self, state_abbr, logical_num, data):
        from data.models import Census
        return Census.objects.filter(
            state_abbr=state_abbr.upper(), logical_num=logical_num).update(
                **data)


if __name__ == '__main__':
    from definitions import TABLES, STATES
    cl = CensusLoader(table_ids=TABLES, states=STATES)
    cl.import_data()
