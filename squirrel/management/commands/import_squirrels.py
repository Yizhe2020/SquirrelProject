import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from adopt.models import Pet


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        squirrel  = []
        for dict_ in data:
            squirrel.append(Squirrel(
                x = dict_['X']
                y = dict_['Y']
            ))

       # Pet.objects.bulk_create(squirrel)

