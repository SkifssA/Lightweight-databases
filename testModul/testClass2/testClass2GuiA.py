from . import testClass2GuiV
from .testClass2GuiV import *

class testClass2GuiA:
    class Default(testClass2GuiV.Default):
        pass
        
    class List(testClass2GuiV.List):
        @Oper('Хуета', State('table', 'id'))
        def weq(value, id):
            print('123123')
