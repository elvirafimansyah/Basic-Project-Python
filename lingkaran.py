def luas_lingkaran():
	jari_jari = int(input("Masukan jari-jari lingkaran: "))
	luas = 22/7 * (float(jari_jari) ** 2)
	print("Hasilnya adalah : ", luas)
	return luas

def keliling_lingkaran():
	jari_jari2 = int(input("Masukan jari-jari lingkaran: "))
	keliling = 2 * 22/7 * float(jari_jari2)
	print("Hasilnya adalah : ", keliling)
	return keliling

while True:
	print("====== SELAMAT DATANG DI PROGRAM LINGKARAN ======")
	print("Berikut adalah menu yang tersedia:")
	print("1. Mencari luas Lingkaran")
	print("2. Mencari keliling Lingkaran")
	print("3. Batal")
	option = input("Option 1-2 : ")
	if option == "1":
		print("Anda Pilih Menu 1: ")
		luas_lingkaran()
	elif option == "2":
		print("Anda Pilih Menu 2:")
		keliling_lingkaran()
	elif option == "3":
		break
	else: 
		print("Keyword Anda Salah!!, Anda bisa coba lagi!!")