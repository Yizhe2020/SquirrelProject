import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from squirrel.models import Data
import datetime

class Command(BaseCommand):
    help = 'Import Squirrel Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['csv_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                obj =Data()
                obj.Latitude = item['X']
                obj.Longitude = item['Y']
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                temp = item['Date']
                date_str = temp[-4:]+'-'+temp[:2]+'-'+temp[2:4]
                obj.Date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                obj.Age = item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = item['Running'] == 'true'
                obj.Chasing = item['Chasing'] == 'true'
                obj.Climbing = item['Climbing'] == 'true'
                obj.Eating = item['Eating'] == 'true'
                obj.Foraging = item['Foraging'] == 'true'
                obj.Other_Activity = item['Other Activities']
                obj.Kuks = item['Kuks'] == 'true'
                obj.Quaas = item['Quaas'] == 'true'
                obj.Moans = item['Moans'] == 'true'
                obj.Tail_Flags = item['Tail flags'] == 'true'
                obj.Tail_Twitches = item['Tail twitches'] == 'true'
                obj.Approaches = item['Approaches'] == 'true'
                obj.Indifferent = item['Indifferent'] == 'true'
                obj.Runs_From = item['Runs from'] == 'true'

                obj.save()
        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))

