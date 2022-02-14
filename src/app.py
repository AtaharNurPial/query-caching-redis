import pymysql
import pymysql.cursors
from datetime import datetime

start_time = datetime.now()
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='testDB',
                             cursorclass=pymysql.cursors.DictCursor)

# cursor = connection.cursor()
# sql = "SELECT * FROM Students"

# result = cursor.execute(sql)
# print(result)
with connection:
    # with connection.cursor() as cursor:
    # #     # Create a new record
    #     sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    # #     # cursor.execute(sql, ('Abdul Hoque', 'abc@gmail.com', 'CSE'))
    # #     cursor.execute(sql, ('Richard','tabsoverspaces@silval.com','CSE'))
    #     cursor.execute(sql, ('test10','test6@test.com','TEST'))
    #     cursor.execute(sql, ('test9','test7@test.com','TEST'))
    #     cursor.execute(sql, ('test8','test8@test.com','TEST'))
    #     cursor.execute(sql, ('test7','test9@test.com','TEST'))
    #     cursor.execute(sql, ('test6','test10@test.com','TEST'))


    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT `id`, `Name`, `email` FROM `Students` WHERE `Major`=%s"
        sql = "SELECT `NAME`, `Major`, `id` FROM `Students` WHERE `Major`='ACE' ORDER BY `id` DESC LIMIT 10"
        # sql = "SELECT * FROM `Students` ORDER BY `id` DESC LIMIT 10"
        # sql = "SELECT * FROM Students"
        # sql = "SELECT `Major`,count(*) FROM `Students` GROUP BY `Major`"
        # cursor.execute(sql, ('CSE',))
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
end_time = datetime.now()
execution_time = end_time - start_time
print(execution_time)

