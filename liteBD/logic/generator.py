import xml.etree.ElementTree as ET
import sqlite3
import glob

from liteBD.templace.ClassTemp import *
import liteBD.SETTING as SETTING
from .requestBD import setReguest

def generatorAllClass():
    pattern = "**/*.xml"  # Двойная звёздочка означает "любая глубина"
    # Поиск файлов
    files = glob.glob(pattern, recursive=True)
    for file in files:
        generatorClass(file)

def generatorClass(path: str):
    data = _parseXml(path)
    pathDir = path[:max(path.rfind('/'), path.rfind('\\'))]
    _createTab(data)
    
    data['attrs'].append({'name': 'id', 'caption': 'id', 'isVisible': False, 'refClass': None, 'order': -1, 'attrType': 'Integer'})
    _createGui(data, pathDir)
    _createLog(data, pathDir)
    


def _parseXml(path: str):
    data = {}
    root = ET.parse(path)
    data['name']=root.getroot().get('name')
    data['caption']=root.getroot().get('caption')
    data['attrs'] = []
    for attr in root.find('attributes').findall('attr'):
        attrDict = {
            'name': attr.get('name'),
            'attrType': attr.get('attrType'),
            'order': attr.get('order', 10000),
            'caption': attr.get('caption', attr.get('name')),
            'refClass': attr.get('refClass'),
            'isVisible': attr.get('isVisible', True)
        }
        data['attrs'].append(attrDict)
    return data

def _createTab(data: dict):
    setReguest(f'''
    CREATE TABLE IF NOT EXISTS {data['name']} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sHeadLine Text,
        {',\n'.join(f'{attr['name']} {attr['attrType']}' for attr in data['attrs'])}
    )
    ''')

def _createGui(data: dict, path: str):
    try:
        with open(f"{path}/{data['name']}GuiV.py", 'w', encoding='UTF-8') as f:
            f.write(TempGuiV.format(**{'request': _createRequest(data)
                                       ,'AttrSettings': _createDictAttr(data)
                                       ,'name': data['name']}))

        with open(f"{path}/{data['name']}GuiA.py", 'x', encoding='UTF-8') as f:
            f.write(TempGuiA.format(**{'name': data['name']
                                       ,'pathFull': _getpathFull(path)}))
    except FileExistsError:
        pass

def _createRequest(data: dict):
    global n1, n2
    n2, n1 = 0, 0
    def attrStr(attr: dict):
        global n1
        if attr['refClass'] is None:
            return f't.{attr['name']}'
        else:
            n1 += 1
            return f't.{attr['name']},\n\t\t\tt{n1}.sHeadLine as {attr['name']}HL'
        
    def joinStr(attr: dict):
        global n2
        if attr['refClass'] is not None:
            n2 += 1
            return f'LEFT JOIN {attr['refClass']} t{n2} ON t{n2}.id = t.{attr["name"]}' 
        else: return ''
        

    return f'''
     SELECT 
\t\t\t{',\n\t\t\t'.join(attrStr(attr) for attr in data['attrs'])}
        FROM {data['name']} t
\t\t\t{'\n\t\t\t'.join(x for attr in data['attrs'] if (x:=joinStr(attr)) != '')}
    \t'''

l, r = '{', '}'

def _createDictAttr(data: dict):
    return f'''[
        {',\n\t\t'.join(l + f'\'name\': \'{attr['name']}\', \'caption\': \'{attr['caption']}\', '+\
                       f'\'isVisible\': {attr['isVisible']}, \'isReference\': {attr['refClass'] is not None}, '+\
                       f'\'order\':{attr['order']}, \'attrType\':\'{attr['attrType']}\'' + r
                       for attr in data['attrs'])}
    ]
    '''
    
def _getpathFull(path:str):
    return '.'.join(path.split('/'))

def _createLog(data: dict, path: str):
    try:
        with open(f"{path}/{data['name']}LogV.py", 'w', encoding='UTF-8') as f:
            f.write(TempLogV.format(**{'name': data['name']
                                       ,'classAttr': _getClassAttr(data)
                                       ,'setter': _getSetter(data)
                                       ,'attrs': _getAttrs(data)
                                       ,'request': _getRequest(data)
                                       ,'asDict': f'{l}w[0][i]: w[1][i] for i in range(len(w[0])){r}'}))

        with open(f"{path}/{data['name']}LogA.py", 'x', encoding='UTF-8') as f:
            f.write(TempLogA.format(**{'name': data['name']
                                       ,'pathFull': _getpathFull(path)}))
    except FileExistsError:
        pass

def _getRequest(data):
    return f"""SELECT
    {',\n'.join(f't.{attr['name']}' for attr in data['attrs'])}
    FROM {data['name']} t
    WHERE t.id = {l}id{r}"""

def _getAttrs(data: dict):
    return f'{', '.join(f"{i['name']}=None" for i in data['attrs'])}'

def _getClassAttr(data: dict):
    t = ' '*8
    return f"""{t}{f'\n{t}'.join(f"self.{i['name']}={i['name']}" for i in data['attrs'])}
"""

def _getSetter(data:dict):
    t = ' '*4
    return f"""
    {f'\n{t}'.join(TempSetter.format(**{'name': data['name'], 'classAttr': i['name']}) for i in data['attrs'])}
"""



