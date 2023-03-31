from owlready2 import *
from PyQt5.QtWidgets import *


class GuiWorker:
    """
    Does GUI updates. Builds graph and displays it.
    """

    #
    # TODO:
    #  1) refactor methods using decorators
    #  2)
    #
    #

    def __init__(self, onto: owlready2.namespace.Ontology):
        self.graph = None
        self.onto = onto
        self.build_graph_from_gui()

    def build_graph_from_gui(self):
        parent = self.onto.Ontology_Root

        self.graph = self.build_graph(parent)
        print(self.graph)

    def build_graph(self, node: owlready2.entity.ThingClass):
        d = {str(node): {}}
        if node.subclasses():
            for ch in node.subclasses():
                res = self.build_graph(ch)
                if str(node) in d:
                    d[str(node)].update(res)
                else:
                    d[str(node)] = res
            return d
        else:
            return node

    def print_tree_from_graph(self, node: QTreeWidget, graph: dict = None) -> None:
        if not graph:
            graph = self.graph
        print('Graph to build:', graph)
        node.clear()
        self.print_tree(node, self.graph)

    def print_tree(self, tree_parent, local_graph):
        for key in local_graph.keys():
            t = QTreeWidgetItem(tree_parent)
            t.setText(0, key)
            self.print_tree(t, local_graph[key])
