# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import sqlite3

from scrapy.exceptions import DropItem

class SqlitePipeline(object):
    def __init__(self):
        # Possible we should be doing this in spider_open instead, but okay
        self.connection = sqlite3.connect('./rutez.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS sinset (id INTEGER PRIMARY KEY autoincrement, name VARCHAR(80))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS word (id INTEGER, name VARCHAR(80))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS rel (id INTEGER, name VARCHAR(20), link INTEGER)')
        self.sinsets=set()

    # Take the item and put it in database - do not allow duplicates
    def get_sinset(self, name):
        self.cursor.execute("select id from sinset where name=?", (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            self.cursor.execute("insert into sinset (name) values (?)", (name,))
            return self.cursor.lastrowid
            
        
    def process_item(self, item, spider):
        sid = self.get_sinset(item['name'])
        if sid != self.cursor.lastrowid:
          return DropItem("Duplicate item found: %s" % item)
        self.sinsets.add(sid)
        for i in item['words']:
          self.cursor.execute("insert into word (id, name) values (?,?)", (sid,i))
        for n,l in item['rels']:
          self.cursor.execute("insert into rel (id, name, link) values (?,?,?)", (sid, n, self.get_sinset(l)))

        self.connection.commit()
        return item
