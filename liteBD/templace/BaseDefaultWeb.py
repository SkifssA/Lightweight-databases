import sqlite3
from liteBD.logic.meta_class import register_callback as callback 
from liteBD.logic.meta_class import *

class BaseDefaultWeb(metaclass=MetaDecorator):
    AttrSettings = []
    def __init__(self):
        pass

    def requestSQL(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')

    def onRefresh(self):
        """Должен вернуть матрицу где 1 строка это название столбцов для List"""
        conn = sqlite3.connect(SETTING.nameDB)
        cursor = conn.cursor()
        cursor.execute(self.requestSQL())
        column_names = [description[0] for description in cursor.description]
        cursor.fetchall()
        return [column_names, *cursor.fetchall()]


    def getLayout(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')