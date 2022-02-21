import sqlite3
import os
import AutomationforWCBS

"""db_path = os.getenv('HOME')+'/mydb.db'
conn = sqlite3.connect(db_path)
print(conn)"""

conn = sqlite3.connect("test.db", isolation_level=None)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, birthday text)")
        
test_tuple = (
    (3, 'park', ' 1234-21-2143'),
    (4, 'sad', '2314-23-23'),
    (5, 'asd', '352213-1523-12')
)

# c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?, ?, ?)", test_tuple) # test_tuple 한번에 삽입
c.execute("SELECT * FROM table1")
for row in c.fetchall():
    print(row)


print(AutomationforWCBS.ser)
conn.close()