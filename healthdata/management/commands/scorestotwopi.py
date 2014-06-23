from __future__ import print_function

from django.core.management.base import BaseCommand

from healthdata.utils import score_tree_to_twopi


class Command(BaseCommand):
    args = ''
    help = 'Export a twopi graph of the scores tree'

    def handle(self, *args, **options):
        twopi = score_tree_to_twopi()
        print(twopi)
