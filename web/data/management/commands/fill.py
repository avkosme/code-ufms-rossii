from django.core.management.base import BaseCommand, CommandError
from data.models import d4826085213, d6162070130, d6168077734, StatisticFind
from ufms.models import Ufms


class Command(BaseCommand):
    help = 'Fill data codes from fms table'

    def add_arguments(self, parser):
        parser.add_argument(
            'action'
        )

    def handle(self, *args, **options):
        if options.get('action'):
            if options.get('action') == 'start':
                self.stdout.write('Started')
                fill = Fill()
                fill.main()
                self.stdout.write('Finished')


class Fill():
    def __init__(self):
        self.data = False
        self.ufms = False
        self.len = False
        self.count = 0

    def main(self):
        datas = d6168077734.objects.filter(code__exact='').all()
        for self.data in datas:
            self.search()


    def len_bad_pass_issued(self):
        self.len = len(self.data.pass_issued.split(' '))
        if self.len < 3:
            self.count = self.count + 1

    def search(self):
        try:
            self.ufms = Ufms.objects.filter(name__icontains=self.data.pass_issued).all()
            if self.ufms:
                print('Совпадение!')
                self.save()
                self.data.code = self.ufms[0].number
                print(self.data.code)
            else:
                print('Не найдено')
        except Ufms.DoesNotExist:
            print('Не найдено')

    def save(self):
        self.data.code = self.ufms[0].number
        self.data.save()
        self.save_statistic()

    def save_statistic(self):
        statisticFind = StatisticFind()
        statisticFind.model_name = 'd6168077734'
        statisticFind.id_find = self.data.pk
        statisticFind.save()
