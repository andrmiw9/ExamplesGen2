import string

from owlready2 import get_ontology


class OntoWorker:
    """
    Does all the job related to low-level work with Ontologies.
    """

    def __init__(self):
        self.onto = None

    def get_onto(self, path: string = "file://C:/Users/Sinitza/Documents/AУЧЕБА/ВКРБ/Ontologys/First.owl"):
        self.onto = get_ontology(path).load()
        return self.onto
