import sys
import importlib
import glob

def openClass(moduleName, className, param):
    # Имя модуля и класса
    module_name = moduleName + 'GuiA'  # Имя файла без .py
    class_name = className

    # Динамический импорт модуля
    module = importlib.import_module(module_name)

    # Получение класса
    cls = getattr(module, class_name, None)

    if cls:
        if param is None:
            return cls().getLayout()
        else:
            return cls().getLayout(param)
    else:
        print(f"Класс {class_name} не найден")

def refreshClass(moduleName, className, param):
    # Имя модуля и класса
    module_name = moduleName + 'GuiA'  # Имя файла без .py
    class_name = className

    # Динамический импорт модуля
    module = importlib.import_module(module_name)

    # Получение класса
    cls = getattr(module, class_name, None)

    if cls:
        if param is None:
            return cls()._getMainLayout()
        else:
            return cls()._getMainLayout(param)
    else:
        print(f"Класс {class_name} не найден")

def getGuiAFile():
    # Шаблон для рекурсивного поиска
    pattern = "**/*GuiA.py"  # Двойная звёздочка означает "любая глубина"
    # Поиск файлов
    files = glob.glob(pattern, recursive=True)
    for file in files:
        f = file[:max(file.rfind('/'), file.rfind('\\'))]
        sys.path.append(f)