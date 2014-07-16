import logging
import json

from boundaryservice.models import Boundary
from healthdata.utils import round_div_float

from data.models import Ers

logger = logging.getLogger(__name__)


def ers_importer():
    obesity = ImportObesityData(
        "data/ers/Adult_Obesity_Rates_By_County.json")
    obesity.import_json()

    access = ImportGroceryAccessData(
        "data/ers/LowAccessToStoresByCountyOK.json")
    access.import_json()

    grocery_per_capita = ImportGroceryPerCapitaData(
        "data/ers/GroceryStoresPerThousandByCountyOK.json")
    grocery_per_capita.import_json()

    farmers_markets = ImportFarmersMarketData(
        "data/ers/FarmersMarketsPerThousandByCountyOK.json")
    farmers_markets.import_json()

    restaurants = ImportRestaurantData(
        "data/ers/FastFoodPerCapitaByCountyOK.json")
    restaurants.import_json()

    lunches = ImportSchoolMealData(
        "data/ers/ReducedAndFreeSchoolLunchesByCountyOK.json")
    lunches.import_json()


class ImportDataFromJson(object):

    def __init__(self, json_name):
        self.json_name = json_name

    def finish_import(self, counties, Ers_data):
        raise NotImplementedError('finish_import is not implemented')

    def import_json(self):
        json_data = open(self.json_name)
        data = json.load(json_data)
        count = 0
        for counties in data['features']:
            if counties['attributes']['State'] == 'OK':
                county_name = counties['attributes']['County']
                county_boundary = Boundary.objects.get(
                    display_name__startswith=county_name, kind='County',
                    external_id__startswith='40')
                state_abbr = "OK"
                Ers_data, created = Ers.objects.get_or_create(
                    boundary=county_boundary)
                Ers_data.state_abbr = state_abbr
                self.finish_import(counties, Ers_data)
                count += 1
                Ers_data.save()

        logger.info("Imported {} records".format(count))


class ImportGroceryPerCapitaData(ImportDataFromJson):
    def finish_import(self, counties, Ers_data):
        grocery_stores_per_capita = (
            counties['attributes']['GROCPTH11'])

        Ers_data.grocery_stores_per_capita = round_div_float(
            grocery_stores_per_capita, 1000.0)


class ImportObesityData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        per_adult_diabetes = counties['attributes']['PCT_DIABETES_ADULTS10']
        per_adult_obesity = counties['attributes']["PCT_OBESE_ADULTS10"]
        rec_facilities_per_capita = counties['attributes']["RECFACPTH11"]

        Ers_data.per_adult_diabetes = round_div_float(
            per_adult_diabetes, 100.0)
        Ers_data.per_adult_obesity = round_div_float(per_adult_obesity, 100.0)
        Ers_data.rec_facilities_per_capita = round_div_float(
            rec_facilities_per_capita, 1000.0)


class ImportGroceryAccessData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        per_low_access_to_groceries = (
            counties['attributes']['PCT_LACCESS_POP10'])

        Ers_data.per_low_access_to_groceries = round_div_float(
            per_low_access_to_groceries, 100.0)


class ImportRestaurantData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        fast_food_rest_per_capita = counties['attributes']['FFRPTH11']
        full_rest_per_capita = counties['attributes']['FSRPTH11']

        Ers_data.fast_food_rest_per_capita = round_div_float(
            fast_food_rest_per_capita, 1000.0)
        Ers_data.full_rest_per_capita = round_div_float(
            full_rest_per_capita, 1000.0)


class ImportFarmersMarketData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        farmers_markets_per_capita = counties['attributes']['FMRKTPTH13']

        Ers_data.farmers_markets_per_capita = round_div_float(
            farmers_markets_per_capita, 1000.0)


class ImportSchoolMealData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        per_students_for_free_lunch = (
            counties['attributes']["PCT_FREE_LUNCH10"])
        per_students_for_reduced_lunch = (
            counties['attributes']["PCT_REDUCED_LUNCH10"])

        Ers_data.per_students_for_free_lunch = round_div_float(
            per_students_for_free_lunch, 100.0)
        Ers_data.per_students_for_reduced_lunch = round_div_float(
            per_students_for_reduced_lunch, 100.0)
