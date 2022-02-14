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

'''Redis Obj'''
R_SERVER = redis.Redis(host="localhost")

'''cursor'''
cursor = connection.cursor()

'''caching'''
cached_data = R_SERVER.get('Students')
if cached_data is not None:
    print(json.loads(cached_data))

# sql = "SELECT * FROM Students"
# sql = "SELECT Major,count(*) FROM Students GROUP BY Major"
sql = "SELECT `NAME`, `Major`, `id` FROM `Students` WHERE `Major`='ACE' ORDER BY `id` DESC LIMIT 10"
cursor.execute(sql)
result = cursor.fetchall()

'''set cache'''
R_SERVER.set(name = 'Students', value=json.dumps(result))

connection.close()
cursor.close()
R_SERVER.close()
print(result)
end_time = datetime.now()
execution_time = end_time - start_time
print(execution_time)

