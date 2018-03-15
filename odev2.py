def mcs2016():
    global sonuc1 #sonuc1 değişkenini mcsfark fonksiyonunda kullanmak üzere global yaptım
    global a      #a,b değişkenini mcs2017 fonksiyonunda kullanmak üzere global yaptım
    global b
    a=170
    b=50
    sonuc1=a/b

    print("2016 yılı müşterilerle çalışma süreniz: {} saattir.".format(round(sonuc1,2)))

def artis_2017():
    global aa  #aa,ab değişkenini mcs2017 fonksiyonunda kullanmak üzere global yaptım
    global ab
    aa=50  #2017 çalışılan süre artış
    ab=20  #2017 müşteri sayısı artış

    print("+"*30)
    print("""+       2017 yılında         +
+   çalışılan süre {} saat   +
+   müşteri sayısı {} kişi   + 
+       artmıştır.           +""".format(aa,ab))
    print("+"*30)

def mcs2017(a,b,aa,ab):
    global sonuc2  #sonuc2 değişkenini mcsfark fonksiyonunda kullanmak üzere global yaptım
    a=a+aa
    b=b+ab
    sonuc2=a/b

    print("2017 yılı müşterilerle çalışma süreniz: {} saattir.".format(round(sonuc2,2)))

mcs2016()
artis_2017()
mcs2017(a,b,aa,ab)

fark=sonuc1-sonuc2
print("2017-2016 yılları arası müşterilerle çalışma süreleri farkı: {} saattir.".format(round(fark,2)))
    
