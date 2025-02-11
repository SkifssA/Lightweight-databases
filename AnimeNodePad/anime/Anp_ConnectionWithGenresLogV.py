from liteBD import *
class Rop:
    tablName = 'Anp_ConnectionWithGenres'
    def __init__(self, idAnime=None, idGenre=None, id=None):
        self.idAnime=idAnime
        self.idGenre=idGenre
        self.id=id


class Anp_ConnectionWithGenresLogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''SELECT
    t.idAnime,
t.idGenre,
t.id
    FROM Anp_ConnectionWithGenres t
    WHERE t.id = {id}''')
        return Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})

    def setidAnime(rop:Rop, value):
        rop.idAnime = value

    def setidGenre(rop:Rop, value):
        rop.idGenre = value

    def setid(rop:Rop, value):
        rop.id = value


