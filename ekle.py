def basaekle():
    oku = open("proje.txt", "r+")
    ekle = oku.read()
    al = input("Eklemek istediğiniz kitabı sırasıyla tarih, yazar ismi ve kitap ismi olarak yazınız.")
    oku.seek(0)
    oku.write("\n" + al)


def ekle():
    oku = open("proje.txt", "a")
    yeniKitapEkle = input("Eklemek istediğiniz kitabı sırasıyla tarih, yazar ismi ve kitap ismi olarak yazınız.")
    oku.write("\n" + yeniKitapEkle )
