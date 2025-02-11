from liteBD import *
from .Anp_ConnectionWithGenresLogV import Anp_ConnectionWithGenresLogV

class Default(BaseDefaultWeb):
    AttrSettings = [
        {'name': 'idAnime', 'caption': 'Аниме', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'idGenre', 'caption': 'Жанры', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    def requestSQL(self)->str:
        return '''
     SELECT 
			t.idAnime,
			t1.sHeadLine as idAnimeHL,
			t.idGenre,
			t2.sHeadLine as idGenreHL,
			t.id
        FROM Anp_ConnectionWithGenres t
			LEFT JOIN Anp_Anime t1 ON t1.id = t.idAnime
			LEFT JOIN Anp_Genre t2 ON t2.id = t.idGenre
    	'''
    
class List(Default, BaseListWeb):
    AttrSettings = [
        {'name': 'idAnime', 'caption': 'Аниме', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'idGenre', 'caption': 'Жанры', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    pass
class Card(Default, BaseCardWeb):
    AttrSettings = [
        {'name': 'idAnime', 'caption': 'Аниме', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'idGenre', 'caption': 'Жанры', 'isVisible': True, 'isReference': True, 'order':20, 'attrType':'Integer'},
		{'name': 'id', 'caption': 'id', 'isVisible': False, 'isReference': False, 'order':-1, 'attrType':'Integer'}
    ]
    
    
    def onRefresh(self, param):
        return Anp_ConnectionWithGenresLogV().load(param['id'])
