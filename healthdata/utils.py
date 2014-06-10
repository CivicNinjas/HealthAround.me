from math import floor
import psycopg2
from boundaryservice.models import Boundary, BoundarySet
from data.models import Census
import json
from xlrd import open_workbook,cellname
from json import JSONEncoder
from itertools import chain
import os
import csv


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
    list_of_crimes = [
    "Larceny", "Auto Theft", "Assault",
    "Robbery", "Malicious Mischief", "Burglary",
    "Rape"
    ]
    count = 0
    dictionary_to_build = {"type": "FeatureCollection", "crs": {
        "type": "name", "properties": {
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
        point = 'POINT(%.17f %.17f)' %(x_coord, y_coord)
        point_tract = (Boundary.objects.filter(shape__contains = point).filter
            (kind=u'Census Tract').first())
        #If the dictionary has already had that census track entered
        if tract_dict.has_key(point_tract.slug):
            #If that crime has already been entered in to that census track
            for tracts in tract_dict[point_tract.slug]['CRIMES']:
                if tracts[0] == crime['attributes']['CRIME_TYPE'][:4]:
                    tracts[1] += 1
                    break
            #Else it hasn't, create a new list in that census track's list.
            else:
                (tract_dict[point_tract.slug]["CRIMES"].append([crime['attributes']
                    ['CRIME_TYPE'][:4], 1]))
        #Else that census track hasn't been entered yet
        else:
            count += 1
            print point_tract.slug
            tract_dict[point_tract.slug] = {'CRIMES':[[crime['attributes']['CRIME_TYPE'][:4], 1]]}
    for tract in tract_dict:
        current_tract_boundary = Boundary.objects.get(slug=tract)
        current_tract_metadata = current_tract_boundary.metadata
        current_county_boundary = Boundary.objects.filter(shape__contains=current_tract_boundary.centroid).filter(kind="County").first()
        new_tract_dict = {"type": "Feature", "properties": {}}
        new_tract_dict["properties"]["geoid"] = current_tract_metadata['GEOID']
       
        new_tract_dict["properties"]["name"] = "%s, %s, %s" %(
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
    new_json = json.dumps(dictionary_to_build,sort_keys=True)
    print count
    return new_json


def dartmouth_health_atlas_excel_importer(excel_file):
    dictionary_to_build = {"type": "FeatureCollection", "crs": {
        "type": "name", "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "features": []
    }
    count = 0 
    excel_book = open_workbook(excel_file)
    excel_page = excel_book.sheet_by_index(0)
    for areas in range(3, 79):
        area_dict = {"type":"Feature", "properties":{}}
        current_row_name_excel = str(excel_page.cell(areas, 0).value)
        current_row_boundary = Boundary.objects.filter(display_name=
                current_row_name_excel[:-4]).filter(kind="County").first()
        current_row_value = float(excel_page.cell(areas, 1).value)
        area_dict["properties"]["geoid"] = current_row_boundary.metadata['GEOID']
        area_dict["properties"]["geoid"] = current_row_boundary.metadata['GEOID']
        area_dict["properties"]["name"] = "%s, %s, %s" %(
                current_row_boundary.metadata['NAMELSAD'],
                current_row_boundary.metadata['NAME'], "OK")
        area_dict["properties"]["DISCHARGE_RATE"] = current_row_value
        area_dict['geometry'] = current_row_boundary.shape.geojson
        dictionary_to_build['features'].append(area_dict.copy())
        count += 1
    new_json = json.dumps(dictionary_to_build, sort_keys=True)
    print count
    return new_json


def dartmouth_health_discharge_rate_db_importer():
    path = 'data/Dartmouth/Discharge_Rate.csv'
    reader = csv.reader(file(path))
    count = 0
    succesful = 0
    for county, value in reader:
        #Tests to see if it is reading in a state based on the lack of a comma
        if county[-4:-3] == ",":
            current_county_name = county[:-4]
            current_county_census = Census.objects.get(boundary__display_name=current_county_name, boundary__kind="County")
        else:
            current_county_name = county
            current_county_census = Census.objects.get(boundary__display_name=(current_county_name + " State"))
        if current_county_census is not None:
            print current_county_census, value
            current_county_census.DISCHARGE_001E = 1000.
            current_county_census.DISCHARGE_002E = float(value)
            current_county_census.save()
            print county + "works"
            succesful += 1
        else:
            print county
        count += 1
    print "Succesful: " + str(succesful)
    print "Total: " + str(count)

def discharge_health_stand_dev():
    tract_set = BoundarySet.objects.all()[2]
    dartmouth_data = Census.objects.filter(boundary__set = tract_set)
    ok_average = float(dartmouth_data[0].DISCHARGE_002E)/float(dartmouth_data[0].DISCHARGE_001E)
    print "Oklahoma Average: %f" %(ok_average)
    count = 0
    total = 0.0
    for data in dartmouth_data[1:]:
        discharge = float(data.DISCHARGE_002E)/float(data.DISCHARGE_001E)
        total += (discharge - ok_average)**(2)
        count += 1
    final_total = (total/float(count))**(0.5)
    return final_total



