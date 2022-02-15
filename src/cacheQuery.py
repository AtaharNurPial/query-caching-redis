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
sql = "SELECT Major,count(*) FROM Students GROUP BY Major"
'''redis object'''
R_SERVER = redis.Redis(host='localhost',port=6379, password='',db=0)

def cache_query(sql, TTL = 10):
    '''creating a hash key'''
    sql = sql.encode('utf-8')
    hash = hashlib.sha224(sql).hexdigest()
    # hash = hash.encode('utf-8')
    key = "sql cache: " + hash
    print("Key: ", key)

    with connection:
        with connection.cursor() as cursor:
            cached_data = R_SERVER.get(key)
            '''checking if cache is null'''
            if cached_data is not None:
                try:
                    return json.loads(cached_data)
                except:
                    '''running the query'''
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    '''setting cachce with expiry time'''
                    R_SERVER.set(key, json.dumps(result))
                    R_SERVER.expire(key, TTL)

                    return json.loads(cached_data)

    end_time = datetime.now()
    execution_time = end_time - start_time
    print(execution_time)


if __name__ == '__main__':
    cache_query(sql)


