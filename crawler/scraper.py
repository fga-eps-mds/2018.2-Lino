import scrapy
import pdfx
import json
import pandas as pd
from pprint import pprint
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
        q['legenda'] = df[cols[0]]
        q['segunda'] = df[cols[1]] + df[cols[2]]
        q['terca'] = df[cols[3]] + df[cols[4]]
        q['quarta'] = df[cols[5]] + df[cols[6]]
        q['quinta'] = df[cols[7]]
        q['sexta'] = df[cols[8]] + df[cols[9]]
        q['sabado'] = df[cols[10]] + df[cols[11]]
        q['domingo'] = df[cols[12]] + df[cols[13]]
        return q

    def getDayMenu(self, fileName, day):
        df = pd.read_table(
            f'./outputs/{fileName}.tsv',
            sep='\t',
            # index_col=0,
            na_filter=False,
            header=1,
            skipfooter=3,
            dayfirst=True,
            parse_dates=True,
            engine='python')
        # rows = list(df.index.values)
        # print(rows)
        q = self.genQuerry(df)
        # leg = list(q['legenda'].values)
        # print(leg)
        return(q[day])

    def genJson(self):
        leg = self.getDayMenu('FGA1','legenda')
        data = self.getDayMenu('FGA1','sexta')
        rows = list(data.index.values)
        obj = {}
        obj['DESJEJUM'] = {}
        obj['ALMOÇO'] = {}
        obj['JANTAR'] = {}
        for item in rows:
            if leg[item] == 'DESJEJUM':
                flag = leg[item]
                continue
            elif leg[item] == 'ALMOÇO':
                flag = leg[item]
                continue
            elif leg[item] == 'JANTAR':
                flag = leg[item]
                continue
            elif leg[item] == '':
                leg[item] == 'Pão:'
            else:
                obj[flag][leg[item]] = data[item]
        pprint(obj)


#crawl = TheCrawler()
#crawl.runCrawler()
p = PdfReader()
# p.downloadMenu('FGA')
# p.getDayMenu('FGA1', 'sexta')
p.genJson()
