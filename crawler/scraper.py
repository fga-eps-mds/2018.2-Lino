import scrapy
import pdfx
import json
import pandas as pd
from tabula import convert_into
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'

class TheCrawler():
    def __init__(self):
        self.process = CrawlerProcess(get_project_settings())

    def runCrawler(self):
        self.process.crawl('RU')
        self.process.start()  # the script will block here until the crawling is finished

class JsonReader():
    def __init__(self):
        with open('result.json') as f:
            self.body = json.load(f)

class PdfReader():
    def __init__(self):
        self.data = JsonReader()
    
    def downloadMenu(self, campus):
        data = self.data
        n = 0
        for item in data.body:
            if campus in item['text']:
                pdf = pdfx.PDFx(item['url'])
                pdf.download_pdfs(DOWNLOAD_PATH)
                name = campus + str(n)
                n += 1
                fileName = item['url'].split('/')
                fileName = fileName.pop()
                convert_into(
                    f'{DOWNLOAD_PATH}{fileName}',
                    f'{OUTPUT_PATH}{name}.tsv',
                    output_format='tsv')

    def genQuerry(self, df):
        cols = list(df.columns.values)
        q = {}
        q['segunda'] = df[cols[0]] + df[cols[1]]
        q['terca'] = df[cols[2]] + df[cols[3]]
        q['quarta'] = df[cols[4]] + df[cols[5]]
        q['quinta'] = df[cols[6]]
        q['sexta'] = df[cols[7]] + df[cols[8]]
        q['sabado'] = df[cols[9]] + df[cols[10]]
        q['domingo'] = df[cols[11]] + df[cols[12]]
        return q

    def readTable(self, fileName):
        df = pd.read_table(
            f'./outputs/{fileName}.tsv',
            sep='\t',
            index_col=0,
            na_filter=False,
            header=1,
            skipfooter=3,
            dayfirst=True,
            parse_dates=True,
            engine='python')
        q = self.genQuerry(df)
        search = input('Insira a pesquisa: ')
        print(q[search])

#crawl = TheCrawler()
#crawl.runCrawler()
p = PdfReader()
p.readTable('FGA0')
#p.downloadMenu('FGA')
