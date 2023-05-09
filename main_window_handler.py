# noinspection PyUnresolvedReferences
from PyQt5 import uic
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QMainWindow, QMessageBox, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import IconEdit
from owlready2 import *


def print_universal(currentItem, ontology, gui_node, switcher):
    t = currentItem.text(0)
    print(t)
    # print('relevant:', self.onto.currentItem.text(0))
    # print(self.onto.search(iri=(f"{0}", t)))
    gui_node.setPlainText('')  # обнуление текста
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
                    # r = ontology.SpecText[instansss][0]
                    gui_node.setPlainText(instansss.SpecText)
            else:
                if instansss.has_ExText:
                    # r = ontology.ExText[instansss][0]
                    gui_node.setPlainText(instansss.ExText)

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
    #  7) Use alertbox or smth instead of console, which user dont see
    #  8) May need to redone print_example calling from main since its dif-t there already
    #
    def __init__(self):
        super().__init__()

        # self.ui = QTMainW()

        self.action_SaveAs = None
        self.action_SaveEx = None
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
        self.Lang_Text: str = None
        self.start_print: bool = False
        self.last_cur_item = None
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

    def save_element_to_ontoex(self, item, new_example: str):
        t = item.text(0)
        print(t)
        # print('relevant:', self.onto.currentItem.text(0))
        # print(self.onto.search(iri=(f"{0}", t)))
        onto_node = self.onto_examples.search_one(iri=f"*{t}")
        if onto_node and onto_node.instances():
            instansss = onto_node.instances()[0]
            if instansss.has_ExText:
                print(instansss.ExText)
                print(new_example)
                instansss.ExText = new_example
                self.onto_examples.save()
                # r = self.onto_examples.ExText[instansss][0]
        # self.onto_examples.ExText[instansss]

        # print('TYPE:', type(instansss))

        # if instansss['has_SpecText']:
        #     r = ontology['SpecText'][instansss][0]
        #     gui_node.setPlainText(r)

        # print('EPEPPEEPEPEPEPEPp')
        # self.Example_Text = 'fwafwfawfawf'
        # print(self.Example_Text)
        else:
            print("Error: No Instances to save to!")

    def print_example(self, currentItem):
        # self.text_ch_counter = 0
        # self.text_ch_counter = 2
        if currentItem == self.last_cur_item:  # fix для cancel
            return

        if self.start_print:  # если были изменения
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("This is a message box")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("MessageBox demo")

            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            # msg.buttonClicked.connect(lambda x: print(x))

            button = msg.exec_()

            if button == QMessageBox.Save:
                self.save_element_to_ontoex(self.last_cur_item, self.Example_Text.toPlainText())
                self.last_cur_item.setBackground(0, QtGui.QBrush(QtGui.QColor('#9bff9d')))
            elif button == QMessageBox.Discard:
                self.last_cur_item.setBackground(0, QtGui.QBrush(QtGui.QColor(255, 255, 255, 0)))
            else:  # cancel
                # self.ite
                # print(currentItem.isSelected())
                currentItem.setSelected(False)
                self.last_cur_item.setSelected(True)
                return

        self.start_print = True  # fix для change_text()
        # print(currentItem)
        # print(type(currentItem))
        self.last_cur_item = currentItem  # do not move up or down
        # currentItem.setForeground(0, QtGui.QBrush(QtGui.QColor("#123456")))
        print_universal(currentItem, self.onto_examples, self.Example_Text, 0)
        self.start_print = False
        # print('coutner after print:')

    def change_text_example(self):
        if not self.start_print:
            print('test')
            self.last_cur_item.setBackground(0, QBrush(QColor('#fac831')))
            self.start_print = True

        # if self.text_ch_counter >= 2:
        # self.text_ch_counter += 1
        # print(self.text_ch_counter)

    def print_language(self, currentItem):
        print_universal(currentItem, self.onto_lang, self.Lang_Text, 1)

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
