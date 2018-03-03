print("Şirket karınızı hesaplamak için lütfen değerlerinizi doğru giriniz!")

finansmanGelir=int(input("Lütfen finansman gelirini giriniz!:" ))
pazarGelir=int(input("Lütfen pazar gelirini giriniz!:" ))
kiraGelir=int(input("Lütfen kira gelirini giriniz!:" ))

ucret=int(input("Lütfen ücret giderini giriniz!:" ))
finansmanGider=int(input("Lütfen ücret giderini giriniz!:" ))
pazarGider=int(input("Lütfen pazar giderini giriniz!:" ))
kiraGider=int(input("Lütfen kira giderini giriniz!:" ))
muhasebeGider=int(input("Lütfen muhasebe giderini giriniz!:" ))

gelir=finansmanGelir+pazarGelir+kiraGelir
gider=ucret+finansmanGider+pazarGider+kiraGider+muhasebeGider
kar=gelir-gider

if kar>1000:
    print("Karlı!")
else:
    print("Karlı Değil!")
