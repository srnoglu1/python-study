urunler = {}

id = input("id: ")
modeli = input("modeli: ")
fiyatı = input("fiyatı: ")

urunler[id] ={
    "modeli":  modeli,
    "fiyatı":  fiyatı

}
id = input("id: ")
modeli = input("modeli: ")
fiyatı = input("fiyatı: ")

urunler[id] ={
    "modeli":  modeli,
    "fiyatı":  fiyatı

}
id = input("id: ")
modeli = input("modeli: ")
fiyatı = input("fiyatı: ")

urunler[id] ={
    "modeli":  modeli,
    "fiyatı":  fiyatı

}
print(urunler)

#<<SECOND-DEMO>>

urunler = {
    '100': {'Modeli': 'IPhoneX', 'fiyatı': '5000'},
    '101': {'Modeli': 'IPhoneSE', 'fiyatı': '4500'}, 
    '102': {'Modeli': 'IPhoneXR', 'fiyatı': '6000'}
    }
id = input("Aramak istediğiniz ürün id: ")
urun = urunler[id]
print(f'id: {id} ürün adı: {urun["Modeli"]} ürün fiyatı: {urun["fiyatı"]}')
