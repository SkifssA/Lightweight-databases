from liteBD.logic.requestBD import getReguest

class testClass2Rop:
    def __init__(self, sCaption=None, nRow=None, idTestClass=None, id=None):
        self.sCaption=sCaption
        self.nRow=nRow
        self.idTestClass=idTestClass
        self.id=id


class testClass2LogV:
    def insert(self):
        return testClass2Rop()

    def setsCaption(self, rop:testClass2Rop, value):
        rop.sCaption = value

    def setnRow(self, rop:testClass2Rop, value):
        rop.nRow = value

    def setidTestClass(self, rop:testClass2Rop, value):
        rop.idTestClass = value

    def setid(self, rop:testClass2Rop, value):
        rop.id = value

    def load(self, id):
        w = getReguest(f"""
        SELECT 
			t.sCaption,
			t.nRow,
			t.idTestClass,
			t.id
        FROM testClass2 t""")
        return testClass2Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})
