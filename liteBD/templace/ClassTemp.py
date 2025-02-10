TempGuiV = """from liteBD import *
from .{name}LogV import {name}LogV

class Default(BaseDefaultWeb):
    AttrSettings = {AttrSettings}
    def requestSQL(self)->str:
        return '''{request}'''
    
class List(Default, BaseListWeb):
    AttrSettings = {AttrSettings}
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = {AttrSettings}
    def __init__(self):
        super().__init__()
        self.register_input_callbacks()
        
    def onRefresh(self, param):
        return {name}LogV().load(param['id'])
"""

TempGuiA = """from {pathFull} import {name}GuiV
class Default({name}GuiV.Default):
    pass
    
class List({name}GuiV.List):
    pass

class Card({name}GuiV.Card):
    pass
"""

TempLogV = """from liteBD import *
class Rop:
    tablName = '{name}'
    def __init__(self, {attrs}):
{classAttr}

class {name}LogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''{request}''')
        return Rop(**{asDict})
{setter}
"""

TempLogA = """from {pathFull} import {name}LogV
class {name}LogA({name}LogV.{name}LogV):
    pass
"""

TempSetter = """def set{classAttr}(rop:Rop, value):
        rop.{classAttr} = value
"""