import json
import pymysql
import pymysql.cursors
import redis
from datetime import datetime
import hashlib

'''start time'''
start_time = datetime.now()

'''db connection'''
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='testDB', cursorclass=pymysql.cursors.DictCursor)

'''queries'''
# sql = "SELECT Major,count(*) FROM Students GROUP BY Major"
# sql = "SELECT count(*) FROM Students"
sql = "SELECT * FROM `Students` ORDER BY `id` DESC LIMIT 5"
'''redis object'''
R_SERVER = redis.Redis(host='localhost',port=6379, password='',db=0)

cursor = connection.cursor()

def cache_query(sql, TTL = 3600):
    '''creating a hash key'''
    sql = sql.encode('utf-8')
    hash = hashlib.sha224(sql).hexdigest()
    # hash = hash.encode('utf-8')
    key = "cacheSQL:" + hash
    print("Key: ", key)

    if(R_SERVER.get(key)):
        print("This was return from redis") 
        return json.loads(R_SERVER.get(key))
    else:
        cursor.execute(sql)
        result = cursor.fetchall()

        R_SERVER.set(key, json.dumps(result))
        R_SERVER.expire(key, TTL)

        print ("Set data redis and return the data")
        return json.loads(R_SERVER.get(key))

end_time = datetime.now()
execution_time = end_time - start_time
print(execution_time)


if __name__ == '__main__':
    cache_query(sql)


