from django.core.management.base import BaseCommand
from data.dartmouth.loading import dartmouth_importer

import logging


class Command(BaseCommand):
    args = ''
    help = 'Import Dartmouth data'

    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format=" %(levelname)s %(name)s: %(message)s")
        dartmouth_importer()
