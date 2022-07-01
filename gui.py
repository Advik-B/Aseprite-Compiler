from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pre_init()
        self.load_ui()
        self.show()

    def pre_init(self):
        self.resize(600, 700)

    def load_ui(self):
        self.setWindowTitle("PyQt5 GUI")
        self.mbar = self.menuBar()


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)
ui = MainWindow()
sys.exit(app.exec_())
