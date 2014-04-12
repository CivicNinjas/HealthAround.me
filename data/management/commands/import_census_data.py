from django.core.management.base import BaseCommand
from data.census.loading import CensusLoader
from data.census.definitions import TABLES, STATES

import logging


class Command(BaseCommand):
    args = ''
    help = 'Print the Census model definition'

    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format=" %(levelname)s %(name)s: %(message)s")
        cl = CensusLoader(table_ids=TABLES, states=STATES)
        cl.import_data()
