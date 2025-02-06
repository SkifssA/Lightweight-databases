TempGuiV = """from liteBD import *

class Default(BaseDefaultWeb):
    AttrSettings = {AttrSettings}
    def requestSQL(self)->str:
        return '''{request}'''
    
class List(Default, BaseListWeb):
    AttrSettings = {AttrSettings}
    pass
"""

TempGuiA = """from . import {name}GuiV
class {name}GuiA:
    class Default({name}GuiV.Default):
        pass
        
    class List({name}GuiV.List):
        pass
"""