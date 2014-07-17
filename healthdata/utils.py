from datetime import date
from math import floor, ceil
from textwrap import fill
from django.db.models import Q
import json

from boundaryservice.models import Boundary, BoundarySet

from data.models import Census


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
        shape=shape_wkt, display_name='Future Data Placeholder',
        kind='Future Data Placeholder',
        slug=fake_slug, centroid=centroid_wkt, name='Placeholder')
    return boundary


def stand_dev_single_value(klass, field, geolevel):
    '''
    Calculate the average and standard deviation for a single database value.
    '''
    ok_state = BoundarySet.objects.get(slug=geolevel)
    ok_data = klass.objects.filter(boundary__set=ok_state).values_list(field)
    total_features = len(ok_data)
    total_sum = 0

    for feature in ok_data:
        total_sum += sum(feature)

    average = total_sum / float(total_features)

    total_dif_squared_sum = 0

    for feature in ok_data:
        total_dif_squared_sum += ((sum(feature) - average) ** 2)

    stand_dev = (
        (total_dif_squared_sum / float(total_features)) ** (0.5))
    print "Average: " + str(average)
    print "Standard Deviation: " + str(stand_dev)
    return average, stand_dev


def std_dev_across_tracts(total_col, target_cols):
    '''
    Calcuate the standard deviation across Oklahoma census tracts
    total_col = Column with the population total
    target_cols = Columns with the count meeting the criteria.
    '''
    # Get average for all Oklahoma
    # TODO: Why did the slug change between database loads?
    # 'oklahoma-state' on one box, 'state-oklahoma' on another
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


def stand_dev_marriage():
    tract_set = BoundarySet.objects.all()[1]
    list_of_rows = [
        'B12001_001E', 'B12001_003E', 'B12001_009E',
        'B12001_012E', 'B12001_018E', 'B12001_005E',
        'B12001_014E',
    ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(
        boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0] - ok_data[1] - ok_data[2] - ok_data[3] - ok_data[4]
    ok_good_marriage = ok_data[5] + ok_data[6]
    ok_percentile = ok_good_marriage/float(ok_total)

    tract_data = Census.objects.filter(
        boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != (tract[1] + tract[2] + tract[3] + tract[4]):
            tract_total_sum = tract[1] + tract[2] + tract[3] + tract[4]
            total_has_married = tract[0] - tract_total_sum
            total_good_marriage = tract[5] + tract[6]
            tract_percentile = total_good_marriage/float(total_has_married)
            total += (tract_percentile - ok_percentile)**2
            count += 1
    final_total = (total/float(count))**(0.5)
    return final_total


def stand_dev_occupancy():
    tract_set = BoundarySet.objects.all()[1]
    list_of_rows = [
        'B25014_001E', 'B25014_003E', 'B25014_004E',
        'B25014_005E', 'B25014_006E', 'B25014_007E',
        'B25014_009E', 'B25014_010E', 'B25014_011E',
        'B25014_012E', 'B25014_013E',
    ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(
        boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_decent_housing = (ok_data[2] + ok_data[7])/8.0
    ok_crowded_housing = (ok_data[3] + ok_data[8])/4.0
    ok_cramped_housing = (ok_data[4] + ok_data[9])/2.0
    ok_bad_housing = float(ok_data[5] + ok_data[10])
    ok_total_negative_housing = (
        ok_decent_housing + ok_crowded_housing + ok_cramped_housing +
        ok_bad_housing)
    ok_percent = ok_total_negative_housing/float(ok_total)

    tract_data = Census.objects.filter(
        boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_decent_housing = (tract[2] + tract[7])/8.0
            tract_crowded_housing = (tract[3] + tract[8])/4.0
            tract_cramped_housing = (tract[4] + tract[9])/2.0
            tract_bad_housing = float(tract[5] + tract[10])
            tract_negative_housing = (
                tract_decent_housing + tract_crowded_housing +
                tract_cramped_housing + tract_bad_housing)
            tract_percentile = tract_negative_housing/float(tract_total)
            total += (tract_percentile - ok_percent)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percent
    return final_total


def stand_dev_row_mobility(total, target):
    tract_set = BoundarySet.objects.all()[1]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data_new = Census.objects.filter(
        boundary=ok_state).values_list(total, target)
    data = Census.objects.filter(
        boundary__set=tract_set).values_list(total, target)
    total_not_same_house = ok_data_new[0][0] - ok_data_new[0][1]
    ok_percentile = total_not_same_house/float(ok_data_new[0][0])

    count = 0
    total = 0.0
    for tracts in data:
        if tracts[0] != 0:
            tracts_not_same_house = tracts[0] - tracts[1]
            percent_diff_house = tracts_not_same_house/float(tracts[0])
            total += (percent_diff_house - ok_percentile)**2
            count += 1
    total = (total/float(count))**(0.5)
    print ok_percentile
    return total


def stand_dev_commute_time():
    list_of_rows = [
        'B08303_001E', 'B08303_008E', 'B08303_009E',
        'B08303_010E', 'B08303_011E', 'B08303_012E',
        'B08303_013E',
    ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(
        boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_bad_commute_times = (
        ok_data[1]/16.0 +
        ok_data[2]/8.0 +
        ok_data[3]/4.0 +
        ok_data[4]/2.0 +
        ok_data[5] + ok_data[6])
    ok_percentile = ok_bad_commute_times/float(ok_total)

    tract_set = BoundarySet.objects.all()[1]
    tract_data = Census.objects.filter(
        boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_bad_commute_times = (
                tract[1]/16.0 +
                tract[2]/8.0 +
                tract[3]/4.0 +
                tract[4] / 2.0 +
                tract[5] + tract[6])
            tract_percentile = float(tract_bad_commute_times)/tract_total
            total += (tract_percentile - ok_percentile)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percentile
    return final_total


def stand_dev_low_value_housing():
    list_of_rows = [
        'B25075_001E', 'B25075_002E', 'B25075_003E',
        'B25075_004E', 'B25075_005E', 'B25075_006E',
        'B25075_007E', 'B25075_008E', 'B25075_009E',
        'B25075_010E', 'B25075_011E', 'B25075_012E',
        'B25075_013E', 'B25075_014E', 'B25075_015E',
    ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(
        boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_low_value = sum((
        ok_data[1], ok_data[2]/2.0, ok_data[3]/2.0, ok_data[4]/4.0,
        ok_data[5]/4.0, ok_data[6]/8.0, ok_data[7]/8.0, ok_data[8]/16.0,
        ok_data[9]/32.0, ok_data[10]/48.0, ok_data[11]/64.0, ok_data[12]/80.0,
        ok_data[13]/96.0, ok_data[14]/128.0))
    ok_percentile = ok_low_value/float(ok_total)

    tract_set = BoundarySet.objects.all()[1]
    tract_data = Census.objects.filter(
        boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_low_value = sum((
                tract[1], tract[2]/2.0, tract[3]/2.0, tract[4]/4.0,
                tract[5]/4.0, tract[6]/8.0, tract[7]/8.0, tract[8]/16.0,
                tract[9]/32.0, tract[10]/48.0, tract[11]/64.0, tract[12]/80.0,
                tract[13]/96.0, tract[14]/128.0))
            tract_percentile = tract_low_value/float(tract_total)
            total += (tract_percentile - ok_percentile)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percentile
    return final_total


def create_dic_from_json_query(json_file):
    '''
    Import crime data from Tulsa Police Department

    TPD limits the number of records returned to 1000, and it isn't
    clear if you can get all the records with multiple calls.  Need a
    direct data dump.
    '''
    list_of_crimes = [
        "Larceny", "Auto Theft", "Assault", "Robbery", "Malicious Mischief",
        "Burglary", "Rape"
    ]
    count = 0
    dictionary_to_build = {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": []
    }
    tract_dict = {}
    json_data = open(json_file)
    data = json.load(json_data)
    for crime in data["features"]:
        x_coord = crime['geometry']['x']
        y_coord = crime['geometry']['y']
        point = 'POINT(%.17f %.17f)' % (x_coord, y_coord)
        point_tract = Boundary.objects.filter(
            shape__contains=point).filter(kind=u'Census Tract').first()

        #If the dictionary has already had that census track entered
        if point_tract.slug in tract_dict:
            #If that crime has already been entered in to that census track
            for tracts in tract_dict[point_tract.slug]['CRIMES']:
                if tracts[0] == crime['attributes']['CRIME_TYPE'][:4]:
                    tracts[1] += 1
                    break
            #Else it hasn't, create a new list in that census track's list.
            else:
                tract_dict[point_tract.slug]["CRIMES"].append(
                    [crime['attributes']['CRIME_TYPE'][:4], 1])
        #Else that census track hasn't been entered yet
        else:
            count += 1
            print point_tract.slug
            tract_dict[point_tract.slug] = {
                'CRIMES': [[crime['attributes']['CRIME_TYPE'][:4], 1]]}
    for tract in tract_dict:
        current_tract_boundary = Boundary.objects.get(slug=tract)
        current_tract_metadata = current_tract_boundary.metadata
        current_county_boundary = Boundary.objects.filter(
            shape__contains=current_tract_boundary.centroid).filter(
                kind="County").first()
        new_tract_dict = {"type": "Feature", "properties": {}}
        new_tract_dict["properties"]["geoid"] = current_tract_metadata['GEOID']
        new_tract_dict["properties"]["name"] = "%s, %s, %s" % (
            current_tract_metadata['NAMELSAD'],
            current_county_boundary.metadata['NAME'], "OK")

        for crime in list_of_crimes:
            for reports in tract_dict[tract]["CRIMES"]:
                print reports
                if crime[:4].upper() == reports[0]:
                    new_tract_dict["properties"][crime] = reports[1]
                    break
            else:
                new_tract_dict["properties"][crime] = 0
        geojsontract = current_tract_boundary.shape.geojson
        new_tract_dict['geometry'] = geojsontract
        dictionary_to_build["features"].append(new_tract_dict.copy())
    new_json = json.dumps(dictionary_to_build, sort_keys=True)
    print count
    return new_json


def discharge_health_stand_dev():
    tract_set = BoundarySet.objects.all()[2]
    dartmouth_data = Census.objects.filter(boundary__set=tract_set)
    ok_average = (
        float(dartmouth_data[0].DISCHARGE_002E) /
        float(dartmouth_data[0].DISCHARGE_001E))
    print "Oklahoma Average: %f" % (ok_average)
    count = 0
    total = 0.0
    for data in dartmouth_data[1:]:
        discharge = float(data.DISCHARGE_002E)/float(data.DISCHARGE_001E)
        total += (discharge - ok_average)**(2)
        count += 1
    final_total = (total/float(count))**(0.5)
    return final_total


def score_tree_to_graph():
    """Export score tree to twopi representation

    The output can be processed with Graphviz's twopi command to create
    visualizations of the score tree.  Or, try a different GraphViz
    visualization like circle or dot.
    """
    from healthdata.models import ScoreNode

    out = ["""\
/* twopi visualization of the healtharound.me score tree

To generate a graph from this file, try:

twopi -Tsvg -oscore_tree.svg <filename.twopi>
*/

graph scoretree {
  size="7.75,10.25";
  orientation="portrait";
  ranksep=3.0;
  nodesep=2.0;
  node [style=filled, fillcolor=white, shape=box];
  overlap="false";\
"""]
    today = date.today().strftime('%Y/%m/%d')
    out.append('  label="Score Nodes for {}";'.format(today))
    out.append("""
  /* Legend */
  subgraph legend {
    node [style=filled];
    rank = sink;
    label = "Legend";
    a_node [label="node", shape=oval];
    fake [fillcolor=lightpink, penwidth=0];
    real [fillcolor=cyan, penwidth=2];
    a_node -- fake [label="weight"];
    a_node -- real [label="weight"];
  };
""")

    nodes = [(0, {'label': '"scores"', 'shape': 'circle'})]
    leaves = []
    links = []

    def to_attr(properties):
        if properties:
            props = []
            for key, val in properties.items():
                props.append('{}={}'.format(key, val))
            return ' [' + ', '.join(props) + ']'
        else:
            return ''

    def add_node(parent_id, node):
        link_props = {'label': '"{}"'.format(node.weight)}
        links.append((parent_id, node.id, link_props))

        name = '"{}"'.format(fill(node.label, 14))
        node_props = {'label': name}
        if node.is_leaf_node():
            if node.metric.algorithm == 0:
                node_props['fillcolor'] = 'lightpink'
                node_props['style'] = 'filled'
                node_props['penwidth'] = 0
                node_props['shape'] = 'box'
            else:
                node_props['fillcolor'] = 'cyan'
                node_props['shape'] = 'box'
                node_props['penwidth'] = 2
        else:
            node_props['shape'] = 'oval'
        nodes.append((node.id, node_props))

        for child in node.get_children():
            add_node(node.id, child)

    for root in ScoreNode.objects.root_nodes():
        add_node(0, root)

    out.append("  /* nodes */")
    out.extend(["  {}{};".format(n, to_attr(p)) for n, p in nodes])

    out.append("\n  /* leaves */")
    out.extend(["  {}{};".format(n, to_attr(p)) for n, p in leaves])

    out.append("\n  /* links */")
    out.extend(
        ["  {} -- {}{};".format(a, b, to_attr(p)) for a, b, p in links])

    out.append("}")

    return "\n".join(out)


def highest_resolution_for_data(area_to_get, field_to_get, klass):
    #Determines the smallest boundary with the data we're looking
    contains_list = Boundary.objects.filter(
        shape__contains=area_to_get.centroid)
    values = []
    for bounds in contains_list:
        area = [
            klass.objects.filter(boundary=bounds).values_list(
                field_to_get, flat=True).first(),
            bounds.shape.area,
            bounds.kind
        ]
        values.append(area)
    sorted_values = sorted(values, key=lambda values: values[1])
    for areas in sorted_values:
        if areas[0] is not None:
            highest_resolution_kind = areas[2]
            return highest_resolution_kind


def get_field_for_area(area_to_get, field_to_get, klass):
    '''
    If the area_to_get contains or is overlapped by any census
    boundaries, this will return a list of the overlapping
    boundaries.

    Note that this only really works for real-value fields, not percentages,
    per capita fields, or per thousand
    '''

    best_kind = highest_resolution_for_data(area_to_get, field_to_get, klass)

    boundary_list = Boundary.objects.filter(
        (Q(shape__within=area_to_get) | Q(shape__overlaps=area_to_get)),
        kind=best_kind)

    '''
    If this list is empty, the area_to_get is contained entirely inside
    other boundaries.  In this situation, the smallest of such boundaries
    that has the field_to_get must be determined and returned.
    '''
    if not boundary_list:

        contains_bound = Boundary.objects.filter(
            shape__contains=area_to_get,
            kind=best_kind
        ).first()

        container_value = klass.objects.filter(
            boundary=contains_bound
        ).values_list(field_to_get, flat=True).first()

        percent = area_to_get.area / float(contains_bound.shape.area)
        total = container_value * percent
        return round(total, 6)

    total = 0.0
    for blocks in boundary_list:

        field = klass.objects.filter(
            boundary=blocks
        ).values_list(
            field_to_get, flat=True
        ).first()

        sect = blocks.shape.simplify(
            tolerance=0.00001,
            preserve_topology=True
        ).intersection(area_to_get)

        sect_area = sect.area
        block_area = blocks.shape.area
        percent = sect_area/float(block_area)
        total += percent * float(field)
    return round(total, 6)


def get_field_for_area_percent(area_to_get, field_to_get, klass):
    best_kind = highest_resolution_for_data(area_to_get, field_to_get, klass)

    if best_kind is None:
        return None
    boundary_list = Boundary.objects.filter(
        (Q(shape__within=area_to_get) | Q(shape__overlaps=area_to_get)),
        kind=best_kind)

    if not boundary_list:

        contains_bound = Boundary.objects.filter(
            shape__contains=area_to_get,
            kind=best_kind
        ).first()

        container_value = klass.objects.filter(
            boundary=contains_bound
        ).values_list(field_to_get, flat=True).first()
        '''
        If the area_to_get is entirely contained within another boundary,
        then the per capita field is  equal to that boundary's field
        '''
        return container_value

    '''
    This block works by getting the population of each intersection with
    the area_to_get and intersecting blocks and then using the per_capita_field
    to get the actual number of whatver the field is in the intersection.
    This is then added to a total, and  the population to a different total.
    When all of the blocks have been looped through, the total for the field
    is divided by the total population for area specified to get the
    per-capita for that area.
    '''
    total_pop = 0.0
    total_pop_field = 0.0
    for blocks in boundary_list:

        field_per_capita = klass.objects.filter(
            boundary=blocks
        ).values_list(
            field_to_get, flat=True
        ).first()

        block_pop = Census.objects.filter(
            boundary=blocks
        ).values_list(
            'B01003_001E', flat=True
        ).first()

        sect = blocks.shape.simplify(
            tolerance=0.00001,
            preserve_topology=True
        ).intersection(area_to_get)

        sect_area = sect.area
        block_area = blocks.shape.area
        percent = sect_area/float(block_area)
        sect_pop = percent * block_pop
        sect_pop_field = sect_pop * field_per_capita
        total_pop += sect_pop
        total_pop_field += sect_pop_field

    percent_area_to_get = total_pop_field / total_pop
    return round(percent_area_to_get, 6)


def round_div_float(float_num, divide_by):
    return ceil(float_num * 10000) / (10000.0 * divide_by)
