import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

uygulama=QApplication(sys.argv)
pencere=QWidget()
izgara=QGridLayout()

def hesapla():
    sayi=int(girdi.text())
    sayi2=int(girdi2.text())
    sayi3=int(girdi3.text())
    ort_calisan_sayi=sayi2/sayi3
    personel_devir_hizi=(sayi/ort_calisan_sayi)*100
    personel_devir_hizi=str(personel_devir_hizi)
    cikti.setText(personel_devir_hizi)

metin=QLabel("Toplam işten ayrılan personel sayısı:")
metin2=QLabel("Aylık çalışan sayısı toplamı:")
metin3=QLabel("Hesaplama yapılmak istenen Ay:")
metin4=QLabel("Hesapla:")
cikti=QLabel("0.00")
buton=QPushButton("Hesapla")

pencere.connect(buton,SIGNAL("pressed()"),hesapla)

girdi=QLineEdit("")
girdi2=QLineEdit("")
girdi3=QLineEdit("")

izgara.addWidget(metin,0,0)
izgara.addWidget(metin2,1,0)
izgara.addWidget(metin3,2,0)
izgara.addWidget(metin4,3,0)

izgara.addWidget(girdi,0,1)
izgara.addWidget(girdi2,1,1)
izgara.addWidget(girdi3,2,1)
izgara.addWidget(cikti,3,1)

izgara.addWidget(buton,5,0)


pencere.setLayout(izgara)
pencere.setWindowTitle("İşgücü Devir Hızı")
pencere.setFixedSize(600,150)
pencere.show()
uygulama.exec_()


