import requests
from bs4 import BeautifulSoup as bs
import re


# print('hello ')
def individuals_list_from_link(link) -> list:
    if link == '/python-print-123-n/':
        link = 'https://pythonexamples.org/python-print-123-n/'  # fix for 1 <a> которая неправильно написана на сайте
    responce = requests.get(link)
    # print(r.encoding)
    responce.encoding = 'utf-8'
    # print(r.encoding)
    # print(f'Status code: {responce.status_code}, link: {link}')
    # print(r.text)
    soup = bs(responce.text, "html.parser")
    # print(soup.original_encoding)

    res = soup.find_all('p', string='Python Program')
    l = []
    for entry in res:
        t = entry.next_sibling.next_sibling.text
        # print('Entry: ', t)
        l.append(t)
    return l


def lookforward2_h4(entry):
    res = entry.next_sibling.next_sibling
    if res and res.name == 'h4':
        return True
    res = entry.next_sibling.next_sibling.next_sibling.next_sibling
    if res and res.name == 'h4':
        return True


def add_to_graph(local_graph: dict, ul):  # t = entry or h4
    alist = ul.findChildren('a')
    for tagA in alist:
        # print(tagA['href'], tagA.text)
        # local_graph3[tagA.text] = tagA['href']

        example_list = individuals_list_from_link(tagA['href'])
        if example_list:
            local_graph[tagA.text] = example_list[0]
        else:
            local_graph[tagA.text] = tagA['href']
    pass


class Parser:
    def __init__(self):
        URL_TEMPLATE = "https://pythonexamples.org/python-basic-examples    /"
        r = requests.get(URL_TEMPLATE)
        # print(r.encoding)
        r.encoding = 'utf-8'
        # print(r.encoding)
        # print('Status code:', r.status_code)
        # print(r.text)
        soup = bs(r.text, "html.parser")
        # print(soup.original_encoding)
        # print(soup)

        self.result = soup.find_all('h3')
        self.graph = {}

        self.build_graph()

    def build_graph(self):
        print('Parsing in progress...\n')
        for entry in self.result:
            if entry.text == 'Summary':
                break

            # print(entry)
            local_graph1 = {}
            self.graph[entry.text] = local_graph1

            if lookforward2_h4(entry):  # если среди 2 тегов снизу есть h4
                local_graph2 = {}
                local_graph1['Next_Level'] = local_graph2
                # print(self.graph)
                # print('YEEEEP')
                condition = True
                t = entry.findNextSibling('h4')
                while condition:  # следующий тег это h4
                    h4 = t
                    # print(h4)
                    local_graph3 = {}
                    local_graph2[h4.text] = local_graph3
                    # print(h4.next_sibling)
                    # print(h4.next_sibling.next_sibling)
                    # print(h4.next_sibling.next_sibling.next_sibling)
                    # print(h4.next_sibling.next_sibling.next_sibling.next_sibling)

                    rtest = h4.findNextSiblings(limit=3)
                    flag = False
                    for e in rtest:
                        # print(e.name)
                        if e.name == 'h3':  # если среди 3 ближайших соседей снизу есть h3, то не трогаем такой h4
                            flag = True
                            break
                    if flag:
                        # already added to big graph with lgraph2[] = {}
                        break

                    ul = h4.findNextSibling('ul')
                    add_to_graph(local_graph3, ul)

                    t = h4.findNextSibling('h4')
                    condition = ul.next_sibling.next_sibling.name == 'h4'  # следующий тег это h4

                    pass
                continue
            else:
                ul = entry.findNextSibling('ul')
                add_to_graph(local_graph1, ul)
                pass

        # print(self.graph)
        # print(self.graph['Python Operators'])
        #
        # print('\n')
        # print(self.graph)
        # print('\n')

        self.print_graph_keys()

    # class Example:
    #     def __init__(self, name: str, example_text: str = '', description: str = ''):
    #         self.name = name
    #         self.example_text = example_text
    #         self.description = description
    #         pass

    def print_graph_keys(self):
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


if __name__ == '__main__':
    p = Parser()

# PARSE 2
# for key_top in graph.keys():  # ex: Python datatypes or Python Operators
#     for key_2 in graph[key_top].keys():  # ex: Python int or Next level
#         if key_2 == 'Next_Level':
#             for key_3 in graph[key_top][key_2].keys():  # ex: Python Arithmetic Operators
#                 # print(1)
#                 for key_4 in graph[key_top][key_2][key_3].keys():  # ex: Python Addition
#                     # print(2)
#                     link = graph[key_top][key_2][key_3][key_4]
#                     # print(link)
#                     example_list = individuals_list_from_link(link)
#                     if example_list:
#                         graph[key_top][key_2][key_3][key_4] = example_list[0]
#
#         else:
#             link = graph[key_top][key_2]
#             example_list = individuals_list_from_link(link)
#             if example_list:
#                 graph[key_top][key_2] = example_list[0]
#             # print(link)
