 sayilar = [1,5,7,3,8,6,9,2,7,66]
 harfler = ["a","c","u","d","s","o","y","c"]
 sonuc = min(sayilar)
 sonuc = max(sayilar)
 sonuc = max(harfler)
 sonuc = min(harfler)
 print(sonuc)
 
#ekleme
 sayilar.append(10) 
 sayilar.insert(3,4)
 sayilar.insert(-1,9)
 sayilar.insert(len(sayilar),50)

#silme 
 sayilar.pop()
 sayilar.pop(0)
 sayilar.remove(8)
 harfler.remove("u")

#sıralama
 sayilar.sort()
 harfler.sort()
 sayilar.reverse()

 print(sayilar.count(7))
 print(harfler.count("c"))
 print(sayilar.index(66))
 print(sayilar.clear())


