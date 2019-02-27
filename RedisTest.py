import redis
host = '127.0.0.1'
port = '6379'
# 增加程序连接池
'''
连接池：
当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
'''
pool=redis.ConnectionPool(host=host,port=port)
# 连接redis程序
'''
这种连接是连接一次就断了，耗资源.端口默认6379，就不用写
r = redis.Redis(host=host,port=port)
'''

'''
使用连接池
'''
r = redis.Redis(connection_pool=pool)

'''
# 设置并获取数据
r.set('name','steven')
print(r.get('name'))
'''

# 管道
'''
pipe = r.pipeline(transaction=True)
pipe.set('name','root')
pipe.set('role','root')
pipe.execute()
print(r.get('name'))
'''