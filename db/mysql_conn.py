# Function return a connection.
import pymysql.cursors

def getConnection():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root', db='tcgplace',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        return conn
    except Exception as e:
        return "Failure to connect with mysql:\n%s" % e
        print("Failure to connect with mysql:\n%s" % e)