import random
def guess(x):
    #random randint adalah angka acak atau secara random
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input("Masukan Angka Anda di antara 1 dan {}: ".format(x)))
        if guess < random_number:
            print("Maaf, tebak lagi. Tebakan terlalu rendah")
        elif guess > random_number:
            print("Maaf, tebak lagi. Tebakan terlalu tinggi")
            
    print("Selamat, Kamu telah menebak angka dengan benar \n==============================================")  
       
# guess ini angka maksimal untuk menebak angka random dari python Anda bisa menuliskan angka maksimal di dalam kurung.
while True:
    max_number = int(input("Masukan Angka Maksimal: "))
    guess(max_number)