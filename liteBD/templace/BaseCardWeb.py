from .BaseDefaultWeb import *

typeDash = {
    'text':'text',
    'integer': 'number'
}

class BaseCardWeb(BaseDefaultWeb):
    def getLayout(self, param):
        self.idObject = param['id']
        data = self.onRefresh()
        print(data)
        try:
            data[1][0]
        except:
            data.append([None]*len(data[0]))
        attrData = {data[0][i]:data[1][i] for i in range(len(data[0]))}
        nested_list = (self.getLableAndInput(attr, attrData) for attr in sorted(self.__class__.AttrSettings, key=lambda x: x['order']))
        return html.Div([
            *self._getStandartLayout(),
            *(item for sublist in nested_list for item in sublist)
        ])
    
    def getLableAndInput(self, attr, attrData):
        return (html.Label(attr['caption']), dcc.Input(id=attr['name'], type=typeDash[attr['attrType'].lower()], value=attrData[attr['name']]), html.Br())
    
    def whereSQL(self):
        return f"""WHERE t.id = {self.idObject}"""