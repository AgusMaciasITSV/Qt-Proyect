import sys
from PySide2.QtWidgets import QMainWindow, QApplication

from MMenu.mainMenu import Ui_MainWindow as MenuWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MenuWindow()
        self.ui.setupUi(self)
    def openForm():
        pass
    
    def openLists():
        pass

    def confirmExit():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
