# Andrey "andrmiw9" Markin 2023

# pyrcc5 IconEdit.qrc -o IconEdit.py

from owlready2 import *
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

from ontologies_work import OntoWorker
from main_window_handler import MainWindow
from gui_work import GuiWorker


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

    onto_worker = OntoWorker()
    onto = onto_worker.get_onto()

    gui_worker = GuiWorker(onto)

    # print(type(onto.Ontology_Root))
    # print(str(list(onto.Ontology_Root.descendants())))
    # for r in onto.Ontology_Root.descendants():
    #     print(r)
    # gen = onto.classes()
    # print(gen.__next__())

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
