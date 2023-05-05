from parser_basics import Parser


class ParseWorker:
    def __init__(self):
        self.parser = Parser()
        pass

    def update_ontology(self):
        pass

    def test(self):
        for key_top in self.graph.keys():  # ex: Python datatypes or Python Operators
            print(key_top)
            for key_2 in self.graph[key_top].keys():  # ex: Python int or Next level

                if key_2 == 'Next_Level':
                    # print('\t')
                    for key_3 in self.graph[key_top][key_2].keys():  # ex: Python Arithmetic Operators
                        print('\t', key_3)
                        # print(1)
                        for key_4 in self.graph[key_top][key_2][key_3].keys():  # ex: Python Addition
                            print('\t\t', key_4)
                else:
                    print('\t', key_2)
