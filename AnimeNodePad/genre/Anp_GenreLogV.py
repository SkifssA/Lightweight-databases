from liteBD import *
class Rop:
    tablName = 'Anp_Genre'
    def __init__(self, sCaption=None, id=None):
        self.sCaption=sCaption
        self.id=id


class Anp_GenreLogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''SELECT
    t.sCaption,
t.id
    FROM Anp_Genre t
    WHERE t.id = {id}''')
        return Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})

    def setsCaption(rop:Rop, value):
        rop.sCaption = value

    def setid(rop:Rop, value):
        rop.id = value


