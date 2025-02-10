from liteBD import *
class Rop:
    tablName = 'testClass2'
    def __init__(self, sCaption=None, nRow=None, idTestClass=None, id=None):
        self.sCaption=sCaption
        self.nRow=nRow
        self.idTestClass=idTestClass
        self.id=id


class testClass2LogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''SELECT
    t.sCaption,
t.nRow,
t.idTestClass,
t.id
    FROM testClass2 t
    WHERE t.id = {id}''')
        return Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})

    def setsCaption(rop:Rop, value):
        rop.sCaption = value

    def setnRow(rop:Rop, value):
        rop.nRow = value

    def setidTestClass(rop:Rop, value):
        rop.idTestClass = value

    def setid(rop:Rop, value):
        rop.id = value


