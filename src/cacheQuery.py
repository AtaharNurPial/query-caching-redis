import json
import pymysql
import redis
from datetime import datetime

'''start time'''
start_time = datetime.now()

'''db connection'''
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='testDB')

'''queries'''
sql = "SELECT Major,count(*) FROM Students GROUP BY Major"
# sql = "SELECT count(*) FROM Students"
# sql = "SELECT `NAME`, `Major`, `id` FROM `Students` WHERE `Major`='ACE' ORDER BY `id` DESC LIMIT 10"
# '''execution'''
with connection:
    with connection.cursor() as cursor:
        '''redis object'''
        R_SERVER = redis.Redis(host='localhost',port=6379, password='',db=0)

        '''get cahce data of Students as key and check if cache is not null'''
        cached_data = R_SERVER.get('Students')
        if cached_data is not None:
            try:
                print(json.loads(cached_data))
            except:
                print("Cache is Empty!!!")

        cursor.execute(sql)
        result = cursor.fetchall()
        '''setting cache value'''
        R_SERVER.set(name= 'Students', value= json.dumps(result))
        R_SERVER.close()
    cursor.close()
# print(result)
end_time = datetime.now()
execution_time = end_time - start_time
print(execution_time)
# connection.close()

# '''Redis Obj'''
# R_SERVER = redis.Redis(host="localhost")

# '''cursor'''
# cursor = connection.cursor()

# '''caching'''
# cached_data = R_SERVER.get('Students')
# if cached_data is not None:
#     print(json.loads(cached_data))

# # sql = "SELECT count(*) FROM Students"
# sql = "SELECT Major,count(*) FROM Students GROUP BY Major"
# # sql = "SELECT `NAME`, `Major`, `id` FROM `Students` WHERE `Major`='ACE' ORDER BY `id` DESC LIMIT 10"
# cursor.execute(sql)
# result = cursor.fetchall()

# '''set cache'''
# R_SERVER.set(name = 'Students', value=json.dumps(result))

# cursor.close()
# R_SERVER.close()
# connection.close()
# print(result)
# end_time = datetime.now()
# execution_time = end_time - start_time
# print(execution_time)

