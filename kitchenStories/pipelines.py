# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno
class KitchenstoriesPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host='127.0.0.1',
                                            db='foodnutrifrombh',
                                            user='root',
                                            passwd='root',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
    def _conditional_insert(self,tx,item):
        sql = "insert into kitchenstrories_copy_copy(chinesename,videourl,catid,catname,imgurl,videosourceurl,ngnixurl,source) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        tx.execute(sql, (item["chinesename"], item['videourl'], item['catid'], item['catname'],item['imgurl'],item['videosourceurl'],item['ngnixurl'],item['source']))


