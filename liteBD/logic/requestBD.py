import sqlite3
from liteBD import SETTING

def getReguest(sql: str)->list:
    conn = sqlite3.connect(SETTING.nameDB)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = x if (x:=cursor.fetchall()) else [[None]*len(cursor.description)]
    return [[description[0] for description in cursor.description], *data]

def setReguest(sql: str):
    conn = sqlite3.connect(SETTING.nameDB)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()