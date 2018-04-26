def isletme_kari():

    print("------------İşletme karı------------")
    print("")
    gelir=int(input("Gelirlerinizi giriniz:"))
    gider=int(input("Giderlerinizi giriniz:"))
    isletme_kari=gelir-gider
    print("İşletme karı=",isletme_kari)
    print("")
    

def adam_basi_ciro():

    print("-----------Adam başı ciro-----------")
    print("")
    toplam_ciro=int(input("Toplam cironuzu giriniz:"))
    toplam_calisan_sayisi=int(input("Toplam çalışan sayınızı giriniz:"))
    adam_basi_ciro=toplam_ciro/toplam_calisan_sayisi
    print("Adam başı ciro=",adam_basi_ciro  )
    return adam_basi_ciro

isletme_kari()
adam_basi_ciro()
