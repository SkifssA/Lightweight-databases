from dash import dash_table
import pandas as pd

from .BaseDefaultWeb import *


class BaseListWeb(BaseDefaultWeb):
    def __init__(self):
        pass

    def getLayout(self):
        w = self.onRefresh()
        columns = self.__getStandartColumns()
        df = pd.DataFrame(w[1:], columns=w[0])
        return html.Div([
            *self._getStandartLayout(),
            *(layoutType[i['typeEdit']](i) for i in self.__class__._decorated_methods),
            # Таблица без радиокнопок и чекбоксов
            dash_table.DataTable(
                id='table',
                columns=columns['data'],
                data=df.to_dict('records'),
                style_cell={'textAlign': 'left', 'padding': '8px'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                fixed_rows={'headers': True},  # Фиксированный заголовок
                style_table={
                    'height': '100%',  # Фиксированная высота
                    'overflowY': 'auto'  # Включение вертикального скролла
                },
                style_data_conditional=[  # Условные стили для выделения строки
                    {
                        'if': {'state': 'active'},  # Выделение активной строки
                        'backgroundColor': '#D1E7DD',  # Цвет фона
                        'border': '2px solid #198754'  # Граница вокруг строки
                    },
                ],
                style_cell_conditional = columns['style']
            ),
        ])
    

    def __getStandartColumns(self)->dict:
        res = {
             'data': [],
             'style': []
        }

        for attr in sorted(self.__class__.AttrSettings, key=lambda x: x['order']):
            if not attr['isReference']:
                if not attr['isVisible']:
                    res['style'].append({'if': {'column_id': attr['name']}, 'display': 'none'})
            else:
                if not attr['isVisible']:
                    res['style'].append({'if': {'column_id': f'{attr['name']}HL'}, 'display': 'none'})
                res['style'].append({'if': {'column_id': attr['name']}, 'display': 'none'})

                res['data'].append({'id': f'{attr['name']}HL', 'name': f'{attr['caption']}'})

            res['data'].append({'id': attr['name'], 'name': attr['caption']})
        return res

    @callback(
            Output('table', 'style_data_conditional'),
            Input('table', 'active_cell')
        )
    def refreshColorSelectRow(active_cell):
            if active_cell is None:
                return []
            
            # Получаем индекс строки из active_cell
            row_index = active_cell['row']
            # Форматируем вывод
            return [{
                        'if': {'row_index': row_index},  # Зебра-стиль для нечетных строк
                        'backgroundColor': '#f0f0ff'
                    }]
    
    # Примеры Setter и Oper
    # @Setter(typeEdit='Input')
    # def setRow(value):
    #     print(value)

    @Oper('Тесты')
    def openList(value):
        print(value)
