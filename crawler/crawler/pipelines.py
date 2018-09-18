# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CrawlerPipeline(object):

    def open_spider(self, spider):
      self.list = []
      self.file = open('result.json', 'w')

    def close_spider(self, spider):
      self.file.write(json.dumps(self.list, indent=4))
      self.file.close()
    
    def process_item(self, item, spider):
      self.list.append(dict(item))
      return item
