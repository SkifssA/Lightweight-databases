from dash import dcc, html

from liteBD import *

generatorAllClass()
getGuiAFile()



app = SETTING.selfApp

# Layout приложения
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Для маршрутизации
    html.H1("Многостраничное приложение", style={'textAlign': 'center'}),
    dcc.Link('Перейти на страницу 1', href='/Anp_Anime/List', style={'marginRight': '20px'}),
    dcc.Link('Перейти на страницу 2', href='/Anp_Genre/List'),
    html.Div(id='page-content')  # Содержимое текущей страницы
])

# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)