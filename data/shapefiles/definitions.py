from datetime import date

from boundaryservice import utils

SHAPEFILES = {
    'Counties': {
        'file': 'counties.zip',
        'singular': 'County',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'United States Census Bureau',
        'domain': 'United States of America',
        'last_updated': date(2013, 8, 6),
        'href': (
            'ftp://ftp2.census.gov/geo/tiger/TIGER2013/'
            'COUNTY/tl_2013_us_county.zip'),
        'notes': 'Resaved as UTF-8 encoding',
        'encoding': '',
        'srid': '',
        'simplification': 0.0001,
    },
    'States': {
        'file': 'tl_2013_us_state.zip',
        'singular': 'State',
        'kind_first': False,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'United States Census Bureau',
        'domain': 'United States of America',
        'last_updated': date(2013, 8, 6),
        'href': (
            'ftp://ftp2.census.gov/geo/tiger/TIGER2013/'
            'STATE/tl_2013_us_state.zip'),
        'notes': '',
        'encoding': '',
        'srid': '',
        'simplification': 0.0001,
    },
    'Census Tracts': {
        'file': 'tl_2013_40_tract.zip',
        'singular': 'Census Tract',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'United States Census Bureau',
        'domain': 'United States of America',
        'last_updated': date(2013, 8, 2),
        'href': (
            'ftp://ftp2.census.gov/geo/tiger/TIGER2013/'
            'TRACT/tl_2013_40_tract.zip'),
        'notes': '',
        'encoding': '',
        'srid': '',
        'simplification': 0.0001,
    },
    'Census Block Groups': {
        'file': 'tl_2013_40_bg.zip',
        'singular': 'Census Block Group',
        'kind_first': True,
        'ider': utils.simple_namer(['GEOID']),
        'namer': utils.simple_namer(['TRACTCE', 'BLKGRPCE']),
        'authority': 'United States Census Bureau',
        'domain': 'United States of America',
        'last_updated': date(2013, 8, 2),
        'href': (
            'ftp://ftp2.census.gov/geo/tiger/TIGER2013/'
            'BG/tl_2013_40_bg.zip'),
        'notes': '',
        'encoding': '',
        'srid': '',
        'simplification': 0.0001,
    },
}
