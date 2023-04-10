import string

from owlready2 import get_ontology


class OntoWorker:
    """
    Does all the job related to low-level work with Ontologies.
    """

    def __init__(self):
        self.onto_ex = None
        self.onto_lang = None

    def get_onto_ex(self, path: string = "file://Ontologies/First.owl"):
        self.onto_ex = get_ontology(path).load()
        # self.onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1")
        # print(type(self.onto))
        return self.onto_ex

    def get_onto_lang(self, path: string = "file://Ontologies/Language.owl"):
        self.onto_lang = get_ontology(path).load()
        # self.onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonLanguage")
        return self.onto_lang
