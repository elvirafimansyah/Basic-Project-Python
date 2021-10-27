#cara pertama
varMinimum = int(input("Masukan nilai minimum : "))
varMaksimum = int(input("Masukan nilai maksimum : "))
x = int(input("Masukan angka kelipatan yang di cari : "))
print("")
print("======= HASIL =======")
print("")
jumlah = []

while varMinimum <= varMaksimum :
    if (varMinimum%x)== 0:
        print (varMinimum)
        jumlah.append(varMinimum)
    varMinimum+=1

print("Jumlah item : ", len(jumlah))
#Good Luck

#cara kedua

# i = 0
# i < ini maksmal kelipatan angka bisa sampai 10000000000 contoh aja yang dibawah ini maksmal 20

# while i < 20:
    # print(i)
    # yang i += ini angka untuk mencari 
    # Kelipatan contoh mau cari kelipatan 4 tulis aja i += 4
    # i += 2
    #Good Luck