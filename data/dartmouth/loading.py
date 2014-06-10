import csv
import logging

from boundaryservice.models import Boundary

from data.models import Dartmouth

logger = logging.getLogger(__name__)


def dartmouth_importer():
    dartmouth_health_discharge_rate_db_importer()


def dartmouth_health_discharge_rate_db_importer():
    path = 'data/dartmouth/discharge_rate.csv'
    reader = csv.reader(file(path))
    count = 0
    county_prefix = None
    for location, value in reader:
        #Tests to see if it is reading in a state based on the lack of a comma
        if location[-4:-3] == ",":
            assert county_prefix
            boundary_name = location[:-4]
            boundary = Boundary.objects.get(
                display_name=boundary_name, kind='County',
                external_id__startswith=county_prefix)
        else:
            assert not county_prefix
            boundary_name = location + " State"
            boundary = Boundary.objects.get(
                display_name=boundary_name, kind='State')
            county_prefix = boundary.external_id
        data, created = Dartmouth.objects.get_or_create(boundary=boundary)
        data.discharge_rate = float(value)
        data.save()
        count += 1
    logger.info("Imported {} discharge rates".format(count))
