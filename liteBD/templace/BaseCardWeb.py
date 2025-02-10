from .BaseDefaultWeb import *

typeDash = {
    'text':'text',
    'integer': 'number'
}
globalData = None

class BaseCardWeb(BaseDefaultWeb):
    def _getMainLayout(self, param):
        global globalData
        globalData = self.onRefresh(param)
        attrData = globalData.__dict__
        nested_list = (self.getLableAndInput(attr, attrData) for attr in sorted(self.__class__.AttrSettings, key=lambda x: x['order']))
        return [
            *(item for sublist in nested_list for item in sublist)
        ]

    def getLableAndInput(self, attr, attrData):
        return (html.Label(attr['caption'])
                ,dcc.Input(id=attr['name'], type=typeDash[attr['attrType'].lower()], value=attrData[attr['name']])
                ,html.Br())
    
    @Oper('Сохранить')
    def safeRop(n):
        global globalData
        setRop(globalData)

    def register_input_callbacks(self):
            """
            Регистрирует callback'и для всех полей ввода, определенных в AttrSettings.
            """
            global globalData

            @SETTING.selfApp.callback(  # Фиктивный output для триггера
                [Input(attr['name'], 'value') for attr in self.__class__.AttrSettings],  # Отслеживаем все поля ввода
                prevent_initial_call=True
            )
            def update_global_data(*input_values):
                if globalData is not None:
                    # Обновляем значения в globalData
                    for idx, attr in enumerate(self.__class__.AttrSettings):
                        setattr(globalData, attr['name'], input_values[idx])
                    print("Обновленные данные:", globalData.__dict__)
