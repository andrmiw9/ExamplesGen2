from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtWidgets
import IconEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = QTMainW()
        self.Tree_Language = None
        self.Tree_Examples = None
        self.Example_Text = None
        self.Language_Text = None

        uic.loadUi('V2Splitter.ui', self)
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
