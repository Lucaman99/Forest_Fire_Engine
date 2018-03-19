import serial
import MySQLdb

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    read_serial = ser.readline()
    a = read_serial[read_serial.index('D'):len(read_serial)-1].split(',')

    print(a)

    db = MySQLdb.connect(host="localhost", user="root", passwd="a", db="basef")

    cursor = db.cursor()
    cursor.execute("INSERT INTO basef (distance, temperature, humidity, coordinates, thermal_camera, light, gyroscope) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (a[0], a[1], a[2], a[3], a[4], a[5], 0))
    db.commit()
    cursor.execute('SELECT distance FROM basef')
    r = cursor.fetchall()
    print(r)
    db.close()
