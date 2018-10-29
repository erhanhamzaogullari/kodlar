import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
data = {'Adi':['Can','Semih','Büşra'], 'Soyadi':['Aydın','Yarar','Demirgüreşçi'], 'bolum':['YBS','YBS','İktisat']}
 
class MyTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.veri = data
        self.setverim()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def setverim(self):
 
        liste=[]
        for n, key in enumerate(sorted(self.veri.keys())):
            liste.append(key)
            
            for m, item in enumerate(self.veri[key]):
                yeni = QTableWidgetItem(item)
                self.setItem(m, n, yeni)
                
             
        self.setHorizontalHeaderLabels(liste)
 
def tabloekran(args):
    app = QApplication(args)
    table = MyTable(data, 3, 3)
    table.show()
    sys.exit(app.exec_())
 
if __name__=="__main__":
    tabloekran(sys.argv)
