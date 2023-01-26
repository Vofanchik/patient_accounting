import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from UI_files.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.save)

    def save(self):
        print(self.ui.lineEdit_51.text())

app = QApplication(sys.argv)
mw = MainWindow()
mw.show()

sys.exit(app.exec_())