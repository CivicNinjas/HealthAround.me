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


