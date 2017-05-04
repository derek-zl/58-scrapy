# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy import signals
import MySQLdb
import MySQLdb.cursors
from datetime import datetime
from hashlib import md5
from twisted.enterprise import adbapi


class GetAllPipeline(object):
    def __init__(self):
        self.file=codecs.open('58_getall_youxisheji_all.json','a',encoding='utf-8')
    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()
        

class MySQLStorePipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def fromf_settings(cls,settings):
        dbargs=dict(host=settings['MYSQL_HOST'],
                    db=settings['MYSQL_DBNAME'],
                    user=settings['MYSQL_USER'],
                    passwd=settings['MYSQL_PASSWD'],
                    charset='utf8',
                    cursorclass=MySQLdb.cursors.DictCursor,
                    use_unicode=True,
                    )
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbargs)
        return cls(dbpool)
    def process_item(self,item,spider):
        d=self.dbpool.runInteraction(self._do_upinsert,item,spider)
        d.addErrback(self._handle_error,item,spider)
        d.addBoth(lambda _:item)
        return d
    def _do_upinsert(self,conn,item,spider):
        linkmd5id=self._get_linkmd5id(item)
        now=datetime.utcnow().replace(microsecond=0).isoformat(' ')
        conn.execute("""
                    select 1 from cnblogsinfo where linkmd5id = %s
        """, (linkmd5id, ))
        ret=conn.fetchone()

        if ret:
            conn.execute("""
             update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
             """,(item['JobTitle'], item['Salary'], item['PushDate'], item['Position'],
                  item['Require'], item['City_address'], item['Authentication'], item['TelePhone'],
                   item['Scale'], item['Nature'], item['Address'], item['Position_intro'],item['JobUrls'],now, linkmd5id))

        else:
            conn.execute("""
                insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated) 
                values(%s, %s, %s, %s, %s, %s)
            """, (linkmd5id, item['JobTitle'], item['Salary'], item['PushDate'], item['Position'],
                  item['Require'], item['City_address'], item['Authentication'], item['TelePhone'],
                   item['Scale'], item['Nature'], item['Address'], item['Position_intro'],item['JobUrls'], now))


    def _get_linkmd5id(self, item):
        return md5(item['JobUrls']).hexdigest()

    def _handle_error(self, failue, item, spider):
        log.err(failure)

