# noinspection PyUnresolvedReferences
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtWidgets
import IconEdit
from owlready2 import *


def print_universal(currentItem, ontology, gui_node, switcher):
    t = currentItem.text(0)
    print(t)
    # print('relevant:', self.onto.currentItem.text(0))
    # print(self.onto.search(iri=(f"{0}", t)))
    gui_node.setPlainText('')
    onto_node = ontology.search_one(iri=f"*{t}")
    if onto_node:
        if onto_node.instances():
            # for i in onto_node.instances():
            #     print(i)

            instansss = onto_node.instances()[0]
            # print(instansss.get_properties())
            # testik = self.onto.onto_node.instances()[0]

            if switcher == 1:
                if instansss.has_SpecText:
                    r = ontology.SpecText[instansss][0]
                    gui_node.setPlainText(r)
            else:
                if instansss.has_ExText:
                    r = ontology.ExText[instansss][0]
                    gui_node.setPlainText(r)

            # print('TYPE:', type(instansss))

            # if instansss['has_SpecText']:
            #     r = ontology['SpecText'][instansss][0]
            #     gui_node.setPlainText(r)

        # print('EPEPPEEPEPEPEPEPp')
        # self.Example_Text = 'fwafwfawfawf'
        # print(self.Example_Text)
    else:
        print("No Instances!")


class MainWindow(QMainWindow):
    """
      Does GUI updates. Builds graph and displays it.
      """

    #
    # TODO:
    #  1) refactor methods using decorators
    #  2) Advanced Topics need fix
    #  3) Add filters for file extensions when opening files
    #  4) Integrate 2 methods of loading files into one or smth
    #  5) Move Dialog classes from main to another file
    #  6) When writing graph, try replace underlines with whitespaces
    #
    def __init__(self):
        super().__init__()

        # self.ui = QTMainW()

        self.Language_Text = None
        self.Tree_Language = None
        self.Example_Text = None
        self.Tree_Examples = None
        self.actionExtendEx = None
        self.actionOpen_Right = None
        self.actionOpen = None
        self.graph_ex: dict = None
        self.graph_lang: dict = None
        self.onto_examples: owlready2.namespace.Ontology = None
        self.onto_lang: owlready2.namespace.Ontology = None
        self.Example_Text: str = None
        self.Lang_Text: str = None
        uic.loadUi('V2Splitter.ui', self)

        # self.Example_Text.setHtml("""print(c)</code></pre> <a class="runonline" target="_blank"
        # href="https://pythonexamples.org/run.php?pgm=a+%3D+10%0Ab+%3D+12%0A%0Ac+%3D+a+%2B+b%0A%0Aprint%28c%29"
        # rel="noindex"> Run</a> <p><strong>Output</strong></p> <pre class="wp-block-code output"><code
        # class="language-python">22</code></pre> <a id="4" class="hide"></a> <h3>Chaining of Addition Operator</h3>
        # <p>You can add more than two numbers in a single statement. This is because, Addition Operator supports
        # chaining.</p> <p><strong>Python Program</strong></p> <pre class="wp-block-code"><code
        # class="language-python">a = 10 b = 12 c = 5 d = 63
        #
        # result = a + b + c + d
        #
        # print(result)</code></pre> <a class="runonline" target="_blank"
        # href="https://pythonexamples.org/run.php?pgm=a+%3D+10%0Ab+%3D+12%0Ac+%3D+5%0Ad+%3D+63%0A%0Aresult+%3D+a+%2B
        # +b+%2B+c+%2B+d%0A%0Aprint%28result%29" rel="noindex"> Run</a> <p><strong>Output</strong></p> <pre
        # class="wp-block-code output"><code class="language-python">90</code></pre> <a id="5" class="hide"></a>
        # <h3>Example 2: Addition of Floating Point Numbers</h3> <p><a
        # href="https://pythonexamples.org/python-float/">Float</a> is one of the numeric datatypes. You can compute
        # the sum of floating point numbers using Python Addition operator. In the following example program,
        # we shall initialize two floating point numbers, and find their sum.</p> <p><strong>Python
        # Program</strong></p> <pre class="wp-block-code"><code class="language-python">a = 10.5 b = 12.9
        #
        # result = a + b
        # """)
        # sf.myWidget.setStyleSheet(“image: url(picture.jpg)”)
        # self.ui.setupUi(self)
        # print(s)
        # s.setupUi(self)

        # print(self.Line_Find.font().setPointSize(72))
        # font = self.Line_Find.font()  # lineedit current font
        # font.setPointSize(18)  # change it's size
        # self.Line_Find.setFont(font)  # set font
        # self.Tree_Examples.itemClicked.connect(self.on_tree_item_clicked)
        # self.Tree_Language.itemClicked.connect(self.on_tree_item_clicked)

        self.show()

    def set_ex_onto(self, onto_ex: owlready2.namespace.Ontology):
        self.onto_examples = onto_ex
        self.graph_ex = self.build_graph_from_onto(self.onto_examples.Ontology_Root)
        # print(self.graph_ex)

    def set_lang_onto(self, onto_lang: owlready2.namespace.Ontology):
        self.onto_lang = onto_lang
        self.graph_lang = self.build_graph_from_onto(self.onto_lang.Ontology_Root)
        # print(self.graph_lang)

    def update_ex_graph(self):
        self.graph_ex = self.build_graph_from_onto(self.onto_examples.Ontology_Root)

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

    def print_tree_from_graph(self, node: QTreeWidget, graph: dict) -> None:
        print('Graph to build:', graph)
        node.clear()
        self.print_tree(node, graph)

    def print_tree(self, tree_parent, local_graph):
        for key in local_graph.keys():
            t = QTreeWidgetItem(tree_parent)
            t.setText(0, key)
            self.print_tree(t, local_graph[key])

    def print_example(self, currentItem):
        print_universal(currentItem, self.onto_examples, self.Example_Text, 0)

    def print_language(self, currentItem):
        print_universal(currentItem, self.onto_lang, self.Lang_Text, 1)

    pass

    # def on_tree_item_clicked(self, Tree: QTreeWidget):
    #     item = self.Tree_Examples.currentItem()
    #     # print(item.text(0))
    #     # print(item.parent().text(0))
    #     print(self.get_path(item))
    #     # print('yep')
    #     pass

    # def get_path(self, item):
    #     def getParent(_item, _out):
    #         if _item.parent() is None:
    #             return _out
    #         out = _item.parent().text(0) + '/' + _out
    #         # print(item.parent.text(e0))
    #         # print(item)
    #         # print(item.parent())
    #         return getParent(_item.parent(), out)
    #
    #     output = getParent(item, item.text(0))
    #     return output

    # def test(self):
    #     print('TEST WORKED')
    #     pass
