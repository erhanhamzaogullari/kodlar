print("Ekipman etkinlik oranını hesaplamak için oee() yazınız ve girdilerinizi yazınız!")


def kullanilabilirlik():
    a=int(input("Lütfen planlanmış üretim süresini giriniz!:"))
    b=int(input("Lütfen plansız duruş süresini giriniz!:"))
    c=int(input("Lütfen planlanmış üretim süresi giriniz!:"))
    kullanilabilirlik=(a-b)/c
    return kullanilabilirlik
def performans():
    a=int(input("Lütfen standart çevrim süresini giriniz!:"))
    b=int(input("Lütfen üretim miktarını giriniz!:"))
    c=int(input("Lütfen planlanmış üretim süresini giriniz!:"))
    d=int(input("Lütfen plansız duruş süresini giriniz!:"))
    performans=(a*b)/(c-d)
    return performans
def kalite():
    a=int(input("Lütfen sağlam ürün miktarını giriniz!:"))
    b=int(input("Lütfen toplam üretim miktarını giriniz!"))
    kalite=a/b
    return kalite
def oee():
    oee=kullanilabilirlik()*performans()*kalite()
    return oee


    
