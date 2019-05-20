#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
# 读取超过内存的文档
from mmap import mmap
def get_lines(fp):
    with open(fp,"r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1

if __name__=="__main__":
    for i in get_lines("D:\movies.xml"):
        print(i)
'''

'''
# 获取当前日期在本年的第几天
import datetime
def getDateInday():
    year = input("请输入年份")
    month =input("请输入月份")
    day =input("请输入日期")
    curdata = datetime.date(year=int(year),month=int(month),day=int(day))
    begindata = datetime.date(year=int(year),month=1,day=1)

    return (curdata-begindata).days+1

if __name__=="__main__":
    print(getDateInday())
'''


def count_str(str_data):
    """定义一个字符出现次数的函数"""
    dict_str = {}
    for i in str_data:
        dict_str[i] = dict_str.get(i,0)+1
    return dict_str
dict_str = count_str("AAABBCCAC")
str_count_data = ""
for k,v in dict_str.items():
    str_count_data += k +str(v)
print(str_count_data)











