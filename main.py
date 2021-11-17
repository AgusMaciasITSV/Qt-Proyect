import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

from MMenu.mainMenu import Ui_MainWindow as MenuWindow
from Form.form_code import Formwindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MenuWindow()
        self.ui.setupUi(self)
        self.form = Formwindow(parent=self)
#        self.list= ListWindow(parent=self)

    def openForm(self):
        self.form.show()
        self.ui.hide()
    
    # def openList(self):
    #     self.list.show()
    #     self.ui.hide()

    def confirmEx(self):
        confirm = QMessageBox()
        confirm.setInformativeText("Esta seguro que desea salir?")
        confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm.setDefaultButton(QMessageBox.Yes)
        confirmation = confirm.exec()
        if confirmation == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())