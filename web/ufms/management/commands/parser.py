from django.core.management.base import BaseCommand, CommandError
from lxml import html
import requests
from ufms.models import Ufms


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            'action'
        )

    def handle(self, *args, **options):
        if options.get('action'):
            if options.get('action') == 'parse':
                self.stdout.write('Started')
                parser = Parser()
                parser.main()
                self.stdout.write('Finished')


class Parser:
    ROOT_URL = 'http://ufms-rossii-gov.ru'

    def __init__(self):
        self.write = False
        self.file = False

        self.name = False
        self.number = False

    def main(self):
        page = requests.get(Parser.ROOT_URL + '/spravochnik-kodov-ufms-rossii/')
        tree = html.fromstring(page.content)
        areas = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/ul//a/@href')

        if self.write:
            self.file = open('out.csv', 'w')

        for area in areas:
            if self.write:
                self.file.write(self.get_codes(area))
            else:
                self.get_codes(area)
        if self.write:
            self.file.close()

    def get_codes(self, url):
        page = requests.get(Parser.ROOT_URL + url)
        tree = html.fromstring(page.content)

        code = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr[2]/td[1]/text()')
        area = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr[2]/td[2]/text()')

        codes = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr//text()')

        self.file = open('media/out.csv', "a")

        # codes = map(lambda s: s.strip(), codes)

        codes = [x for x in codes if x != '\n']
        codes = [x for x in codes if x != 'Кем выдан\n']
        codes = [x for x in codes if x != 'Код подразделения\n']

        for key, code in enumerate(codes):

            if key % 2 == 0 and code:
                self.name = code
                self.name = code
                self.name = self.name.replace("\n", "")
                self.name = self.name.strip()
            else:
                self.number = code
                self.number = self.number.replace("\n", "")
                self.number = self.number.strip()

            print(self.name)
            print(self.number)
            if self.name and self.number:
                self.save(name=self.name, number=self.number)

    def save(self, name, number):
        try:
            print(name, number)
            ufms = Ufms()
            ufms.name = name
            ufms.number = number
            ufms.save()
        except:
            pass
