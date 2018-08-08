from django.core.management.base import BaseCommand, CommandError
import csv
from data.models import d4826085213, d6162070130, d6168077734


class Command(BaseCommand):
    help = 'Import data from csv files'

    def add_arguments(self, parser):
        parser.add_argument(
            'action'
        )

    def handle(self, *args, **options):
        if options.get('action'):
            if options.get('action') == 'import':
                self.stdout.write('Started')
                parser = Data()
                parser.main()
                self.stdout.write('Finished')


class Data:
    def __init__(self):
        self.data = False

    def main(self):
        with open('media/6168077734.csv', newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')

            for row in spamreader:
                self.data = row
                self.set_attributes()

    def set_attributes(self):
        data = d6168077734()
        data.guid = self.data[0]
        data.fio = self.data[1]
        data.born_date = self.data[2]
        data.born_place = self.data[3]
        data.pass_num = self.data[4]
        data.pass_date = self.data[5]
        data.pass_issued = self.data[6]
        data.code = self.data[7]
        data.inn = self.data[8]
        data.name = self.data[9]
        data.number = self.data[10]
        data.save()
