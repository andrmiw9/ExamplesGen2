import string

from owlready2 import get_ontology


class OntoWorker:
    """
    Does all the job related to low-level work with Ontologies.
    """

    def __init__(self):
        self.onto = None

    def get_onto(self, path: string = "file://Ontologies/First.owl"):
        self.onto = get_ontology(path).load()
        # self.onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1")
        # print(type(self.onto))
        return self.onto
