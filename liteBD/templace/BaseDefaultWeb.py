import sqlite3
from liteBD.logic.meta_class import register_callback as callback 
from liteBD.logic.meta_class import *
from liteBD.logic.urlPars import openClass, refreshClass
from liteBD.logic.requestBD import getReguest
from liteBD.SETTING import selfApp

def refreshLayout(pathname, search):
        if len(str(pathname)) > 4:
            className, subClassName = str(pathname)[1:].split('/')
        params = {'className': className}
        if search is not None:
            if len(search) > 4:
                params = params | dict([p.split('=') for p in search[1:].split('&')])
        return (className, subClassName, params)

class BaseDefaultWeb(metaclass=MetaDecorator):
    AttrSettings = []
    decorated_methods = []
    
    def requestSQL(self):
        pass

    def whereSQL(self):
        pass

    def onRefresh(self):
        """Должен вернуть матрицу где 1 строка это название столбцов для List"""
        return getReguest(self.requestSQL() + (x if isinstance(x:=self.whereSQL(), str) else ''))

    def _getStandartLayout(self):
        return (
            html.Div([*(layoutType[i['typeEdit']](i) for i in self.__class__.decorated_methods), html.Br()], id='ToolBar'),
                )
    
    def _getMainLayoutDefault(self):
        return html.Div([
            *self._getMainLayout()
        ], id='MainLayout')

    def getLayout(self):
        return html.Div([
            *self._getStandartLayout(),
            self._getMainLayoutDefault()
        ])

    def _getMainLayout(self):
        pass

    @selfApp.callback(
        Output('page-content', 'children', allow_duplicate=True),
        Input('url', 'pathname'),
        Input('url', 'search')
    )
    def display_page(pathname, search):
        return openClass(*refreshLayout(pathname, search))
        
    @Oper('Обновить', (
            Output('MainLayout', 'children', allow_duplicate=True),
            State('url', 'pathname'),
            State('url', 'search'),
    ))
    def refresh(pathname, search, n):
        return refreshClass(*refreshLayout(pathname, search))