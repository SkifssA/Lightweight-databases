from .custom_decorator import *
from dash import dcc, html, Input, Output, State

layoutType = {
    'Input': lambda x: dcc.Input(id=x['name']),
    'LookUp': lambda x: dcc.Dropdown(id=x['name']),
    'Button': lambda x: html.Button(x['caption'], id=x['name'])
}

class MetaDecorator(type):
    def __new__(cls, name, bases, dct):
        # Словарь для хранения имён методов и их параметров
        decorated_methods = []
        # Проходим по всем методам класса

        print(name)
        for attr_name, attr_value in dct.items():
            print(attr_name)
            if callable(attr_value):
                if hasattr(attr_value, '_setter'):
                    decorated_methods.append(cls.deroratorWork(
                        attr_value, attr_name, dct,(Input(attr_name, 'value'),)
                        ))
                elif hasattr(attr_value, '_oper'):
                    decorated_methods.append(cls.deroratorWork(
                        attr_value, attr_name, dct,(Input(attr_name, 'n_clicks'), *getattr(attr_value, '_custom_decorator_params', {})['state']),
                        {'typeEdit':'Button'}))
            
        # Добавляем словарь декорированных методов как атрибут класса
        dct['_decorated_methods'] = decorated_methods
        
        print(name, decorated_methods)

        return super().__new__(cls, name, bases, dct)
    
    def deroratorWork(attr_value, attr_name, dct, paramCallback, param={}):
        decorator_params = getattr(attr_value, '_custom_decorator_params', {})
        decorator_params['name'] = attr_name
        decorator_params = decorator_params | param
        # Применяем дополнительный декоратор с параметрами
        dct[attr_name] = register_callback(
            *paramCallback
        )(attr_value)

        return decorator_params