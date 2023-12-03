import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow

# Modelo VISTA donde el modelo se conecta a la BD Y REFLEJARA LA INFORMACION Y la vista muestra LA INFORMACIÓN DEL MODELO
# Los cambios que se realizan en la vista se aplican en el modelo y de ahí a la BD

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("Contactos.db"))
        
        if not conexion.open():
            print("No se puede conectar a la Base de Datos")
            sys.exit(True)
        
        modelo = QSqlTableModel()
        modelo.setTable("Contactos")
        modelo.select()
        
        modelo.setHeaderData(0, Qt.Horizontal, "Id")
        modelo.setHeaderData(1, Qt.Horizontal, "Nombres")
        modelo.setHeaderData(2, Qt.Horizontal, "Apellidos")
        modelo.setHeaderData(3, Qt.Horizontal, "Sexo")
        modelo.setHeaderData(4, Qt.Horizontal, "Edad")
        modelo.setHeaderData(5, Qt.Horizontal, "Empleo")
        modelo.setHeaderData(6, Qt.Horizontal, "Número")
        modelo.setHeaderData(7, Qt.Horizontal, "Email")

        self.tabla.setModel(modelo)
        self.tabla.setColumnHidden(0, True)
        self.tabla.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Inicializa la aplicación y muestra la ventana principal