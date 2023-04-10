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

    def __init__(self, onto_left: owlready2.namespace.Ontology, onto_right: owlready2.namespace.Ontology):
        self.graph_ex = None
        self.graph_lang = None
        self.onto_examples = onto_left
        self.onto_lang = onto_right
        self.Example_Text = None
        self.Lang_Text = None

        self.graph_ex = self.build_graph_from_onto(self.onto_examples.Ontology_Root)
        self.graph_lang = self.build_graph_from_onto(self.onto_lang.Ontology_Root)

    def build_graph_from_onto(self, parent):
        return self.build_graph(parent)
        # print(self.graph_ex)

    def build_graph(self, node: owlready2.entity.ThingClass):
        node_str = str(node).split('.')[1]
        d = {node_str: {}}
        if node.subclasses():
            for ch in node.subclasses():
                res = self.build_graph(ch)
                if node_str in d:
                    d[node_str].update(res)
                else:
                    d[node_str] = res
            return d
        else:
            return node

    def print_tree_from_graph(self, node: QTreeWidget, graph: dict = None) -> None:
        if not graph:
            return
        print('Graph to build:', graph)
        node.clear()
        self.print_tree(node, graph)

    def print_tree(self, tree_parent, local_graph):
        for key in local_graph.keys():
            t = QTreeWidgetItem(tree_parent)
            t.setText(0, key)
            self.print_tree(t, local_graph[key])

    def print_example(self, currentItem):
        # print('TEST11TEST11')
        # t = str(currentItem.text(0)).split('.')[1]
        t = currentItem.text(0)
        print(t)
        # print('relevant:', self.onto.currentItem.text(0))
        # print(self.onto.search(iri=(f"{0}", t)))
        self.Example_Text.setPlainText('')
        onto_node = self.onto_examples.search_one(iri=f"*{t}")
        if onto_node:
            if onto_node.instances():
                instance = onto_node.instances()[0]
                # print(instance.get_properties())
                # testik = self.onto.onto_node.instances()[0]
                if instance.has_ExText:
                    r = self.onto_examples.ExText[instance][0]
                    self.Example_Text.setPlainText(r)
                    # print('EPEPPEEPEPEPEPEPp')
                # self.Example_Text = 'fwafwfawfawf'
                # print(self.Example_Text)
            else:
                print("No Instances!")

    def print_language(self):
        print('yep')
        pass
