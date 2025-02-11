from liteBD import *
from .testClassLogV import testClassLogV

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'nRow', 'isVisible': True, 'isReference': False, 'order':10000, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def requestSQL(self)->str:
        return '''
     SELECT 
			t.sCaption,
			t.nRow,
			t.id
        FROM testClass t
			
    	'''
    
class List(Default, BaseListWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'nRow', 'isVisible': True, 'isReference': False, 'order':10000, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'nRow', 'isVisible': True, 'isReference': False, 'order':10000, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    
    def onRefresh(self, param):
        return testClassLogV().load(param['id'])
