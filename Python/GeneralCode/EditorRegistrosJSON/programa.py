import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from helpers import absPath  # Importa la función absPath desde el módulo helpers
from ui_tabla import Ui_MainWindow  # Importa la clase Ui_MainWindow desde el módulo ui_tabla

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        with open(absPath("contactos.json")) as archivo:
            self.datos = json.load(archivo)  # Lee el archivo "contactos.json" y almacena los datos en self.datos
        
        self.columnas = ["Nombres", "Apellidos", "Edad", "Empleo", "Email"]  # Define las columnas de la tabla
        
        self.tabla.setRowCount(len(self.datos))  # Establece el número de filas en la tabla
        self.tabla.setColumnCount(len(self.datos))  # Establece el número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(self.columnas)  # Establece las etiquetas de las columnas
        
        for i, fila in enumerate(self.datos):
            for j, columna in enumerate(self.columnas):
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, fila[columna])
                self.tabla.setItem(i, j, item)  # Llena la tabla con los datos de self.datos
        
        self.tabla.resizeColumnsToContents()  # Ajusta el ancho de las columnas automáticamente

        self.tabla.itemChanged.connect(self.celda_modificada)  # Conecta la señal itemChanged a la función celda_modificada

    def celda_modificada(self, item):
        fila, campo = item.row(), self.columnas[item.column()]
        self.datos[fila][campo] = item.data(Qt.EditRole)  # Actualiza los datos en self.datos cuando se modifica una celda
        with open(absPath("contactos.json"), "w") as archivo:
            json.dump(self.datos, archivo)  # Guarda los datos actualizados en el archivo "contactos.json"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Inicializa la aplicación y muestra la ventana principal
