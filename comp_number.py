import random
def computer_guess(x):
    rendah = 1 
    tinggi = x
    umpanbalik = ''
    while umpanbalik != 'c' and rendah != tinggi:
        if tinggi != rendah:
            guess = random.randint(rendah, tinggi)
        else:
            guess = rendah
        
        # print("Perhatian !Harap menggunakan huruf KECIL, Jangan menggunakan huruf KAPITAL!")
        umpanbalik = input("Apakah {} terlalu tinggi (T), terlalu rendah (R) atau benar (B) ? ".format(guess)).lower()
        if umpanbalik == "t":
            tinggi = guess - 1
        elif umpanbalik == "r":
            rendah = guess + 1
        elif umpanbalik == "b":
            print("Selamat, Computer telah berhasil menebak angka anda dengan benar")
    
#maksimal angka yang akan di tebak adalah  tulis di dalam kurung angkanya

while True:
    print("Perhatian! Harap menggunakan huruf KECIL, Jangan menggunakan huruf KAPITAL!")
    max_num = int(input("Masukan Angka Maksimal: "))
    computer_guess(max_num)