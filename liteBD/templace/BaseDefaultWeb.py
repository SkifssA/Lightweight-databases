import sqlite3
from liteBD.logic.meta_class import register_callback as callback 
from liteBD.logic.meta_class import *
from liteBD.logic.urlPars import openClass
from liteBD.SETTING import selfApp

class BaseDefaultWeb(metaclass=MetaDecorator):
    AttrSettings = []
    def __init__(self):
        pass

    def requestSQL(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')

    def whereSQL(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')

    def onRefresh(self):
        """Должен вернуть матрицу где 1 строка это название столбцов для List"""
        conn = sqlite3.connect(SETTING.nameDB)
        cursor = conn.cursor()
        cursor.execute(self.requestSQL() + (x if isinstance(x:=self.whereSQL(), str) else ''))
        column_names = [description[0] for description in cursor.description]
        cursor.fetchall()
        return [column_names, *cursor.fetchall()]

    def _getStandartLayout(self):
        return (dcc.Location(id='url', refresh=False),)

    def getLayout(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')


    @selfApp.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname'),
        Input('url', 'search')
    )
    def display_page(pathname, search):
        params = None
        if len(search) > 4:
            params = dict([p.split('=') for p in search[1:].split('&')])
        print(pathname)
        if len(str(pathname)) > 4:
            className, subClassName = str(pathname)[1:].split('/')
            return openClass(className, subClassName, params)