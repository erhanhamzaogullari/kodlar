def aktif():
    global aktif
    print("--------------Dönen Varlıklar---------------")
    a=int(input("100 Kasa hesabını giriniz:"))
    b=int(input("101 Alınan çekler hesabını giriniz:"))
    c=int(input("102 Bankalar hesabını giriniz:"))
    d=int(input("121 Alınacak senetler hesabını giriniz:"))
    e=int(input("153 Ticari mallar hesabını giriniz:"))
    donen=a+b+c+d+e
    print("------------Dönen Varlıklar=",donen,"------------")

    print("")
    print("")

    print("--------------Duran Varlıklar---------------")
    f=int(input("252 Binalar hesabını giriniz:"))
    g=int(input("254 Taşıtlar hesabını giriniz:"))
    h=int(input("255 Demirbaşlar hesabını giriniz:"))
    duran=f+g+h
    print("------------Dönen Varlıklar=",duran,"------------")

    print("")
    
    aktif=donen+duran
    print("Aktif Toplam =",aktif)

def pasif():
    global pasif
    print("--------Kısa Vadeli Yabancı Kaynak----------")
    a=int(input("300 Banka kredileri hesabını giriniz:"))
    b=int(input("320 Satıcılar hesabını giriniz:"))
    kvyk=a+b
    print("--------Kısa Vadeli Yabancı Kaynak=",kvyk,"-----")
    
    print("")
    print("")

    print("--------Uzun Vadeli Yabancı Kaynak----------")
    c=int(input("400 Banka kredileri hesabını giriniz:"))
    d=int(input("421 Borç senetleri hesabını giriniz:"))
    uvyk=c+d
    print("--------Uzun Vadeli Yabancı Kaynak=",uvyk,"-----")
    
    print("")
    print("")

    print("----------------Öz Kaynaklar----------------")
    e=int(input("500 Sermaye hesabını giriniz:"))
    print("----------------Öz Kaynaklar=",e,"----------")
    
    print("")
    
    pasif=kvyk+uvyk+e
    print("Pasif Toplam =",pasif)

    print("")


aktif()
pasif()
if aktif==pasif:
    print("Kapanış bilançosu doğru hesaplanmıştır!")
else:
    print("Bilanço yanlış hesaplanmıştır!")












    
