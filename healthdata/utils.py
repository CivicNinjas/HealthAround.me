from boundaryservice.models import Boundary, BoundarySet
from data.models import Census

def stand_dev_form(total, target):
	tract_set = BoundarySet.objects.all()[1]
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(total, target)
	data = Census.objects.filter(boundary__set=tract_set).values_list(total, target)
	ok_percentile = ok_data_new[0][1]/float(ok_data_new[0][0])
	count = 0
	total = 0.0
	for tracts in data:
		if tracts[0] != 0:
			total += (tracts[1]/float(tracts[0]) - ok_percentile)**2
			count += 1
	total = (total/float(count))**(0.5)
	return total


#This should be used when you need to get the standard deviation for a value
#that is obtained by dividing a number of rows of data by the total number
#of entries on that form, IE where the total can be obtained from the 
# BXXXXXX_001E entry.
def stand_dev_total_rows(rows):
	tract_set = BoundarySet.objects.all()[1]
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	#Gets the data for calculating the total for Oklahoma
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	#Gets the data for calculating the totals at each individual census tract
	data = Census.objects.filter(boundary__set=tract_set).values_list(*rows)
	#This block of code obtains the percentile for Oklahoma, which is neccesary for 
	#the standard deviation calculations.
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	to_divide_ok = sum(total_ok_pre)
	ok_percentile = to_divide_ok/float(total_ok)
	count = 0
	total = 0.0
	for tracts in data:
		if tracts[0] != 0:
			tracks = list(tracts)
			tracts_total = tracks.pop(0)
			tracts_unemployed = sum(tracks)
			total += (tracts_unemployed/float(tracts_total) - ok_percentile)**2
			count += 1
	final_total = (total/float(count))**(0.5)
	return final_total

def stand_dev_income_housing_cost(rows):
	tract_set = BoundarySet.objects.all()[1]
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	data = Census.objects.filter(boundary__set=tract_set).values_list(*rows)
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	unemployed_ok = sum(total_ok_pre)
	ok_percentile = unemployed_ok/float(total_ok)

	count = 0
	total = 0.0
	for tracts in data:
		if tracts != 0:
			current_tract = list(tracts)
			tracts_total = current_tract.pop(0)
			tracts_unemployed = sum(current_tract)
			total += (tracts_unemployed/float(tracts_total) - ok_percentile)**2
			count += 1

	total = (total/float(count))**(0.5)
	return total

#Should be used when you need to calcualte the standard deviation
#of a value obtained by dividing the sum of a number of rows(numer_rows)
#by several other rows(denom_rows)
def stand_dev_numer_denom(numer_rows, denom_rows):
	numer_length = len(numer_rows)
	denom_length = len(denom_rows)
	tract_set = BoundarySet.objects.all()[1]
	ok_boundary = Boundary.objects.get(slug='oklahoma-state')
	ok_data = Census.objects.filter(boundary=ok_boundary).values_list(*numer_rows + denom_rows).first()
	tract_data = Census.objects.filter(boundary__set=tract_set).values_list(*numer_rows + denom_rows)
	ok_numer = sum(ok_data[:numer_length])
	ok_denom = sum(ok_data[numer_length:numer_length+denom_length])
	ok_percentile = ok_numer/float(ok_denom)

	count = 0
	total = 0.0
	for tract in tract_data:
		if sum(tract[numer_length:numer_length+denom_length]) != 0:
			tract_numer = sum(tract[:numer_length])
			tract_denom = sum(tract[numer_length:numer_length+denom_length])
			total += (tract_numer/float(tract_denom) - ok_percentile)**2
			count += 1

	final_total = (total/float(count))**(0.5)
	return final_total


def avg_multiple_rows(rows):
	ok_data = Boundary.objects.get(slug='oklahoma-state')
	ok_data_new = Census.objects.filter(boundary=ok_data).values_list(*rows).first()
	total_ok_pre = list(ok_data_new)
	total_ok = total_ok_pre.pop(0)
	sum_to_average = sum(total_ok_pre)
	ok_percentile = sum_to_average/float(total_ok)
	return ok_percentile


