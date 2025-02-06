from functools import wraps

import liteBD.SETTING as SETTING

# Декоратор для регистрации callback'ов
def register_callback(*_args, **_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        func
        # Регистрация callback в приложении
        SETTING.selfApp.callback(
            *_args, **_kwargs # Параметры callback берутся из атрибута _callback_args
        )(wrapper)

        return wrapper

    return decorator

def Oper(caption, state=(), **kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs_func):
            return func(*args, **kwargs_func)

        # Помечаем функцию, чтобы мета-класс мог её найти
        wrapper._oper = True
        # Сохраняем параметры декоратора
        wrapper._custom_decorator_params = kwargs | {'caption': caption} | {'state': state}
        return wrapper
    return decorator

def Setter(**kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs_func):
            return func(*args, **kwargs_func)

        # Помечаем функцию, чтобы мета-класс мог её найти
        wrapper._setter = True
        # Сохраняем параметры декоратора
        wrapper._custom_decorator_params = kwargs
        return wrapper
    return decorator
