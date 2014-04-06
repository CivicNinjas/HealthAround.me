#!/usr/bin/env python
'''Load Census Data'''
from csv import reader
from urllib import urlretrieve
import os.path


class CensusLoader(object):
    census_url = 'http://www2.census.gov/acs2012_5yr/summaryfile/'
    table_lookup_name = 'Sequence_Number_and_Table_Number_Lookup.txt'
    table_lookup_url = census_url + table_lookup_name
    data_url = (
        census_url + '2008-2012_ACSSF_By_State_By_Sequence_Table_Subset/')
    cache_folder = os.path.join(os.path.dirname(__file__), 'cache')

    def __init__(self, table_ids, **kwargs):
        '''Initialize the Census Loader

        Keyword arguments:
        - table_ids - a list of U.S. census table IDs (such as 'B23121')
        '''

        self.table_ids = table_ids
        self._seq_defs = None

    def cached_path(self, url, path):
        local_path = os.path.join(self.cache_folder, path)
        filename, headers = urlretrieve(url, local_path)
        return filename

    def open_snatnl(self):
        '''Return the Sequence Number and Table Number Lookup file'''
        snatnl_path = self.cached_path(
            self.table_lookup_url, self.table_lookup_name)
        return open(snatnl_path, 'rb')

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
            self._seq_defs = sd

        return self._seq_defs


if __name__ == '__main__':
    from pprint import pprint
    from definitions import TABLES
    cl = CensusLoader(table_ids=TABLES)
    pprint(cl.seq_defs())
