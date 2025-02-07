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