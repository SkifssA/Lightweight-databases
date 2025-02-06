from liteBD import *

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0},
		{'name': 'nRow', 'caption': 'Кол-во', 'isVisible': True, 'isReference': False, 'order':10},
		{'name': 'idTestClass', 'caption': 'TestClass', 'isVisible': True, 'isReference': True, 'order':20},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1}
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
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0},
		{'name': 'nRow', 'caption': 'Кол-во', 'isVisible': True, 'isReference': False, 'order':10},
		{'name': 'idTestClass', 'caption': 'TestClass', 'isVisible': True, 'isReference': True, 'order':20},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1}
    ]
    
    pass
