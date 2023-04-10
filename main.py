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

    # onto_ex = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1")

    onto_worker = OntoWorker()
    onto_ex = onto_worker.get_onto_ex()
    onto_lang = onto_worker.get_onto_lang()

    # print('testik:', onto_ex.Int.instances()[0].get_properties())
    # # print('testik:', has_ExText[onto_ex.Int.instances()[0]])
    # prop1 = list(onto_ex.Int.instances()[0].get_properties())
    #
    # print('prop1:', prop1)
    # for prop in onto_ex.Int.instances()[0].get_properties():
    #     for value in prop[onto_ex.Int.instances()[0]]:
    #         print(".%s == %s" % (prop.python_name, value))
    # print('\n')
    # # if (prop1[0][onto_ex.Int.instances()[0]]):
    # #     print('yep')
    #
    # for val in prop1:
    #     print(type(val), val)
    # print('\n')
    #
    # # print(onto_ex.properties())
    # for entry in onto_ex.properties():
    #     print(entry)

    # print(list(onto_ex.properties()))
    # if onto_ex.ExText in list(onto_ex.properties()):
    #     print('YEEYEYEYEY')

    # testik = onto_ex.Int.instances()[0]
    # if onto_ex.has_ExText[testik]:
    #     print(onto_ex.ExText[testik])
    #     print('EPEPPEEPEPEPEPEPp')
    # print(onto_ex.Ontology_Root)

    # print("MEGA TEST", testik.ExText)
    # print(onto_ex.search_one(iri='http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1#Ontology_Root'))

    # if (prop1[0] == True):
    #     print('yep')

    # for i in onto_ex.Int.instances():
    # print(i)

    # print(type(onto_ex.Ontology_Root))
    # print(str(list(onto_ex.Ontology_Root.descendants())))

    # for r in onto_ex.Ontology_Root.descendants():
    #     print(r)
    # gen = onto_ex.classes()
    # print(gen.__next__())

    gui_worker = GuiWorker(onto_ex, onto_lang)

    # test_graph = {'First': {'Datatypes': {'Numeric types': {'Int': {'Example1': {}}, 'Float': {'Example2': {}}}}}}

    app = QApplication(sys.argv)
    window = MainWindow()
    window.Tree_Examples.itemClicked.connect(gui_worker.print_example)
    window.Tree_Language.itemClicked.connect(gui_worker.print_language)
    # window.Tree_Language.itemClicked.connect(gui_worker.print_language)
    # print('ex text:', window.Example_Text)
    gui_worker.Example_Text = window.Example_Text
    gui_worker.Lang_Text = window.Language_Text

    # p = window.findChild(QTreeWidget, 'Tree_Examples')
    gui_worker.print_tree_from_graph(window.Tree_Examples, gui_worker.graph_ex)  # update left ontology
    gui_worker.print_tree_from_graph(window.Tree_Language, gui_worker.graph_lang)  # update left ontology

    # print(p.findChild(QTreeWidgetItem))
    # print(t.children())
    # print(t.text())

    # t: QTreeWidget = window.findChild(QTreeWidget)
    # t.clear()
    # build_gui_from_graph(test_graph, t)
    # print()

    # gui_graph = window.findChild(QToolButton, "B_edit")
    # print(gui_graph)
    # t = gui_graph.parent()
    # print(t.objectName())
    # print(t.children())
    # print(t.findChild(QTreeWidget))
    # for ch in gui_graph.children():
    #     print(ch.objectName())

    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
