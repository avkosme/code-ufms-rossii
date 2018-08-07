from lxml import html
import requests
import utmf.models.Ufms


class Parser:
    ROOT_URL = 'http://ufms-rossii-gov.ru'

    def __init__(self):
        self.write = False
        self.file = False

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
                return
        if self.write:
            self.file.close()

    def get_codes(self, url):
        page = requests.get(Parser.ROOT_URL + url)
        tree = html.fromstring(page.content)

        code = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr[2]/td[1]/text()')
        area = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr[2]/td[2]/text()')

        codes = tree.xpath('/html/body/div[1]/div/div[1]/div/article/div/table/tbody/tr/*/text()')

        for code in codes:
            print('xx')

        return

        # self.file = open('out.csv', "a")
        # for line in codes:
        #     self.file.write(line)
        #     return
        # self.file.close()

        try:

            ufms = Ufms()
            ufms.name = area[0]
            ufms.number = code[0]
            ufms.save()

            # print(code[0])
            # print(area[0])
            # return ''.join((code[0], ';', area[0]))
        except:
            return ''


if __name__ == '__main__':
    parser = Parser()
    parser.main()
