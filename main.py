# Andrey "andrmiw9" Markin 2023

# pyrcc5 IconEdit.qrc -o IconEdit.py

from owlready2 import *
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

from ontologies_work import OntoWorker
from main_window_handler import MainWindow
from gui_work import GuiWorker


# def recursive_obxod(self, node: owlready2.entity.ThingClass):
#     d = {str(node): {}}
#     if node.subclasses():
#         for ch in node.subclasses():
#             res = self.recursive_obxod(ch)
#             if str(node) in d:
#                 d[str(node)].update(res)
#             else:
#                 d[str(node)] = res
#         return d
#     else:
#         return node
def recursive_build(tree_parent, local_graph):
    # if startNode.:
    #     for sbcls in startNode.subclasses():
    #         t = QTreeWidgetItem(startNode)
    #         t.setText(0, sbcls.object_name())
    for key in local_graph.keys():
        t = QTreeWidgetItem(tree_parent)
        t.setText(0, key)
        recursive_build(key, local_graph[key].keys())
    pass


def build_gui_from_graph(graph, node: QTreeWidget) -> None:
    print('Graph to build:', graph)
    n = QTreeWidgetItem(node)
    n.setText(0, 'Cities')
    itemsmth = QTreeWidgetItem(n)
    itemsmth.setText(0, 'Oslo')
    itemsmth.setText(1, 'Yes')

    node.insertTopLevelItems(None, graph)
    # for key in graph.keys():
    #     t = QTreeWidgetItem(node)
    #     t.setText(0, key)
    #     for k in graph[key].keys():
    #           r = QTreeWidgetItem(key)
    #           r.setText(0, k)
    #           ...
    # recursive_build(graph['First'])

    pass


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

    # onto_worker = OntoWorker()
    # onto = onto_worker.get_onto()

    # print(type(onto.Ontology_Root))
    # print(str(list(onto.Ontology_Root.descendants())))

    # for r in onto.Ontology_Root.descendants():
    #     print(r)
    # gen = onto.classes()
    # print(gen.__next__())

    # gui_worker = GuiWorker(onto)
    # gui_worker.graph
    test_graph = {'First': {'Datatypes': {'Numeric types': {'Int': {'Example1': {}}, 'Float': {'Example2': {}}}}}}

    app = QApplication(sys.argv)
    window = MainWindow()

    # gui_worker.update_Left()

    t: QTreeWidget = window.findChild(QTreeWidget)
    t.clear()
    build_gui_from_graph(test_graph, t)
    print()

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
