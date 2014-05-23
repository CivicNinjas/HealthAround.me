from boundaryservice.models import Boundary, BoundarySet
from data.models import Census

def stand_dev_form(total, target):
	tract_set = BoundarySet.objects.all()[1]
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(total, target)
	data = Census.objects.filter(boundary__set=tract_set).values_list(total, target)
	ok_percentile = float(ok_data_new[0][1]/ok_data_new[0][0])
	count = 0
	total = 0.0
	for tracts in data:
		if tracts[0] != 0:
			total += (float(tracts[1]/tracts[0]) - ok_percentile)**2
			count += 1
	total = (total/count)**(0.5)
	return total


list_of_rows = (
                    'B23001_001E', 'B23001_008E', 'B23001_015E',
                    'B23001_022E', 'B23001_029E', 'B23001_036E',
                    'B23001_043E', 'B23001_050E', 'B23001_057E',
                    'B23001_064E', 'B23001_071E', 'B23001_076E',
                    'B23001_081E', 'B23001_086E', 'B23001_094E',
                    'B23001_101E', 'B23001_108E', 'B23001_115E',
                    'B23001_122E', 'B23001_129E', 'B23001_136E',
                    'B23001_143E', 'B23001_150E', 'B23001_157E',
                    'B23001_162E', 'B23001_167E', 'B23001_172E',
    )

def stand_dev_employment(rows):
	tract_set = BoundarySet.objects.all()[1]
	
	
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	data = Census.objects.filter(boundary__set=tract_set).values_list(*rows)
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	unemployed_ok = sum(total_ok_pre)
	ok_percentile = float(unemployed_ok/total_ok)

	count = 0
	total = 0.0
	for tracts in data:
		if tracts[0] != 0:
			tracks = list(tracts)
			tracts_total = tracks.pop(0)
			tracts_unemployed = sum(tracks)
			total += (float(tracts_unemployed/tracts_total) - ok_percentile)**2
			count += 1
	total = (total/count)**(0.5)
	return total

def stand_dev_income_housing_cost(rows):
	tract_set = BoundarySet.objects.all()[1]
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	data = Census.objects.filter(boundary__set=tract_set).values_list(*rows)
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	unemployed_ok = sum(total_ok_pre)
	ok_percentile = float(unemployed_ok/total_ok)

	count = 0
	total = 0.0
	for tracts in data:
		if tracts != 0:
			tracks = list(tracts)
			tracts_total = tracks.pop(0)
			tracts_unemployed = sum(tracks)
			total += (float(tracts_unemployed/tracts_total) - ok_percentile)**2
			count += 1

	total = (total/count)**(0.5)
	return total

def avg_multiple_rows(rows):
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	sum_to_average = sum(total_ok_pre)
	ok_percentile = float(sum_to_average/total_ok)
	return ok_percentile


