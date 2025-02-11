from liteBD import *
from .Anp_GenreLogV import Anp_GenreLogV

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def requestSQL(self)->str:
        return '''
     SELECT 
			t.sCaption,
			t.id
        FROM Anp_Genre t
			
    	'''
    
class List(Default, BaseListWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    
    def onRefresh(self, param):
        return Anp_GenreLogV().load(param['id'])
