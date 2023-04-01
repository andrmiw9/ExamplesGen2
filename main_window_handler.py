from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtWidgets
import IconEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = QTMainW()
        uic.loadUi('TestQt.ui', self)
        # sf.myWidget.setStyleSheet(“image: url(picture.jpg)”)
        # self.ui.setupUi(self)
        # print(s)
        # s.setupUi(self)
        self.treeWidget.itemClicked.connect(self.onItemClicked)

        self.show()

    def onItemClicked(self):
        item = self.treeWidget.currentItem()
        # print(item.text(0))
        # print(item.parent().text(0))
        print(self.getParentPath(item))
        # print('yep')
        pass

    def getParentPath(self, item):
        def getParent(item, _out):
            if item.parent() is None:
                return _out
            out = item.parent().text(0) + '/' + _out
            # print(item.parent.text(0))
            # print(item)
            # print(item.parent())
            return getParent(item.parent(), out)

        output = getParent(item, item.text(0))
        return output
