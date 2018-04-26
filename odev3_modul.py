def etkilesim_orani():
    global oran
    a=int(input("Beğeni sayısını giriniz:"))
    b=int(input("Yorum sayısını giriniz:"))
    c=int(input("Paylaşım sayısını giriniz:"))
    d=int(input("İçerik sayısını giriniz:"))
    e=int(input("Takipçi sayısını giriniz:"))
    oran=(((a+b+c)/d)/e)
    print("Etkileşim oranınız:",oran)

etkilesim_orani()

if oran<0.2:
    print("Başarısız")
else:
    print("Başarılı")
    
