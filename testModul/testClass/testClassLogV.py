from liteBD import *
class Rop:
    tablName = 'testClass'
    def __init__(self, sCaption=None, nRow=None, id=None):
        self.sCaption=sCaption
        self.nRow=nRow
        self.id=id


class testClassLogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''SELECT
    t.sCaption,
t.nRow,
t.id
    FROM testClass t
    WHERE t.id = {id}''')
        return Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})

    def setsCaption(rop:Rop, value):
        rop.sCaption = value

    def setnRow(rop:Rop, value):
        rop.nRow = value

    def setid(rop:Rop, value):
        rop.id = value


