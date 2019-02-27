'''
   发布与订阅是不同于存值取值，存值取值不需要同步，发布与订阅是需要同步的
   '''
'''
#这样是可以的，为了配套，使用下面的
import redis

obj = redis.Redis(password='helloworld')
obj.publish('fm104.5','hello')

'''
from RedisHelper import RedisHelper
obj = RedisHelper()
obj.public('hello world!')