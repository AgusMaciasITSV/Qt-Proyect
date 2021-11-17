import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

from MMenu.mainMenu import Ui_MainWindow as MenuWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MenuWindow()
        self.ui.setupUi(self)
        #self.CExit = ConfirmEx()

    def openForm(self):
        pass
    
    def openList(self):
        pass

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


#         confirm = QMessageBox()
#         confirm.setInformativeText("Esta seguro que desea salir?")
#         confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#         confirm.setDefaultButton(QMessageBox.Yes)
#         confirm.setText("Se eliminaran todos los alumnos")
#         confirmation = confirm.exec()
#         if confirmation == QMessageBox.Yes:
#             self.close()
# #         self.CEXit.show()

# # class ConfirmEx(QMainWindow):
# #     def salir(self):
# #         confirm = QMessageBox()
# #         confirm.setInformativeText("Esta seguro que desea salir?")
# #         confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
# #         confirm.setDefaultButton(QMessageBox.Yes)
# #         #confirm.setText("Se eliminaran todos los alumnos")
# #         confirmation = confirm.exec()
# #         if confirmation == QMessageBox.Yes:
# #             self.close()