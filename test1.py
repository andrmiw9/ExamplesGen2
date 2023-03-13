# print("Hello there!")
# text = ""
# pat = "@"
# with open("Classes.py", 'r+') as f:
#     for line in f:
#         # line = line.rstrip()
#         text += line
#
#     print(text)
#     print(type(text))
#
#     text = text.replace('@', "OBLADI-OBLADA!")
#     # print(text)
#     # print
#     print(5)
#
#     print(text)

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title('Testing1')
# root.geometry("1000x500")
#
# tr = ttk.Treeview(root)
# # tr['columns'] = ("Name", "Sec")
# # tr.column("#0", width=120, minwidth=100)
# # tr.column("Name", width=120, anchor=W)
# # tr.column("Sec", width=20, anchor=CENTER)
# #
# # tr.heading('#0', text='First', anchor=W)
# # tr.heading('Name', text='Second', anchor=W)
# # tr.heading('Sec', text='Third', anchor=W)
#
# tr.insert(parent='', index="end", iid=0, text='Something1', values=("john", 2))
# tr.insert(parent='0', index="end", iid=1, text='Something1', values=("mat", 51))
# tr.grid()


# FeetToMeters(root)
# tree = ttk.Treeview(root)
# # Inserted at the root, program chooses id:
# tree.insert('', 'end', 'widgets', text='Widget Tour')
#
# # Same thing, but inserted as first child:
# tree.insert('', 0, 'gallery', text='Applications')
#
# # Treeview chooses the id:
# id = tree.insert('', 'end', text='Tutorial')
#
# # Inserted underneath an existing node:
# tree.insert('widgets', 'end', text='Canvas')
# tree.insert(id, 'end', text='Tree')


# root.mainloop()


from PyQt5 import QtWidgets as qw
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from TestQt import Ui_MainWindow as QTMainW
import sys


def application():
    # app = QApplication(sys.argv)
    # mwind = QMainWindow()
    #
    # mwind.setWindowTitle("Test1")
    # mwind.setGeometry(300, 255, 122, 521)
    #
    # mwind.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    window = TestQtWindow()
    sys.exit(app.exec_())


class TestQtWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = QTMainW()
        uic.loadUi('TestQt.ui', self)
        # self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    application()
    print("Something New!")
    print('cadabra')
    print('tatatabra')
