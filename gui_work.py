import owlready2
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

    def __init__(self):
        self.graph_ex: dict = None
        self.graph_lang: dict = None
        self.onto_examples: owlready2.namespace.Ontology = None
        self.onto_lang: owlready2.namespace.Ontology = None
        self.Example_Text: str = None
        self.Lang_Text: str = None
        # onto_right: owlready2.namespace.Ontology

        # self.graph_ex = self.build_graph_from_onto(self.onto_examples.Ontology_Root)
        # self.graph_lang = self.build_graph_from_onto(self.onto_lang.Ontology_Root)

    def set_ex_onto(self, onto_ex: owlready2.namespace.Ontology):
        self.onto_examples = onto_ex
        self.graph_ex = self.build_graph_from_onto(self.onto_examples.Ontology_Root)
        # print(self.graph_ex)

    def set_lang_onto(self, onto_lang: owlready2.namespace.Ontology):
        self.onto_lang = onto_lang
        self.graph_lang = self.build_graph_from_onto(self.onto_lang.Ontology_Root)
        # print(self.graph_lang)

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

    def print_language(self, currentItem):
        t = currentItem.text(0)
        print(t)
        # print('relevant:', self.onto.currentItem.text(0))
        # print(self.onto.search(iri=(f"{0}", t)))
        self.Lang_Text.setPlainText('')
        onto_node = self.onto_lang.search_one(iri=f"*{t}")
        if onto_node:
            if onto_node.instances():
                instance = onto_node.instances()[0]
                # print(instance.get_properties())
                # testik = self.onto.onto_node.instances()[0]
                if instance.has_SpecText:
                    r = self.onto_lang.SpecText[instance][0]
                    self.Lang_Text.setPlainText(r)
                    # print('EPEPPEEPEPEPEPEPp')
                # self.Example_Text = 'fwafwfawfawf'
                # print(self.Example_Text)
            else:
                print("No Instances!")
        pass
