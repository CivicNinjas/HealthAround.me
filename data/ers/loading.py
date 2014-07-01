import logging
import json

from boundaryservice.models import Boundary
from math import ceil

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


def round_float(float_num):
    return float(ceil(float_num * 10000) / 10000.0)


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
        grocery_stores_per_thousand = \
            counties['attributes']['GROCPTH11']

        Ers_data.grocery_stores_per_thousand = \
            round_float(grocery_stores_per_thousand)


class ImportObesityData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        adult_diabetes = counties['attributes']['PCT_DIABETES_ADULTS10']
        adult_obesity = counties['attributes']["PCT_OBESE_ADULTS10"]
        childhood_obesity = counties['attributes']["PCT_OBESE_CHILD11"]
        rec_facilities_per_thousand = counties['attributes']["RECFACPTH11"]

        Ers_data.adult_diabetes = float(adult_diabetes)
        Ers_data.adult_obesity = float(adult_obesity)
        if childhood_obesity is None:
            Ers_data.childhood_obesity = childhood_obesity
        else:
            Ers_data.childhood_obesity = float(childhood_obesity)
        Ers_data.rec_facilities_per_thousand = round_float(
            rec_facilities_per_thousand)


class ImportGroceryAccessData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        percent_low_access_to_groceries = \
            counties['attributes']['PCT_LACCESS_POP10']

        Ers_data.percent_low_access_to_groceries = round_float(
            percent_low_access_to_groceries)


class ImportRestaurantData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        fast_food_rest_per_thousand = counties['attributes']['FFRPTH11']
        full_rest_per_thousand = counties['attributes']['FSRPTH11']

        Ers_data.fast_food_rest_per_thousand = \
            round_float(fast_food_rest_per_thousand)
        Ers_data.full_rest_per_thousand = \
            round_float(full_rest_per_thousand)


class ImportFarmersMarketData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):
        farmers_markets_per_thousand = counties['attributes']['FMRKTPTH13']

        Ers_data.farmers_markets_per_thousand = \
            round_float(farmers_markets_per_thousand)


class ImportSchoolMealData(ImportDataFromJson):

    def finish_import(self, counties, Ers_data):

        percent_students_for_free_lunch = (
            counties['attributes']["PCT_FREE_LUNCH10"])
        percent_students_for_reduced_lunch = (
            counties['attributes']["PCT_REDUCED_LUNCH10"])

        Ers_data.percent_students_for_free_lunch = (
            percent_students_for_free_lunch)
        Ers_data.percent_students_for_reduced_lunch = (
            percent_students_for_reduced_lunch)
