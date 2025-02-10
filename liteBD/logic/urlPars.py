import sys
import importlib
import glob

def getClass(moduleName, subName:str, className = None):
    module_name = moduleName + subName
    class_name = className if className is not None else module_name + subName
    module = importlib.import_module(module_name)
    cls = getattr(module, class_name, None) 
    if cls:
        return cls()
    else:
        print(f"Класс {class_name} не найден")

def openClass(moduleName, className, param):
    return getClass(moduleName, 'GuiA', className).getLayout(param)
        

def refreshClass(moduleName, className, param):
    return getClass(moduleName, 'GuiA', className)._getMainLayout(param)

def getRop(param):
    return getClass(param['className'], 'LogA').load(param['id'])

def getHeadLine(className, id):
    return getClass(className, 'LogA').getHeadLine(id)

def getGuiAFile():
    # Шаблон для рекурсивного поиска
    pattern = "**/*GuiA.py"  # Двойная звёздочка означает "любая глубина"
    # Поиск файлов
    files = glob.glob(pattern, recursive=True)
    for file in files:
        f = file[:max(file.rfind('/'), file.rfind('\\'))]
        sys.path.append(f)