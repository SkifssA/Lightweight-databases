from liteBD import *

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0},
		{'name': 'nRow', 'caption': 'None', 'isVisible': True, 'isReference': False, 'order':None},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1}
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
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0},
		{'name': 'nRow', 'caption': 'None', 'isVisible': True, 'isReference': False, 'order':None},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1}
    ]
    
    pass
