from math import floor

from boundaryservice.models import Boundary, BoundarySet
from data.models import Census


def std_dev_across_tracts(total_col, target_cols):
    '''
    Calcuate the standard deviation across Oklahoma census tracts

    total_col = Column with the population total
    target_cols = Columns with the count meeting the criteria.
    '''
    # Get average for all Oklahoma
    # TODO: Why did the slug change between database loads?
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(
        boundary=ok_state).values_list(total_col, *target_cols)[0]
    ok_total = ok_data[0]
    ok_values = ok_data[1:]
    ok_percentile = sum(ok_values) / float(ok_total)

    # Calculate standard deviation of tracts
    tract_set = BoundarySet.objects.get(slug='census-tracts')
    tract_rows = Census.objects.filter(
        boundary__set=tract_set).values_list(total_col, *target_cols)
    count = 0
    total = 0.0
    for row in tract_rows:
        tract_total = row[0]
        tract_values = row[1:]
        if tract_total != 0:
            tract_percentage = sum(tract_values) / float(tract_total)
            total += (tract_percentage - ok_percentile)**2
            count += 1
    std_dev = (total/count)**(0.5)
    return std_dev


def fake_boundary(location, precision):
    '''
    Returns a rectangular fake Boundary

    precision determines the size of the Boundary.  2 is about 1 mile tall,
    and width varies by latitude
    '''

    def round_down(val):
        factor = pow(10, precision)
        return floor(val * factor) / factor

    lon, lat = location
    factor = pow(10, precision)
    increment = 1.0 / factor
    params = {
        'bot_lon': floor(lon * factor) / factor,
        'bot_lat': floor(lat * factor) / factor,
        'precision': precision,
        'pplus': precision + 1,
    }
    params['top_lon'] = params['bot_lon'] + increment
    params['top_lat'] = params['bot_lat'] + increment
    params['ctr_lon'] = params['bot_lon'] + (increment / 2)
    params['ctr_lat'] = params['bot_lat'] + (increment / 2)
    shape_wkt = (
        "MULTIPOLYGON((("
        "{bot_lon:0.{precision}f} {bot_lat:0.{precision}f},"
        "{bot_lon:0.{precision}f} {top_lat:0.{precision}f},"
        "{top_lon:0.{precision}f} {top_lat:0.{precision}f},"
        "{top_lon:0.{precision}f} {bot_lat:0.{precision}f},"
        "{bot_lon:0.{precision}f} {bot_lat:0.{precision}f}"
        ")))").format(**params)
    centroid_wkt = (
        "POINT("
        "{ctr_lon:0.{pplus}f} {ctr_lat:0.{pplus}f}"
        ")").format(**params)
    fake_slug = (
        'fake_{precision}_'
        '{bot_lon:0.{precision}f}_'
        '{bot_lat:0.{precision}f}').format(**params)
    boundary = Boundary(
        shape=shape_wkt, display_name='Pending Data', kind='Pending Data',
        slug=fake_slug, centroid=centroid_wkt, name='fake')
    return boundary


def boundaries_for_location(location, set_slugs):
    '''
    Generate Boundaries for a location

    location - a (lon, lat) pair of floats
    set_slugs - a list of BoundarySet slugs, like 'census-tracts' or
        'states'.  The boundaries are returned in this order.  A slug
        of 'fake_2' will generate a fake Boundary with two decimals of
        precision (about a mile tall).
    '''
    wkt = 'POINT({} {})'.format(*location)
    for boundary_slug in set_slugs:
        if boundary_slug.startswith('fake_'):
            _, precision = boundary_slug.split('_', 2)
            boundary = fake_boundary(location, int(precision))
        else:
            boundary_set = BoundarySet.objects.get(slug=boundary_slug)
            try:
                boundary = Boundary.objects.get(
                    set=boundary_set, shape__contains=wkt)
            except Boundary.DoesNotExist:
                continue
        yield boundary
