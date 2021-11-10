import sys
from PySide2.QtWidgets import QMainWindow, QApplication

from su_archivo_convertido_desde_ui import nombre_de_la_clase_en_el_archivo_convertido_de_ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = nombre_de_la_clase_en_el_archivo_convertido_de_ui()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
