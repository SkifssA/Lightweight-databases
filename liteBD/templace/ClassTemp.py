TempGuiV = """from liteBD import *

class Default(BaseDefaultWeb):
    AttrSettings = {AttrSettings}
    def requestSQL(self)->str:
        return '''{request}'''
    
class List(Default, BaseListWeb):
    AttrSettings = {AttrSettings}
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = {AttrSettings}
    pass
"""

TempGuiA = """from {pathFull} import {name}GuiV
class Default({name}GuiV.Default):
    pass
    
class List({name}GuiV.List):
    pass

class Card({name}GuiV.Card):
    pass
"""

TempLogV = """
class Rop:
    def __init__(self, {attrs}):
{classAttr}

class {name}LogV:
    def insert():
        return {name}Rop()
    
    def load(id):
        w = getReguest("""""")
        return testClass2Rop(**w.__dict__)
{setter}
"""

TempLogA = """from {pathFull} import {name}LogV
class {name}LogA({name}LogV.{name}LogV):
    pass
"""

TempSetter = """def set{classAttr}(rop:{name}Rop, value):
        rop.{classAttr} = value
"""