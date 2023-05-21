import requests
from bs4 import BeautifulSoup as bs
import re
import owlready2
from owlready2 import *
import types


class ParserLang:
    def __init__(self):
        path: str = "file://Ontologies/Language.owl"
        folder = path[:path.rfind('/') + 1]
        # print(folder)
        onto_path.append(folder)

        self.onto_lang = get_ontology(path).load()

        URL_TEMPLATE = "https://docs.python.org/3/library/index.html#library-index"
        r = requests.get(URL_TEMPLATE)
        r.encoding = 'utf-8'
        soup = bs(r.text, "html.parser")
        # graph = {}
        result = soup.find(name='div', attrs={'class': "toctree-wrapper compound"})
        start_tag = result.find('a', string='Text Processing Services').parent

        lis = [start_tag, ]
        t = start_tag.find_next_siblings('li')
        lis.extend(t)

        for l in lis:
            parent: str = 'Standart_Library'
            key1 = l.text.split('\n')[0]
            key1 = key_validator(key1)
            with self.onto_lang:
                k_cls = types.new_class(key1, (self.onto_lang[parent],))
                lcl_ul = l.find('ul')
                if lcl_ul:
                    for li in lcl_ul.find_all('li'):
                        t = li.text.split('—')[0][:-1]
                        t = key_validator(t)
                        # print(t)
                        tagA = li.find('a')
                        # print(tagA['href'])
                        URL_TEMPLATE2 = "https://docs.python.org/3/library/" + tagA['href']
                        r2 = requests.get(URL_TEMPLATE2)
                        r2.encoding = 'utf-8'
                        soup2 = bs(r2.text, "html.parser")
                        lcl_result = soup2.find('hr', attrs={'class': "docutils"})
                        if lcl_result:
                            lcl_result = lcl_result.findNextSibling('p')
                        print(t, lcl_result, '\n')
                        if lcl_result is None:  # fix
                            lcl_result = ''

                        k_clss2 = types.new_class(t, (self.onto_lang[key1],))

                        instance = self.onto_lang[t]()
                        # print(parsr.graph[key_top][key_2][key_3])
                        instance.SpecText = str(lcl_result)
                        instance.has_SpecText = True

        # print('\n\n\n', graph)
        # for k in graph.keys():
        #     print(k)
        #     for v in graph[k]:
        #         print('\t', v)
        #
        # self.graph = graph

        # for k in graph.keys():
        #     print(k)

        self.onto_lang.save(file='Ontologies/Result1.owl')


def key_validator(text: str) -> str:
    text = text.replace(' ', '_')  # fix for ontology
    return re.sub(r'[^a-zA-Z0-9_]', '', text)


if __name__ == '__main__':
    p = ParserLang()
