import sqlite3

db_path = "D:\Python\SideProject\AutomationForWCBS\Aging.db" #Aging log 저장 경로

def Update_DB(date, res):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute("CREATE TABLE IF NOT EXISTS AgingDB \
        (time text PRIMARY KEY, Log text)")
    c.execute('INSERT INTO AgingDB VALUES(?, ?);', (date, res))
    conn.commit()
    conn.close()