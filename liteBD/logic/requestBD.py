import sqlite3
from liteBD import SETTING
from liteBD.logic.urlPars import getHeadLine

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

def setRop(rop):
    dictRop = rop.__dict__
    idRop = dictRop.pop('id')
    print(dictRop)
    if idRop is None:
        dictRop['sHeadLine'] = rop.sCaption
        setReguest(f"""INSERT INTO {rop.__class__.tablName} ({', '.join(i for i in dictRop.keys())})
        VALUES ({', '.join(f'\'{i}\'' if isinstance(i, str) else f'{i}' for i in dictRop.values())});""")
    else:
        dictRop['sHeadLine'] = getHeadLine(rop.__class__.tablName, dictRop)
        setReguest(f"""UPDATE {rop.__class__.tablName}
        SET {', '.join(f'{k}={v}' for k, v in dictRop.items())}
        WHERE id = {idRop};""")