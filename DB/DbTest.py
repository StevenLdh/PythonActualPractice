
'''
# 文件操作类使用
import configparser
import os
os.chdir(r'D:/projectspace/PythonActualPractice/')
cf = configparser.ConfigParser()
cf.read("dbconf.ini")
host = cf.get("mysql", "host")
user = cf.get("mysql", "user")
pwd = cf.get("mysql", "password")
db = cf.get("mysql", "db")
'''

# 调用mysql数据访问类
from MysqlDBUtils import MysqlDBUtils;
sql = "select GID,FullName,ModifyTime from bas_goods where profileid=10004621;"
ms = MysqlDBUtils()
resList = ms.ExecQuery(sql)
for row in resList:
    print("GID: %d\tFullName: %s\tModifyTime: %s" % (row[0], row[1], row[2]))
ms.Close()

