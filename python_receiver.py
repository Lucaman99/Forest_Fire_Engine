import MySQLdb
import time

arr = []

def one():

    db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="testing")

    cur = db.cursor()
    cur.execute("SELECT * FROM test")
    data = cur.fetchall()
    db.close()

    arr.append(data[len(data) - 1][1])

    print(data[len(data) - 1][1])
    base = len(data)

    def send():

        db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="testing")

        cur = db.cursor()
        cur.execute("SELECT * FROM test")
        datat = cur.fetchall()
        db.close()


        if (base != len(datat)):
            one()
        else:
            time.sleep(0.1)
            send()

    send()

one()
