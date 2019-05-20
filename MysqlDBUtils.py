# -*- coding:utf-8 -*-
import pymysql

class MysqlDBUtils(object):

   def executesql(self,sqlstr, parma):
       __conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='today_news',charset='utf8')
       _cursor = __conn.cursor()
       _cursor.execute(sqlstr,parma)
