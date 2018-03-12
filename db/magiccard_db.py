import json
from db import mysql_conn
from resources import send_to_queue as queue

conn = mysql_conn.getConnection()

def get_expansion_all():
    try:
        with conn.cursor() as cursor:
            sql = "SELECT ExpansionId, Name FROM magicexpansion ORDER BY %s %s" % ('ExpansionId', 'ASC')
            cursor.execute(sql)

            list_ids = []

            for row in cursor.fetchall():
                list_ids.append(row['ExpansionId'])

            return list_ids

    except Exception as e:
        return "Failure to insert on mysql:\n%s" % e
        print("Failure to insert on mysql:\n%s" % e)

    conn.close()

def get_magiccard_all(id):
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM magiccard WHERE ExpansionId='"+ id +"'ORDER BY %s %s" % ('GathererId', 'ASC')
            cursor.execute(sql)
            row = cursor.fetchone()
            list_all = []
            c = 0
            while row is not None:
                list_all.append(row)
                data = json.loads(json.dumps(list_all))
                list_all = []
                queue.send(data)
                row = cursor.fetchone()
                c += 1

            sql = "SELECT Name FROM magicexpansion WHERE ExpansionId='"+ id +"'"
            cursor.execute(sql)
            row = cursor.fetchone()

            return row, c

    except Exception as e:
        return "Failure to insert on mysql:\n%s" % e
        print("Failure to insert on mysql:\n%s" % e)

    conn.close()
