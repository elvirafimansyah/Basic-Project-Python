def luas_persegi():
    sisi = float(input("Masukan sisi persegi: "))
    luas2 = sisi * sisi
    print("Luas Persegi : ", luas2)
    return luas2

def keliling_persegi():
    s = float(input("Masukan sisi persegi: "))
    keliling2 = s * 4
    print("Keliling Persegi : ", keliling2)
    return keliling2

while True:
    print("====== SELAMAT DATANG DI PROGRAM PERSEGI ======")
    print("Berikut adalah menu yang tersedia: ")
    print("1. Mencari luas persegi")
    print("2. Mencari Keliling persegi")
    print("3. Tutup")
    option = input("Option 1-3 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        luas_persegi()
    elif option == '2':
        print("Anda Pilih Menu 2")
        keliling_persegi()
    elif option == '3':
        break
    else:
        print("Keyword Anda salah silahkan coba lagi!!")