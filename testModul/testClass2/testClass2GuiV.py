from liteBD import *
from .testClass2LogV import testClass2LogV

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'Кол-во', 'isVisible': True, 'isReference': False, 'order':10, 'attrType':'Integer'},
		{'name': 'idTestClass', 'caption': 'TestClass', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def requestSQL(self)->str:
        return '''
     SELECT 
			t.sCaption,
			t.nRow,
			t.idTestClass,
			t1.sHeadLine as idTestClassHL,
			t.id
        FROM testClass2 t
			LEFT JOIN testClass t1 ON t1.id = t.idTestClass
    	'''
    
class List(Default, BaseListWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'Кол-во', 'isVisible': True, 'isReference': False, 'order':10, 'attrType':'Integer'},
		{'name': 'idTestClass', 'caption': 'TestClass', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'nRow', 'caption': 'Кол-во', 'isVisible': True, 'isReference': False, 'order':10, 'attrType':'Integer'},
		{'name': 'idTestClass', 'caption': 'TestClass', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def onRefresh(self):
        return testClass2LogV().load()
