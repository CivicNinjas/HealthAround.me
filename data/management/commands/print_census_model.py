from django.core.management.base import BaseCommand
from data.census.loading import CensusLoader
from data.census.definitions import TABLES


class Command(BaseCommand):
    args = ''
    help = 'Print the Census model definition'

    def handle(self, *args, **options):
        cl = CensusLoader(table_ids=TABLES)
        self.stdout.write(cl.model_declaration())
