from ekle import *
from ara import *
from liste import *

cevaplar = ["A", "S", "L"]
print("Kitap eklemek için (A)")
print("Kitap araması yapmak için (S)")
print("Kitapları listelemek için (L)")
cevaplarim = ["ö", "s"]
islem = input("Yapmak istediğin işlemi seç : ")
if islem.upper() == cevaplar[0]:
    sor = input("Ekleyeceğin kitap cumhuriyetten öncesine mi sonrasına mı ait? Ö/S")
    if cevaplarim[0] == sor.lower():
        basaekle()
    else:
        ekle()
elif islem.upper() == cevaplar[1]:
    ara()
elif islem.upper() == cevaplar[2]:
    liste()



