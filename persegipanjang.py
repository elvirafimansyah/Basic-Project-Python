def luas_persegi_panjang():
    panjang = float(input('Masukan Panjang persegi panjang: '))
    lebar = float(input("Masukan Lebar persegi panjang: "))
    luas = panjang * lebar
    print("Luas Persegi Panjang : ", luas)
    return luas

def keliling_persegi_panjang():
    p = float(input("Masukan panjang persegi panjang: "))
    l = float(input("Masukan lebar persegi panjang: "))
    keliling = 2 * (p + l)
    print("Keliling persegi panjang : ", keliling)
    return keliling

while True:
    print("===== SELAMAT DATANG DI PROGRAM PERSEGI PANJANG =====")
    print("Berikut adalah menu yang tersedia: ")
    print("1. Mencari Luas persegi panjang")
    print("2. Mencari keliling persegi panjang")
    print("3. Tutup")
    option = input("Option 1 - 3: ")
    if option == "1":
        print("Anda Pilih Menu 1")
        luas_persegi_panjang()
    elif option == "2":
        print("Anda Pilih Menu 2")
        keliling_persegi_panjang()
    elif option == "3":
        break
    else:
        print("Keyword Anda salah silahkan coba lagi!!")
