from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
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

        # editb = self.findChild(QToolButton, "B_edit")
        # print(editb)
        # editb.setStyleSheet('icon: url(edit_ico.ico)')

        self.show()
