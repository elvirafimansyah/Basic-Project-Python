def luas_layang():
    d1 = float(input("Masukan d1 layang2: "))
    d2 = float(input("Masukan d2 layang2: "))
    luas = 1 / 2 * d1 * d2
    print("Luas layang-layang : ", luas)
    return luas

while True:
    print("===== SELAMAT DATANG DI PROGRAM LAYANG-LAYANG =====")
    print("Berikut Menu yang tersedia:")
    print("1. Mencari Luas layang-layang")
    print("2. Tutup")
    option = input("Option 1-2 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        luas_layang()
    elif option == "2":
        break
    else:
        print("Keyword Anda salah!! Silahkan coba lagi")
