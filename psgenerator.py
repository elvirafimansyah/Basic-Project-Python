# you must write import random for password can be random
import random

print("========== RANDOM PASSWORD GENERATOR ==========")
print("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}_-()*;/,"
all = alphabet + number + ALPHABET + symbols
#(length) artinya panjang dari password nya 
length = 10


"""
fungsi .join(random.sample()) adalah  digunakan untuk
menggabungkan berbagai macam tipe data contohnya angka, symbols, huruf kecil dan dan huruf besar
"""
password = "".join(random.sample(all,length))

# Rekomendasi password kami, Jika kamu binggung 
print("Recomandation Your Password, if you so confused is : ", password)
# Saya merekomendasi kamu untuk mencatat password kamu di buku/kertas. Jangan lupa password mu !
print("I Recomandation your notes to record the password for you. Don't forget your password")

# Good Luck