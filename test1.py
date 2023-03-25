# print("Hello there!")
# text = ""
# pat = "@"
# with open("Classes.py", 'r+') as f:
#     for line in f:
#         # line = line.rstrip()
#         text += line
#
#     print(text)
#     print(type(text))
#
#     text = text.replace('@', "OBLADI-OBLADA!")
#     # print(text)
#     # print
#     print(5)
#
#     print(text)

# pyrcc5 IconEdit.qrc -o IconEdit.py


from owlready2 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from TestQt import Ui_MainWindow as QTMainW
import sys
import IconEdit


def application():
    # app = QApplication(sys.argv)
    # mwind = QMainWindow()
    #
    # mwind.setWindowTitle("Test1")
    # mwind.setGeometry(300, 255, 122, 521)
    #
    # mwind.show()
    # sys.exit(app.exec_())

    # onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1")
    onto = get_ontology(r"file://C:/Users/Sinitza/Documents/AУЧЕБА/ВКРБ/Ontologys/First.owl").load()
    print(list(onto.classes()))

    app = QApplication(sys.argv)
    window = TestQtWindow()
    sys.exit(app.exec_())


class TestQtWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = QTMainW()
        uic.loadUi('TestQt.ui', self)
        # sf.myWidget.setStyleSheet(“image: url(picture.jpg)”)
        # self.ui.setupUi(self)
        # print(s)
        # s.setupUi(self)
        editb = self.findChild(QToolButton, "B_edit")
        print(editb)
        editb.setStyleSheet('icon: url(edit_ico.ico)')
        self.show()


if __name__ == '__main__':
    application()
    print("Something New!")
    print('cadabra')
    print('tatatabra')
