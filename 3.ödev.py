print("Adam başı ciro değerini hesaplamak için adambasiciro() yazınız!")
def ciro():
    a=int(input("Lütfen satış miktarını giriniz!:"))
    b=int(input("Lütfen birim satış fiyatını giriniz!:"))
    ciro=a*b
    return ciro
def adambasiciro():
    calisanSayisi=int(input("Lütfen çalışan sayısını giriniz!:"))
    adamBasiCiro=ciro()/calisanSayisi
    return adamBasiCiro
