def fungsi():
    hasilnow = float(input("Masukan Koin Anda Sekarang : "))
    jalan = hasilnow + float(20)
    print("Berikut Menu yang tersedia: ")
    print("1. Silahkan tulis ( y atau yes ) di bawah jika koin bertambah 20 di input di bawah ini")
    print("2. Silahkan tulis ( s atau no) setelah itu, Input nominal koin yang anda dapat random")
    option = input("Option 1-2: ")
    if option == "y" or "yes":
        print("Koin Anda berjumlah : ", jalan)
    elif option == "s" or "tidak":
        koin = float(input("Masukan Koin yang Anda dapat random : "))
        koinrun = koin + hasilnow
        print("Koin Anda berjalan : ", koinrun)
    else: 
        print("Keyword Anda salah!!, Silahkan coba lagi")
    
    return jalan
    return koinrun
while True:
    fungsi()