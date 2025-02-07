from .custom_decorator import *
import pandas as pd
from dash import dcc, html, Input, Output, State

layoutType = {
    'Input': lambda x: dcc.Input(id=x['name']),
    'LookUp': lambda x: dcc.Dropdown(id=x['name']),
    'Button': lambda x: html.Button(x['caption'], id=x['name'])
}

class MetaDecorator(type):
    def __new__(cls, name, bases, namespace):
        # Словарь для хранения имён методов и их параметров
        decorated_methods = []
        parent_decorated_methods = []
        # Проходим по всем методам класса
        for attr_name, attr_value in namespace.items():
            if callable(attr_value):
                if hasattr(attr_value, '_setter'):
                    decorated_methods.append(cls.deroratorWork(
                        attr_value, attr_name, namespace,(Input(attr_name, 'value'),)
                        ))
                elif hasattr(attr_value, '_oper'):
                    decorated_methods.append(cls.deroratorWork(
                        attr_value, attr_name, namespace,(*getattr(attr_value, '_custom_decorator_params', {})['state'], Input(attr_name, 'n_clicks')),
                        {'typeEdit':'Button'}))
            
        for base in bases:
            if hasattr(base, 'decorated_methods'):   
                parent_decorated_methods += base.decorated_methods
        # Добавляем словарь декорированных методов как атрибут класса

        df = pd.DataFrame(parent_decorated_methods + decorated_methods)

        # Удаляем дубликаты
        df_unique = df.drop_duplicates()

        # Преобразуем обратно в список словарей
        unique_data = df_unique.to_dict(orient='records')

        namespace['decorated_methods'] = unique_data

        return super().__new__(cls, name, bases, namespace)
    
    def deroratorWork(attr_value, attr_name, dct, paramCallback, param={}):
        decorator_params = getattr(attr_value, '_custom_decorator_params', {})
        decorator_params['name'] = attr_name
        decorator_params = decorator_params | param
        # Применяем дополнительный декоратор с параметрами
        dct[attr_name] = register_callback(
            *paramCallback
        )(attr_value)

        return decorator_params