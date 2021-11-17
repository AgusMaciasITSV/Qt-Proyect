import sys

from PyQt5.QtCore import QCoreApplication
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import json
from datetime import datetime

from ui_files.formpro import Ui_form
from ui_files.tabla1 import Ui_tabla


class Ui_table(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tabla()
        self.ui.setupUi(self)


class Persona:
    def __init__(self, nombre="", apellido="", dni=0, fecha=0, ciudad="", vacuna=""):
        super(Formwindow).__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha = fecha
        self.ciudad = ciudad
        self.ciudad = ciudad
        self.vacuna = vacuna
        self.vacunados = [
            {
                'nombre': 'h',
                'apellido': 'Sanchez',
                'documento': '123123123'
            }
        ]

    def nueva(self):
        data = {}
        data["persona"] = []

        data["persona"] = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'documento': self.dni,
            'fecha': self.fecha,
            'ciudad': self.ciudad,
            'vacuna': self.vacuna,
        }
        self.data.append(self.vacunados)
        with open('data.json', 'w') as file:
            json.dump(self.vacunados, file, indent=12, default=str)


class Formwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form()
        self.ui.setupUi(self)
        self.ui.label.hide()
        self.tabla = Ui_table()
        self.vacunados = [
            {
                'nombre': 'h',
                'apellido': 'Sanchez',
                'documento': '123123123'
            }
        ]

    """def closeEvent(self, event):
        self.hide()
        self.parent.show()"""

    def agregar(self):

        ciudad = self.ui.ciudadseleccion.currentText()
        vacuna = self.ui.vacunaseleccion.currentText()
        nombre = self.ui.nombreline.text()
        apellido = self.ui.apellidoline.text()
        dni = self.ui.dniline.text()
        fecha = self.ui.fechaseleccion.date()
        if not vacuna == "Seleccione la vacuna" and not ciudad == "seleccione ciudad" and not nombre == "" and not apellido == "" and not dni == "":
            message = QMessageBox()
            message.setText("Se cargaron los datos correctamente")
            message.exec()
        if vacuna == "Seleccione la vacuna" or ciudad == "seleccione ciudad" or nombre == "" or apellido == "" or dni == "":
            message = QMessageBox()
            message.setText("Termine de ingresar los datos porfavor")
            message.exec()
        row = int(self.tabla.ui.tableWidget.rowCount())
        self.tabla.ui.tableWidget.insertRow(row)
        persona = [ciudad, vacuna, nombre, apellido, dni, fecha]

        print(row)
        for i in range(len(persona)):
            item_to_add = str(persona[i])
            print( persona[i])
            self.tabla.ui.tableWidget.setItem(row, i, QTableWidgetItem(item_to_add))
        Persona(ciudad, vacuna, nombre, apellido, dni, fecha)

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
        self.ui.ciudadseleccion.setCurrentText(QCoreApplication.translate("form", u"seleccione ciudad", None))
        self.ui.vacunaseleccion.setCurrentText(QCoreApplication.translate("form", u"Seleccione la vacuna", None))
        self.ui.fechaseleccion.setDate(datetime.now().date())

    def nombre(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Formwindow()
    window.show()

    sys.exit(app.exec_())
