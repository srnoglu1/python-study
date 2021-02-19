#  ---- QUESTIONS ----

name = ["Ada","Yiğit","Beril","Cansu","Kerem"]
years = [1998,1996,1999,2001,2003]

#cenk ismini listenin sonuna ekle ?
 name.append("Cenk")
 sonuc = name
 print(sonuc)

#nazlı ismini listenin başına ekle ?
 name.insert(0,"Nazlı")
 sonuc = name
 print(sonuc)

#yiğit ismini listeden siliniz ?
 name.pop(1)
 sonuc = name
 print(sonuc)

#liste elemanlarını ters çevirin ?
 name.reverse()
 sonuc = name
 print(sonuc)

#years listesini rakamsal büyüklüğe göre sıralayın ?
 years.sort()
 sonuc = years
 print(years)

#years dizisini en büyük ve en küçük elemanı nedir ?
 sonuc = min(years)
 sonuc = max(years)
 print(sonuc)

#beril ismi listenin bir elemanımıdır ?
 sonuc = "Beril" in name
 print(sonuc)

#yiğit isminin indexi nedir ?
 index = name.index("Yiğit")
 name.pop(index)
 print(index)

#p = "iphoneX", "iphoneXS" karekter dizesini listeye çeviriniz ?
 p = "IphoneX,IphoneXS"
 sonuc = p.split(",")
 print(sonuc)

#years dizisinde kaç tane 1998 değeri vardır ?
 print(years.count(1998))

#years dizisindeki tüm elemanlarını siliniz ?
 years.clear()
 print(years)

#Kullanıcıdan alacağınız 3 tane marka bilgisini yazdırıp bir listede saklayınız ?
 markalar = []

 marka = input("Marka: ")
 markalar.append(marka)

 marka = input("Marka: ")
 markalar.append(marka)

 marka = input("Marka: ")
 markalar.append(marka)

 print(markalar)
