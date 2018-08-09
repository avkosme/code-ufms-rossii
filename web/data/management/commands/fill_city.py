from django.core.management.base import BaseCommand, CommandError
from data.models import d4826085213, d6162070130, d6168077734, StatisticFind
from ufms.models import Ufms
import random


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


class Fill:
    def __init__(self):
        self.data = False
        self.pass_issued = False
        self.pass_issued_split = False

    def main(self):
        datas = d4826085213.objects.filter(code__exact='')
        for self.data in datas:
            self.search()

    def search(self):
        self.pass_issued_split = self.data.pass_issued.split(' ')
        if len(self.pass_issued_split) > 3:
            for r in self.pass_issued_split:
                self.pass_issued = r.lower()
                if self.pass_issued not in self.exclude_dict():
                    self.cut_pass_issued()
                    if len(self.pass_issued) > 3:
                        try:
                            self.ufms = Ufms.objects.filter(name__icontains=self.pass_issued)
                            print(self.ufms.query)
                            self.ufms = self.ufms.all()
                            if self.ufms:
                                print('Совпадение!')
                                self.save()
                                print(self.data)
                            else:
                                print('Не найдено')
                        except Ufms.DoesNotExist:
                            print('Не найдено')

    def save(self):
        self.data.code = random.choice(self.ufms).number
        self.data.save()
        self.save_statistic()

    def cut_pass_issued(self):
        self.pass_issued = self.pass_issued[2:]
        self.pass_issued = self.pass_issued[:-2]

    def save_statistic(self):
        statisticFind = StatisticFind()
        statisticFind.model_name = 'd4826085213'
        statisticFind.id_find = self.data.pk
        statisticFind.save()

    def exclude_dict(self):
        return [
            'ао',
            'УФМС',
            'окр',
            'авт',
            'ОТДЕЛЕНИЕМ',
            'уфмс'
            'россии'
            'автоном.',
            'в',
            'внутренних',
            'спубли',
            'утренн',
            'управлением',
            'г',
            'гор',
            'г.',
            'г.мценск',
            'гор.',
            'гор',
            'города',
            'городе',
            'городским',
            'городскому',
            'дел',
            'и',
            'краю',
            'края',
            'межрайонным',
            'милиции',
            'мо',
            'мп',
            'мро',
            'мкр.',
            'обл.',
            'обл',
            '.',
            'обл.в',
            'обл,',
            'области',
            'овд',
            'овд',
            'окр.-',
            'округе',
            'округу',
            'отдела',
            'отдела',
            'отделением',
            'отдеоением',
            'отделение',
            'отделом',
            'отелом',
            'оуфмс',
            'оуфмс',
            'оуфмс',
            'оуфмс',
            'округа',
            'по',
            'пунктом',
            'пунктом',
            'р-на',
            'р-не',
            'ровд',
            'рувд',
            'района',
            'район',
            'районе',
            'республике',
            'респ',
            'республики',
            'респулике',
            'россии',
            'с.',
            'стерлитамак',
            'советском',
            'селе',
            'территориальным',
            'тп',
            'тп6оуфмс',
            'тп№3',
            'тыва',
            'увд',
            'управлением',
            'урае',
            'облости',
            'райне',
            'уфмс',
            'офмс',
            'уфсм',
            'центрального',
            'нсо',
            'при',
            'сао',
            'мос',
            'мвд',
            'ом',
            'столом',
            'отделение',
            'паспортным',
            'муниципальному',
            'отд.уфмс',
            'уфмсроссии',
            'ростовской',
            'городском',
            'дислокации',
            'межрайонного',
            'поселении',
            'москвы',
            'р-ну',
            'город',
            'во',
            'окр.',
            'рф',
            'п.',
            '-',
            'району',
            'цао',
            'отдел',
            'го',
            'пгт',
            'отдел',
            'о-нием',
            'отдел',
            'поселении',
            'межрайонного',
            'миграционного',
            'учета',
            'р-на',
            'р-он',
            'о/м',
            '№14',
            '№5',
            '№6',
            '№35',
            '№25',
            'тп№1',
            'от-ем',
            'округу,',
            'на',
            'с',
            'п',
            '',
            '63',
            '8',
            '39',
            '78',
            '71',
            '31',
            ' ',
            '',
            '121',
            '2',
            '3',
            '1',
            '№',
            '№1',
            '№1',
            '№4', ]
