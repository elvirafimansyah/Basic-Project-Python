def luas_segitiga():
    alas = float(input('Masukan alas segitiga: '))
    tinggi = float(input("Masukan tinggi segitiga: "))
    luas = 1 / 2 * alas * tinggi
    print("Luas segitiga : ", luas)
    return luas

def keliling_segitiga():
    s1 = float(input("Masukan sisi 1 segitiga: "))
    s2 = float(input("Masukan sisi 2 segitiga: "))
    s3 = float(input("Masukan sisi 3 segitiga: "))
    keliling = s1 + s2 + s3 
    print("Keliling Segitiga : ", keliling)

while True:
    print("===== SELAMAT DATANG DI PROGRAM SEGITIGA")
    print("Berikut Menu yang tersedia:")
    print("1. Mencari Luas Segitiga")
    print("2. Mencari Keliling Segitiga")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        luas_segitiga()
    elif option == "2":
        print("Anda Pilih Menu 2")
        keliling_segitiga()
    elif option == '3':
        break
    else:
        print("Keyword Anda salah silahkan coba lagi!!")