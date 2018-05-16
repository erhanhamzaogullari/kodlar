#!C:\Users\Erhan\AppData\Local\Programs\Python\Python36-32\python.exe

import cgi

form=cgi.FieldStorage()
girdi=form.getvalue("deger")

girdi=int(girdi)
sonuc=[]

while girdi>=0:
    kalan=int(girdi%2)
    sonuc.append(kalan)
    girdi=(girdi-kalan)/2
    if girdi==0:
        sonuc.reverse()
        break
    




print("Content-type:text/html")
print("")
print("""<html style="background-color:darkblue">""")
print("<head>")
print("<title>Binary Çevirici</title>")
print("</head>")
print("<body>")
print("""<h2 style="text-align:center;color:orange;margin-top:300px">Binary karşılığı : """,*sonuc,sep="")
print("</body>")
print("</html>")
    
