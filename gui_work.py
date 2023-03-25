from owlready2 import *


class GuiWorker:
    """
    Does GUI updates.
    """

    def __init__(self, onto: owlready2.namespace.Ontology):
        self.onto = onto
        self.build_graph()
        pass

    def build_graph(self):
        parent = self.onto.Ontology_Root

        graph = self.recursive_obxod(parent)
        print(graph)

    def recursive_obxod(self, node: owlready2.entity.ThingClass):
        d = {str(node): {}}
        if node.subclasses():
            for ch in node.subclasses():
                res = self.recursive_obxod(ch)
                if str(node) in d:
                    d[str(node)].update(res)
                else:
                    d[str(node)] = res
            return d
        else:
            return node

    # while ()
    #     print(list(onto.Ontology_Root.subclasses()))
    # for clss in onto.Ontology_Root.:
    #     print(clss)
    #     for parent in clss.
    #         pass
