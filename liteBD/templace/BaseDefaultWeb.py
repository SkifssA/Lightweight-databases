import sqlite3
from liteBD.logic.meta_class import register_callback as callback 
from liteBD.logic.meta_class import *
from liteBD.logic.urlPars import openClass
from liteBD.SETTING import selfApp

def refreshLayout(pathname, search):
        params = None
        if search is not None:
            if len(search) > 4:
                params = dict([p.split('=') for p in search[1:].split('&')])
        if len(str(pathname)) > 4:
            className, subClassName = str(pathname)[1:].split('/')
            return openClass(className, subClassName, params)

class BaseDefaultWeb(metaclass=MetaDecorator):
    AttrSettings = []
    decorated_methods = []
    
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
        return (dcc.Location(id='url', refresh=False), *(layoutType[i['typeEdit']](i) for i in self.__class__.decorated_methods), html.Br())

    def getLayout(self):
        print('НЕ ПЕРЕОПРЕДЕЛЕНО')

    

    @selfApp.callback(
        Output('page-content', 'children', allow_duplicate=True),
        Input('url', 'pathname'),
        Input('url', 'search')
    )
    def display_page(pathname, search):
        return refreshLayout(pathname, search)
        
    # @Oper('Обновить', (
    #         Output('page-content', 'children', allow_duplicate=True),
    #         State('url', 'pathname'),
    #         State('url', 'search'),
    # ))
    # def openList(n, pathname, search):
    #     return refreshLayout(pathname, search)