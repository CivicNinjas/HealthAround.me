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
    print ok_percentile
    return std_dev


def stand_dev_marriage():
    tract_set = BoundarySet.objects.all()[1]
    list_of_rows = [
            'B12001_001E', 'B12001_003E', 'B12001_009E',
            'B12001_012E', 'B12001_018E', 'B12001_005E',
            'B12001_014E', 
        ] 
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0] - ok_data[1] - ok_data[2] - ok_data[3] - ok_data[4]
    ok_good_marriage = ok_data[5] + ok_data[6]
    ok_percentile = ok_good_marriage/float(ok_total)

    tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*list_of_rows)
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
            'B25014_001E','B25014_003E','B25014_004E',
            'B25014_005E','B25014_006E','B25014_007E',
            'B25014_009E','B25014_010E','B25014_011E',
            'B25014_012E','B25014_013E',
        ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(boundary=ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_decent_housing = (ok_data[2] + ok_data[7])/8.0
    ok_crowded_housing = (ok_data[3] + ok_data[8])/4.0
    ok_cramped_housing = (ok_data[4] + ok_data[9])/2.0
    ok_bad_housing = float(ok_data[5] + ok_data[10])
    ok_total_negative_housing = ok_decent_housing + ok_crowded_housing + ok_cramped_housing + ok_bad_housing
    ok_percent = ok_total_negative_housing/float(ok_total)

    tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_decent_housing = (tract[2] + tract[7])/8.0
            tract_crowded_housing = (tract[3] + tract[8])/4.0
            tract_cramped_housing = (tract[4] + tract[9])/2.0
            tract_bad_housing = float(tract[5] + tract[10])
            tract_negative_housing = tract_decent_housing + tract_crowded_housing + tract_cramped_housing + tract_bad_housing
            tract_percentile = tract_negative_housing/float(tract_total)
            total += (tract_percentile - ok_percent)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percent
    return final_total


def stand_dev_row_mobility(total, target):
    tract_set = BoundarySet.objects.all()[1]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data_new = Census.objects.filter(boundary=ok_state).values_list(total, target)
    data = Census.objects.filter(boundary__set=tract_set).values_list(total, target)
    total_not_same_house = ok_data_new[0][0] - ok_data_new[0][1]
    ok_percentile = total_not_same_house/float(ok_data_new[0][0])
    
    count = 0
    total = 0.0
    for tracts in data:
        if tracts[0] != 0:
            tracts_not_same_house = tracts[0] - tracts[1]
            total += (tracts_not_same_house/float(tracts[0]) - ok_percentile)**2
            count += 1
    total = (total/float(count))**(0.5)
    print ok_percentile
    return total


def stand_dev_occupancy():
    tract_set = BoundarySet.objects.all()[1]
    list_of_rows = [
            'B25014_001E','B25014_003E','B25014_004E',
            'B25014_005E','B25014_006E','B25014_007E',
            'B25014_009E','B25014_010E','B25014_011E',
            'B25014_012E','B25014_013E',
        ]
    ok_boundary = Boundary.objects.get(slug='oklahoma-state')
    ok_data = Census.objects.filter(boundary=ok_boundary).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_decent_housing = (ok_data[2] + ok_data[7])/8.0
    ok_crowded_housing = (ok_data[3] + ok_data[8])/4.0
    ok_cramped_housing = (ok_data[4] + ok_data[9])/2.0
    ok_bad_housing = float(ok_data[5] + ok_data[10])
    ok_total_negative_housing = ok_decent_housing + ok_crowded_housing + ok_cramped_housing + ok_bad_housing
    ok_percent = ok_total_negative_housing/float(ok_total)

    tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_decent_housing = (tract[2] + tract[7])/8.0
            tract_crowded_housing = (tract[3] + tract[8])/4.0
            tract_cramped_housing = (tract[4] + tract[9])/2.0
            tract_bad_housing = float(tract[5] + tract[10])
            tract_negative_housing = tract_decent_housing + tract_crowded_housing + tract_cramped_housing + tract_bad_housing
            tract_percentile = tract_negative_housing/float(tract_total)
            total += (tract_percentile - ok_percent)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percent
    return final_total


def stand_dev_commute_time():
    list_of_rows = [
            'B08303_001E', 'B08303_008E', 'B08303_009E',
            'B08303_010E', 'B08303_011E', 'B08303_012E',
            'B08303_013E',
        ]
    ok_state = Boundary.objects.get(set__slug='states', external_id=40)
    ok_data = Census.objects.filter(boundary = ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_bad_commute_times = ok_data[1]/16.0 + ok_data[2]/8.0 + ok_data[3] / 4.0 + ok_data[4] /2.0 + ok_data[5] + ok_data[6]
    ok_percentile = ok_bad_commute_times/float(ok_total)

    tract_set = BoundarySet.objects.all()[1]
    tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_bad_commute_times = tract[1]/16.0 + tract[2]/8.0 + tract[3]/4.0 + tract[4] / 2.0 + tract[5] + tract[6]
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
    ok_data = Census.objects.filter(boundary = ok_state).values_list(*list_of_rows).first()
    ok_total = ok_data[0]
    ok_low_value = sum(( ok_data[1], ok_data[2]/2.0, ok_data[3]/2.0, ok_data[4]/4.0,
            ok_data[5]/4.0, ok_data[6]/8.0, ok_data[7]/8.0, ok_data[8]/16.0, ok_data[9]/32.0,
            ok_data[10]/48.0, ok_data[11]/64.0, ok_data[12]/80.0, ok_data[13]/96.0, ok_data[14]/128.0) )
    ok_percentile = ok_low_value/float(ok_total)


    tract_set = BoundarySet.objects.all()[1]
    tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*list_of_rows)
    count = 0
    total = 0.0
    for tract in tract_data:
        if tract[0] != 0:
            tract_total = tract[0]
            tract_low_value = sum((tract[1], tract[2]/2.0, 
                tract[3]/2.0, tract[4]/4.0, tract[5]/4.0, tract[6]/8.0,
                tract[7]/8.0, tract[8]/16.0, tract[9]/32.0,
                tract[10]/48.0, tract[11]/64.0, tract[12]/80.0,
                tract[13]/96.0, tract[14]/128.0))
            tract_percentile = tract_low_value/float(tract_total)
            total += (tract_percentile - ok_percentile)**(2)
            count += 1
    final_total = (total/float(count))**(0.5)
    print ok_percentile
    return final_total