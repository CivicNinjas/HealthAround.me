import logging
import json

from boundaryservice.models import Boundary
from math import ceil

from data.models import Ers

logger = logging.getLogger(__name__)


def ers_importer():
    import_obesity_data_from_json()


def import_obesity_data_from_json():
    json_data = open('data/ers/Adult_Obesity_Rates_By_County.json')
    data = json.load(json_data)
    count = 0
    for counties in data['features']:
        if counties['attributes']['State'] == 'OK':
            county_name = counties['attributes']['County']
            county_boundary = Boundary.objects.get(
                display_name__startswith=county_name, kind='County',
                external_id__startswith='40')
            state_abbr = "OK"
            adult_diabetes = counties['attributes']["PCT_DIABETES_ADULTS10"]
            adult_obesity = counties['attributes']["PCT_OBESE_ADULTS10"]
            childhood_obesity = counties['attributes']["PCT_OBESE_CHILD11"]
            rec_facilities_per_thousand = counties['attributes']["RECFACPTH11"]

            Ers_data, created = Ers.objects.get_or_create(
                boundary=county_boundary)
            Ers_data.state_abbr = state_abbr
            Ers_data.adult_diabetes = float(adult_diabetes)
            Ers_data.adult_obesity = float(adult_obesity)
            if childhood_obesity is None:
                Ers_data.childhood_obesity = childhood_obesity
            else:
                Ers_data.childhood_obesity = float(childhood_obesity)
            Ers_data.rec_facilities_per_thousand = float(
                ceil(rec_facilities_per_thousand * 10000) / 10000.0)
            Ers_data.save()
            count += 1
    logger.info("Imported {} obesity records".format(count))
