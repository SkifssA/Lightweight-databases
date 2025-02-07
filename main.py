from dash import Dash, dcc, html, callback_context
import random

from liteBD import *


getGuiAFile()
generatorAllClass()


app = SETTING.selfApp

# Layout приложения
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Для маршрутизации
    html.H1("Многостраничное приложение", style={'textAlign': 'center'}),
    dcc.Link('Перейти на страницу 1', href='/testClass2/Card?id=1', style={'marginRight': '20px'}),
    dcc.Link('Перейти на страницу 2', href='/testClass2/List'),
    html.Div(id='page-content')  # Содержимое текущей страницы
])

# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)