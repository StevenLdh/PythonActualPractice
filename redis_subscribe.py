#!/usr/bin/env python
# -*- coding:utf8 -*-

# redis订阅
from RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)   # [b'message', b'fm104.5', b'who are you?']
    # print(msg[2].decode('utf8'))

