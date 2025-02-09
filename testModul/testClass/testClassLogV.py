
class Rop:
    def __init__(self, sCaption=None, nRow=None, id=None):
        self.sCaption=sCaption
        self.nRow=nRow
        self.id=id


class testClassLogV:
    def insert():
        return testClassRop()
    
    def load(id):
        w = getReguest()
        return testClass2Rop(**w.__dict__)

    def setsCaption(rop:testClassRop, value):
        rop.sCaption = value

    def setnRow(rop:testClassRop, value):
        rop.nRow = value

    def setid(rop:testClassRop, value):
        rop.id = value


