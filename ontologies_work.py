import string

from owlready2 import *
from parser_basics import Parser
import types


def test(self):
    pass


class OntoWorker:
    """
    Does all the job related to low-level work with Ontologies.
    """

    def __init__(self):
        self.onto_ex = None
        self.onto_lang = None

    def update_ontoex_from_parse(self):  # extend ontology from parse result
        parsr = Parser()

        # parsr.graph['Python Classes and Objects']
        print(parsr.graph)
        with self.onto_ex:
            for key_top in parsr.graph.keys():  # ex: Python datatypes or Python Operators
                print(key_top)
                ktop_cls = types.new_class(key_top, (self.onto_ex['Python_Basics'],))
                for key_2 in parsr.graph[key_top].keys():  # ex: Python int or Next level
                    if key_2 == 'Next_Level':
                        pass
                        for key_3 in parsr.graph[key_top][key_2].keys():  # ex: Python Arithmetic Operators
                            print('\t', key_3)
                            k3_cls = types.new_class(key_3, (self.onto_ex[key_top],))
                            # print(1)
                            for key_4 in parsr.graph[key_top][key_2][key_3].keys():  # ex: Python Addition
                                k4_cls = types.new_class(key_4, (self.onto_ex[key_3],))
                                print('\t\t', key_4)
                    else:
                        if key_2 == key_top:
                            key_2 += '*'
                        k2_cls = types.new_class(key_2, (self.onto_ex[key_top],))
                        print('\t', key_2)

        print('\n\n')
        pass

    def get_onto_ex(self, path: string = "file://Ontologies/First.owl"):
        # print(path)
        self.onto_ex = get_ontology(path).load()
        # self.onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonExamples1")
        # print(type(self.onto))
        self.update_ontoex_from_parse()
        return self.onto_ex

    def get_onto_lang(self, path: string = "file://Ontologies/Language.owl"):
        self.onto_lang = get_ontology(path).load()
        # self.onto = get_ontology("http://www.semanticweb.org/sinitza/ontologies/2023/1/PythonLanguage")
        return self.onto_lang
