# noinspection PyUnresolvedReferences
from PyQt5 import uic
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QAction, QDialog, QDialogButtonBox, QLabel, QMainWindow, QMenu, QMessageBox, QTreeWidget, \
    QTreeWidgetItem
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import copy

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

        self.was_search = False
        self.action_SaveAs = None
        self.action_SaveEx = None
        self.Language_Text = None
        self.Tree_Language = None
        self.Example_Text = None
        self.Tree_Examples = None
        self.BFind = None
        self.Line_Find = None
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
        uic.loadUi('V3Splitter.ui', self)
        # self.Tree_Examples.setContextMenuPolicy(ActionsContextMenu)
        # noinspection PyUnresolvedReferences
        self.Tree_Examples.setContextMenuPolicy(Qt.CustomContextMenu)
        # noinspection PyUnresolvedReferences
        self.BFind.clicked.connect(self.find_main)
        # noinspection PyUnresolvedReferences
        self.Tree_Examples.customContextMenuRequested.connect(self.show_context_menu)
        t = QAction(self.Tree_Examples)
        t.setText("&amp;New")
        self.Tree_Examples.newAction = t
        # self.Tree_Examples.addAction(QAction(self))

        self.show()

    # def test(self):
    #     print('TEST WORKED')
    #     pass

    def find_main(self):
        if not self.onto_examples:  # проверяем что онтология примеров загружена
            print('Загрузите онтологию примеров, чтобы искать в ней!')
            button = QMessageBox.warning(self, "Предупреждение",
                                         "Сначала загрузите онтологию примеров, чтобы искать в ней!")
            return

        if self.was_search:  # значит нажата кнопка отмены
            self.BFind.setText('Найти')
            self.print_tree_from_graph(self.Tree_Examples, self.graph_ex)
            self.Line_Find.clear()
            return

        print('find_main')
        # onto_node = self.onto_examples.search_one(iri=f"*{t}")
        text = self.Line_Find.text()
        print(f'text to search: {text}')
        # print(self.onto_examples.ontology.root)
        t = self.onto_examples.search(iri=f'*{text}*', subclass_of=self.onto_examples['Ontology_Root'],
                                      _case_sensitive=False)
        # subclass_of = 'Ontology_Root'
        if t:
            print(t)
            full_list = []
            for entry in t:
                print(entry)
                print(entry.ancestors())
                print(type(entry))
                for en in entry.ancestors():
                    if en not in full_list:
                        full_list.append(en)

            full_list = [(str(i).split('.')[1]) for i in full_list]
            print('Full list:', full_list)
            # self.recursive_print_tree_graph_from_list(full_list)
            # self.get_graph_ex_from_list(full_list)
            print('DO', self.graph_ex)
            # d = self.graph_ex.copy()
            d = copy.deepcopy(self.graph_ex)
            self.filter_dict_by_list(d, full_list)
            print("POSLE", d)
            print('POSLE_graphex', self.graph_ex)
            self.print_tree_from_graph(self.Tree_Examples, d)
            # full_list.pop(self.onto_examples['owl.Thing'])
            # print('Full list:', full_list)

            self.BFind.setText('Отмена')
            self.was_search = True

        else:
            print('Поиск не дал результатов')
            button = QMessageBox.warning(self, "Предупреждение",
                                         "Поиск не дал результатов")
        pass

    def filter_dict_by_list(self, data, lst):
        if type(data) == dict and bool(data):  # словарь и непустой
            for key in list(data):
                if isinstance(data[key], dict):  # если это вложенный словарь, вызываем эту же функцию для него
                    self.filter_dict_by_list(data[key], lst)
                elif isinstance(data[key], list):  # если это список, вызываем эту же функцию для списка
                    self.filter_dict_by_list(data[key], lst)
                else:  # это строка, ничего не делаем
                    pass

            # удаляем из словаря ключи, которых нет в списке
            for key in list(data):
                if isinstance(data[key], dict) and bool(
                        data[key]):  # если это вложенный непустой словарь, ничего не делаем
                    pass
                elif key not in lst:  # если ключ отсутствует в списке, удаляем его из словаря
                    del data[key]

    def enter_node_name(self, item):
        name, done1 = QtWidgets.QInputDialog.getText(
            self, 'Диалоговое окно ввода', 'Введите имя для нового узла и класса онтологии:')
        # lambda: item.addChild(QTreeWidgetItem())
        print('enter node name')
        print(item)
        if done1:
            q = QTreeWidgetItem()
            q.setText(0, name)
            item.addChild(q)
        pass

    def show_context_menu(self, pos):
        # получаем выбранный элемент
        item = self.Tree_Examples.itemAt(pos)
        # создаем контекстное меню
        menu = QMenu(self)

        # создаем пункт меню "Add child"
        addChildAction = QAction("Добавить дочернюю ноду", self)
        # noinspection PyUnresolvedReferences

        # addChildAction.triggered.connect(lambda: item.addChild(QTreeWidgetItem()))
        addChildAction.triggered.connect(lambda: self.enter_node_name(item))

        # создаем пункт меню "Remove item"
        removeItemAction = QAction("Удалить выбранную ноду", self)
        # noinspection PyUnresolvedReferences
        removeItemAction.triggered.connect(lambda: item.parent().removeChild(item))
        # takeChild(0)

        # добавляем пункты меню в контекстное меню
        menu.addAction(addChildAction)
        if item is not None:
            menu.addAction(removeItemAction)

        # показываем контекстное меню в заданной позиции
        menu.exec_(self.Tree_Examples.mapToGlobal(pos))

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
            msg.setText("У вас есть несохраненные изменения")
            msg.setInformativeText("Сохранить изменения?")
            msg.setWindowTitle("Предупреждение")

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
