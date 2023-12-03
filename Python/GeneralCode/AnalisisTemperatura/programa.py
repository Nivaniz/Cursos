from PySide6 import QtWidgets
from ui_monitor import Ui_MainWindow
from functools import partial
import pyqtgraph as pg  
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.valores = [
            {"nombre": "Valor 1", "valores": [], "color": "r", "simbolo": "o"},
            {"nombre": "Valor 2", "valores": [], "color": "b", "simbolo": "o"},
            {"nombre": "Valor 3", "valores": [], "color": "g", "simbolo": "o"},
        ]
        
        for valor in self.valores:
            self.comboBox.addItem(valor["nombre"])
        
        self.construirGrafico()
        self.pushButton.clicked.connect(self.AgregarTemperatura)
        self.pushButton_2.clicked.connect(partial(self.AgregarTemperatura, True))

        
    def construirGrafico(self):
        self.widget.addLegend()
        self.widget.setBackground("w")
        self.graficos = []
        for valor in self.valores:
            plot = self.widget.plot(valor["valores"], name=valor["nombre"],
                                    pen=pg.mkPen(valor["color"], width=3),
                                    symbol=valor["simbolo"],
                                    symbolBrush=valor["color"], symbolSize=12)
            self.graficos.append(plot)

        self.widget.showGrid(x=True, y=True)
        self.widget.setYRange(-40, 50)
        self.widget.setTitle("Reporte de Temperaturas", size="20px")
        styles = {"color": "#000", "font-size": "15px"}
        self.widget.setLabel("left", "Temperaturas (ºC)", **styles)
        self.widget.setLabel("bottom", "Horas (H)", **styles)
    
    
    def AgregarTemperatura(self, autogenerar=False):
        if not autogenerar:
           indice = self.comboBox.currentIndex()
           temperatura = self.spinBox.value()
           self.valores[indice]["valores"].append(temperatura)
           self.graficos[indice].setData(self.valores[indice]["valores"])
        else:
            for indice, valor in enumerate(self.valores):
                temperatura = random.randint(-20, 50)
                valor["valores"].append(temperatura)
                self.graficos[indice].setData(valor["valores"])
        
            
if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
