from django.core.management.base import BaseCommand
from data.ers.loading import ers_importer

import logging


class Command(BaseCommand):
    args = ''
    help = 'Import Ers data'

    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format=" %(levelname)s %(name)s: %(message)s")
        ers_importer()
