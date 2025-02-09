from .BaseDefaultWeb import *

typeDash = {
    'text':'text',
    'integer': 'number'
}

class BaseCardWeb(BaseDefaultWeb):
    def _getMainLayout(self, param):
        self.idObject = param['id']
        data = self.onRefresh()
        attrData = data.__dict__
        nested_list = (self.getLableAndInput(attr, attrData) for attr in sorted(self.__class__.AttrSettings, key=lambda x: x['order']))
        return [
            *(item for sublist in nested_list for item in sublist)
        ]

    def getLableAndInput(self, attr, attrData):
        return (html.Label(attr['caption'])
                ,dcc.Input(id=attr['name'], type=typeDash[attr['attrType'].lower()], value=attrData[attr['name']])
                ,html.Br())