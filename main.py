# Andrey "andrmiw9" Markin 2023

# pyrcc5 IconEdit.qrc -o IconEdit.py

from owlready2 import *
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import IconEdit
from ontologies_work import OntoWorker
from main_window_handler import MainWindow


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

    onto_wrkr = OntoWorker()
    onto = onto_wrkr.get_onto()
    print(list(onto.classes()))

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
