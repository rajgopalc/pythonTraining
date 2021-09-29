import sqlite3

conn = sqlite3.connect('fileDB.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE iot_device")

cursor.execute("CREATE TABLE iot_device(device_id integer primary key,state TEXT)")

for i in range(0, 10, 1):
    if i % 2 == 0:
        cursor.execute("INSERT INTO iot_device VALUES (NULL,'off')")
    else:
        cursor.execute("INSERT INTO iot_device VALUES (NULL,'on')")

for i in cursor.execute("SELECT * FROM iot_device"):
    print(i)

val = cursor.execute("SELECT * FROM iot_device WHERE device_id=1")
for i in val:
    print(i[1])

conn.commit()

conn.close()
