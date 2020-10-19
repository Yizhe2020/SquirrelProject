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
                obj = Data()
                obj.Latitude = item['X']
                obj.Longitude = item['Y']
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                temp = item['Date']
                date_str = temp[-4:]+'-'+temp[:2]+'-'+temp[2:4]
                obj.Date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                obj.Age = item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = str(item['Running']) == 'true'
                obj.Chasing = str(item['Chasing']) == 'true'
                obj.Climbing = str(item['Climbing']) == 'true'
                obj.Eating = str(item['Eating']) == 'true'
                obj.Foraging = str(item['Foraging']) == 'true'
                obj.Other_Activity = item['Other Activities']
                obj.Kuks = str(item['Kuks']) == 'true'
                obj.Quaas = str(item['Quaas']) == 'true'
                obj.Moans = str(item['Moans']) == 'true'
                obj.Tail_Flags = str(item['Tail flags']) == 'true'
                obj.Tail_Twitches = str(item['Tail twitches']) == 'true'
                obj.Approaches = str(item['Approaches']) == 'true'
                obj.Indifferent = str(item['Indifferent']) == 'true'
                obj.Runs_From = str(item['Runs from']) == 'true'

                obj.save()

        msg = f'you are importing from {file_}'

        self.stdout.write(self.style.SUCCESS(msg))

