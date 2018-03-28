import MySQLdb

x = raw_input("Entry 1")
y = raw_input("Entry 2")

db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="testing")

cursor = db.cursor()
cursor.execute("INSERT INTO test (value1, value2) VALUES ('%s', '%s')" % (int(x), y))
db.commit()
db.close()
