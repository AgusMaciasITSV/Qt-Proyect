import sys

from PyQt5.QtCore import QCoreApplication
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

from formpro import Ui_form


class Formwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form()
        self.ui.setupUi(self)

    def agregar(self):
        data = {
            'nombre': self.ui.nombreline.text(),
            'apellido': self.ui.apellidoline.text(),
            'documento': self.ui.dniline.text(),
            'fecha': self.ui.fechaseleccion.date(),
            'ciudad': self.ui.ciudadseleccion.currentText(),
            'vacuna': self.ui.vacunaseleccion.currentText(),
        }
        count_before = len(self.parent.students)
        self.parent.LATABLA.append(data)
        print(self.parent.LATABLA)
        if count_before != len(self.parent.LATABLA):
            message = QMessageBox()
            message.setText(f"Se agrego el vacunado {data['nombre']} exitosamente")
            message.exec()

    def borrar(self):
        self.ui.nombreline.setText("")
        self.ui.nombreline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el nombre", None))
        self.ui.apellidoline.setInputMask("")
        self.ui.apellidoline.setText("")
        self.ui.apellidoline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el apellido", None))
        self.ui.dniline.setText("")
        self.ui.dniline.setPlaceholderText(QCoreApplication.translate("form", u"Ingrese el DNI", None))
        self.ui.botonborrar.setText(QCoreApplication.translate("form", u"Borrar", None))
        self.ui.botonagregar.setText(QCoreApplication.translate("form", u"agregar", None))
        self.ui.ciudadseleccion.setItemText(0, QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.ui.ciudadseleccion.setItemText(1, QCoreApplication.translate("form", u"La calera", None))
        self.ui.ciudadseleccion.setItemText(2, QCoreApplication.translate("form", u"Villa allende", None))
        self.ui.ciudadseleccion.setItemText(3, QCoreApplication.translate("form", u"Narnia", None))

        self.ui.ciudadseleccion.setCurrentText(QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.ui.vacunaseleccion.setItemText(0, QCoreApplication.translate("form", u"Seleccione la vacuna", None))
        self.ui.vacunaseleccion.setItemText(1, QCoreApplication.translate("form", u"SPUTNIK V(1era dosis)", None))
        self.ui.vacunaseleccion.setItemText(2, QCoreApplication.translate("form", u"SPUTNIK V(2da dosis)", None))
        self.ui.vacunaseleccion.setItemText(3, QCoreApplication.translate("form", u"ASTRAZENECA(1era dosis)", None))
        self.ui.vacunaseleccion.setItemText(4, QCoreApplication.translate("form", u"ASTRAZENECA(2da dosis)", None))
        self.ui.vacunaseleccion.setItemText(5, QCoreApplication.translate("form", u"PFIZER(1era dosis)", None))
        self.ui.vacunaseleccion.setItemText(6, QCoreApplication.translate("form", u"PFIZER(2da dosis)", None))
        self.ui.vacunaseleccion.setItemText(7, QCoreApplication.translate("form", u"MODERNA(1era dosis)", None))
        self.ui.vacunaseleccion.setItemText(8, QCoreApplication.translate("form", u"MODERNA(2da dosis)", None))
        self.ui.vacunaseleccion.setItemText(9, QCoreApplication.translate("form", u"SINOPHARM(1era dosis) ", None))
        self.ui.vacunaseleccion.setItemText(10, QCoreApplication.translate("form", u"SINOPHARM(2da dosis) ", None))

    def nombre(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Formwindow()
    window.show()

    sys.exit(app.exec_())
