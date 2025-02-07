import dash

nameDB = 'test.db'
selfApp = dash.Dash(__name__, suppress_callback_exceptions=True, prevent_initial_callbacks='initial_duplicate')