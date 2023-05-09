# Andrey "andrmiw9" Markin 2023
from PyQt5.QtGui import QKeySequence
# pyrcc5 IconEdit.qrc -o IconEdit.py

from owlready2 import *
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import json

from ontologies_work import OntoWorker
from main_window_handler import MainWindow
from parser_basics import Parser

CONST_EXAMPLES: bool = False
CONST_LANGUAGE: bool = False
gui: MainWindow = None

onto_worker = OntoWorker()


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

    # test_graph = {'First': {'Datatypes': {'Numeric types': {'Int': {'Example1': {}}, 'Float': {'Example2': {}}}}}}

    app = QApplication(sys.argv)
    global gui
    gui = MainWindow()

    gui.actionOpen.triggered.connect(left_loader)  # Открыть примеры
    gui.actionOpen_Right.triggered.connect(right_loader)  # Открыть спецификацию
    gui.action_SaveEx.setShortcut(QKeySequence("Ctrl+S"))
    gui.action_SaveEx.triggered.connect(save_onto_ex)
    gui.action_SaveAs.triggered.connect(save_onto_ex_as)
    gui.actionExtendEx.triggered.connect(extend_ontology_json)  # расширить онтологию примеров JSON'ом
    # or:
    # self.MyInput.textChanged[str].connect(self.doSomething)
    sys.exit(app.exec_())

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


def save_onto_ex():
    print('save')
    if CONST_EXAMPLES:
        onto_worker.save_onto_ex()
    else:
        print('Сначала загрузите онтологию примеров, чтобы сохранять в неё же')


def save_onto_ex_as():
    print('save as')
    if CONST_EXAMPLES:
        filename, _ = QFileDialog.getSaveFileName(gui, "Save File", ".", "Ontology (*.owl);;All Files (*)")
        if filename:
            onto_worker.save_onto_ex(custom_file=filename)
            # with open(filename, 'w') as file:
            #     file.write("Welcome to GeeksCoders.com")
    else:
        print('Сначала загрузите онтологию примеров')

        # name = QFileDialog.getSaveFileName(self, 'Save File')
        # file = open(name, 'w')
        # text = self.textEdit.toPlainText()
        # file.write(text)
        # file.close()


class MyDialog(QFileDialog):
    def __init__(self, parent):
        super(MyDialog, self).__init__(parent)
        self.setFileMode(QFileDialog.ExistingFile)
        self.setNameFilter("Ontology (*.owl)")
        self.setViewMode(QFileDialog.List)


def extend_ontology_json():
    if not CONST_EXAMPLES:
        print('Ошибка: сначала загрузите примеры!')
        return

    print('extender')
    dialog = MyDialog(gui)
    dialog.setNameFilter('JSON (*.json)')  # modify filter for JSON

    if dialog.exec_():
        filename = dialog.selectedFiles()
        print('Filenames:', filename)
        if filename[0]:
            with open(filename[0]) as json_file:
                data = json.load(json_file)
                print('Data from file:', data)
                onto_worker.update_examples_from_graph(data)

                gui.update_ex_graph()

                gui.print_tree_from_graph(gui.Tree_Examples, gui.graph_ex)  # update left
            # gui.set_ex_onto(onto_worker.get_onto_ex(filename[0]))
            # gui.Tree_Examples.itemClicked.connect(gui.print_example)
            # gui.Example_Text = gui.Example_Text
            #
            # gui.print_tree_from_graph(gui.Tree_Examples, gui.graph_ex)  # update left ontology
    pass


def left_loader():
    global CONST_EXAMPLES
    CONST_EXAMPLES = False
    # print('left_loader')-
    dialog = MyDialog(gui)

    if dialog.exec_():
        filename = dialog.selectedFiles()
        print('Filenames:', filename)
        if filename[0]:
            # getting ontology from file and setting in gui worker
            gui.set_ex_onto(onto_worker.get_onto_ex(filename[0]))
            gui.Tree_Examples.itemClicked.connect(gui.print_example)
            gui.Example_Text.textChanged.connect(gui.change_text_example)

            gui.print_tree_from_graph(gui.Tree_Examples, gui.graph_ex)  # update left ontology

            CONST_EXAMPLES = True


def right_loader():
    global CONST_LANGUAGE
    CONST_LANGUAGE = False
    # print('right_loader')
    dialog = MyDialog(gui)

    if dialog.exec_():
        filename = dialog.selectedFiles()
        print('Filenames:', filename)
        if filename[0]:
            gui.set_lang_onto(onto_worker.get_onto_lang(filename[0]))
            gui.Tree_Language.itemClicked.connect(gui.print_language)

            gui.print_tree_from_graph(gui.Tree_Language, gui.graph_lang)  # update left ontology
            CONST_LANGUAGE = True
    pass


if __name__ == '__main__':
    application()
