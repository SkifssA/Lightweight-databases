from liteBD import *
from .Anp_AnimeLogV import Anp_AnimeLogV

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'sUrl', 'caption': 'Ссылка', 'isVisible': False, 'isReference': False, 'order':10, 'attrType':'Text'},
		{'name': 'nScore', 'caption': 'Оценка', 'isVisible': True, 'isReference': False, 'order':20, 'attrType':'Integer'},
		{'name': 'sCommentSite', 'caption': 'Описание', 'isVisible': True, 'isReference': False, 'order':30, 'attrType':'Text'},
		{'name': 'sComment', 'caption': 'Мой коментарий', 'isVisible': True, 'isReference': False, 'order':40, 'attrType':'Text'},
		{'name': 'bVisible', 'caption': 'Просмотренно', 'isVisible': True, 'isReference': False, 'order':50, 'attrType':'Integer'},
		{'name': 'bEnd', 'caption': 'Закончилось', 'isVisible': True, 'isReference': False, 'order':60, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def requestSQL(self)->str:
        return '''
     SELECT 
			t.sCaption,
			t.sUrl,
			t.nScore,
			t.sCommentSite,
			t.sComment,
			t.bVisible,
			t.bEnd,
			t.id
        FROM Anp_Anime t
			
    	'''
    
class List(Default, BaseListWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'sUrl', 'caption': 'Ссылка', 'isVisible': False, 'isReference': False, 'order':10, 'attrType':'Text'},
		{'name': 'nScore', 'caption': 'Оценка', 'isVisible': True, 'isReference': False, 'order':20, 'attrType':'Integer'},
		{'name': 'sCommentSite', 'caption': 'Описание', 'isVisible': True, 'isReference': False, 'order':30, 'attrType':'Text'},
		{'name': 'sComment', 'caption': 'Мой коментарий', 'isVisible': True, 'isReference': False, 'order':40, 'attrType':'Text'},
		{'name': 'bVisible', 'caption': 'Просмотренно', 'isVisible': True, 'isReference': False, 'order':50, 'attrType':'Integer'},
		{'name': 'bEnd', 'caption': 'Закончилось', 'isVisible': True, 'isReference': False, 'order':60, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = [
        {'name': 'sCaption', 'caption': 'Наименование', 'isVisible': True, 'isReference': False, 'order':0, 'attrType':'Text'},
		{'name': 'sUrl', 'caption': 'Ссылка', 'isVisible': False, 'isReference': False, 'order':10, 'attrType':'Text'},
		{'name': 'nScore', 'caption': 'Оценка', 'isVisible': True, 'isReference': False, 'order':20, 'attrType':'Integer'},
		{'name': 'sCommentSite', 'caption': 'Описание', 'isVisible': True, 'isReference': False, 'order':30, 'attrType':'Text'},
		{'name': 'sComment', 'caption': 'Мой коментарий', 'isVisible': True, 'isReference': False, 'order':40, 'attrType':'Text'},
		{'name': 'bVisible', 'caption': 'Просмотренно', 'isVisible': True, 'isReference': False, 'order':50, 'attrType':'Integer'},
		{'name': 'bEnd', 'caption': 'Закончилось', 'isVisible': True, 'isReference': False, 'order':60, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    
    def onRefresh(self, param):
        return Anp_AnimeLogV().load(param['id'])
