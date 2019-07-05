import serial
import MySQLdb

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    read_serial = ser.readline()
    a = read_serial[read_serial.index('D')-1:len(read_serial)-1].split(',')
    b = ''
    for t in a:
        b = b + t +','
        

    print(b)

    db = MySQLdb.connect(host="localhost", user="root", passwd="a", db="basef")

    cursor = db.cursor()
    cursor.execute("INSERT INTO basef2 (input) VALUES ('%s')" % (b))
    db.commit()
    db.close()
