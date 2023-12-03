import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from helpers import absPath  # Importa la función absPath desde el módulo helpers
from ui_tabla import Ui_MainWindow  # Importa la clase Ui_MainWindow desde el módulo ui_tabla

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Inicializa la aplicación y muestra la ventana principal