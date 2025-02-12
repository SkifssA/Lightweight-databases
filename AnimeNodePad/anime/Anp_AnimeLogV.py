from liteBD import *
class Rop:
    tablName = 'Anp_Anime'
    def __init__(self, sCaption=None, sUrl=None, nScore=None, sCommentSite=None, sComment=None, bVisible=None, bEnd=None, idAnime=None, id=None):
        self.sCaption=sCaption
        self.sUrl=sUrl
        self.nScore=nScore
        self.sCommentSite=sCommentSite
        self.sComment=sComment
        self.bVisible=bVisible
        self.bEnd=bEnd
        self.idAnime=idAnime
        self.id=id


class Anp_AnimeLogV:
    def insert():
        return Rop()
    
    def load(self, id):
        w = getReguest(f'''SELECT
    t.sCaption,
t.sUrl,
t.nScore,
t.sCommentSite,
t.sComment,
t.bVisible,
t.bEnd,
t.idAnime,
t.id
    FROM Anp_Anime t
    WHERE t.id = {id}''')
        return Rop(**{w[0][i]: w[1][i] for i in range(len(w[0]))})

    def setsCaption(rop:Rop, value):
        rop.sCaption = value

    def setsUrl(rop:Rop, value):
        rop.sUrl = value

    def setnScore(rop:Rop, value):
        rop.nScore = value

    def setsCommentSite(rop:Rop, value):
        rop.sCommentSite = value

    def setsComment(rop:Rop, value):
        rop.sComment = value

    def setbVisible(rop:Rop, value):
        rop.bVisible = value

    def setbEnd(rop:Rop, value):
        rop.bEnd = value

    def setidAnime(rop:Rop, value):
        rop.idAnime = value

    def setid(rop:Rop, value):
        rop.id = value


