ogrenciler = {
    100: {
        "ad" : "Emirhan",
        "soyad" : "Sirinoglu",
        "yas" : 22,
        "notlar" : [50,65,80]
        
    },
    101: {
        "ad" : "Ada",
        "soyad" : "Serim",
        "yas" : 19,
        "notlar" : [45,30,75]
    }

}
sonuc = ogrenciler[100]["ad"]
sonuc = ogrenciler[101]["soyad"]
sonuc = (ogrenciler[101]["notlar"] [0] + ogrenciler[101]["notlar"] [1] + ogrenciler[101]["notlar"] [2])/3
sonuc = (ogrenciler[100]["notlar"] [0] + ogrenciler[101]["notlar"] [1] + ogrenciler[101]["notlar"] [2])/3

print(sonuc)
