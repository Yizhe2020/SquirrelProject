from django.http import HttpResponse

import csv

from django.core.management.base import BaseCommand

from squirrel.models import Data


class Command(BaseCommand):
    help = 'export the squirrel data csv'

    def add_arguments(self,parser):
        parser.add_argument('csv_file', help = 'file exported')

    def handle(self, *args, **options):
        file_= options['csv_file']

        with open(file_, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Latitude','Longitude','Unique Squirrel ID','Shift','Date','Age',
                'Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging',
                'Other Activity','Kuks','Quaas','Moans','Tail Flags','Tail Twitches','Approaches',
                'Indifferent','Runs_From'])
            for i in Data.objects.all().values_list('Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age',
                'Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging',
                'Other_Activity','Kuks','Quaas','Moans','Tail_Flags','Tail_Twitches','Approaches',
                'Indifferent','Runs_From'):
                writer.writerow(i)

            csvfile.close()

        msg = f'you are exporting to {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
