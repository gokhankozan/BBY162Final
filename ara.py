def ara():
    while True:
        arama = input("Aramak istediğin kitap adı,tarih ya da yazar ismini yazın. ")
        oku = open("proje.txt")
        for satir in oku.readlines():
            if satir.lower().find(arama) != -1:
                print(satir)
            elif satir.upper().find(arama) !=-1:
                print(satir)

