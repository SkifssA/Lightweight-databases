from liteBD import *

generatorClass('testModul/testClass/testClass.xml')
generatorClass('testModul/testClass2/testClass2.xml')

from testModul.testClass2.testClass2GuiA import *



app = SETTING.selfApp


# Layout приложения
app.layout = testClass2GuiA.List().getLayout()


# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)