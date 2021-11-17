import sys
from PySide2.QtWidgets import QMainWindow, QApplication

from MMenu.mainMenu import Ui_MainWindow as MenuWindow
from MMenu.exit_dialog import Ui_Dialog as ExDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MenuWindow()
        self.ui.setupUi(self)
        self.CExit = ConfirmEx()

    def openForm(self):
        pass
    
    def openLists(self):
        pass

    def confirmExit(self):
        self.CEXit.show()

class ConfirmEx(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ExDialog()
        self.ui.setupUi(self)       

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
