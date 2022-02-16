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


with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('HELLO','world@to.com','ENV'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('bug','fix@app.com','CSE'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('ignorance','is@bliss.com','PHL'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('mrbeast','beast@yt.com','RAD'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('dani','milkman@karlson.com','CSE'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('dummy','data@app.com','DUM'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('pol','pol@email.com','POL'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('env','env@email.com','ENV'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('ecn','ecn@app.com','ECN'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('ace','ace@app.com','ACE'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('bus','bus@app.com','BUS'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('pr','pr@app.com','PR'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('spo','fsp@app.com','SPO'))
    #         except:
    #             print("Nothing to insert...")
    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('alp','alp@app.com','ALP'))
    #         except:
    #             print("Nothing to insert...")

    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('eee','fix@eee.com','EEE'))
    #         except:
    #             print("Nothing to insert...")
        
    #     for i in range(5000):
    #         sql = "INSERT INTO `Students` (`Name`, `email`, `Major`) VALUES (%s, %s, %s)"
    #         try:
    #             cursor.execute(sql, ('aws','fix@app.com','AWS'))
    #         except:
    #             print("Nothing to insert...")

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # try:
    #     connection.commit()
    # except:
    #     print("Failed to insert...")

    with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT `id`, `Name`, `email` FROM `Students` WHERE `Major`=%s"
        # sql = "SELECT `NAME`, `Major`, `id` FROM `Students` WHERE `Major`='ACE' ORDER BY `id` DESC LIMIT 10"
        # sql = "SELECT * FROM `Students` ORDER BY `id` DESC LIMIT 10"
        sql = "SELECT count(*) FROM Students"
        # sql = "SELECT `Major`,count(*) FROM `Students` GROUP BY `Major`"
        # cursor.execute(sql, ('CSE',))
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
end_time = datetime.now()
execution_time = end_time - start_time
print(execution_time)

