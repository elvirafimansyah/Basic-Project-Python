def c_r():
    celcius = float(input("Masukan Suhu Celcius : "))
    reamur = (4/5) * celcius
    print("Suhu Reamur : ", reamur , "R")
    return reamur

def c_f():
    celcius1 = float(input('Masukan Suhu Celcius: '))
    fahrenhit = ((9/5) * celcius1) + 32
    print("Suhu Fahrenhit : ", fahrenhit, "F")
    return fahrenhit

def c_k():
    celcius2 = float(input("Masukan Suhu Celcius: "))
    kelvin = celcius2 + 273
    print('Suhu Kelvin : ', kelvin, "K")
    return kelvin

def f_k():
    f = float(input('Masukan Suhu Celcius:'))
    k = 5/9 * (f-32) + 273
    print("Suhu Kelvin : ", k, "K")
    return k

def k_f():
    k2 = float(input("Masukan Suhu Kelvin: "))
    f2 = 9/5 * (k2-273) + 32
    print("Suhu Fahrenhit : ", f2, "F")
    return f2

def f_c():
    fah = float(input("Masukan suhu Fahrenhit: "))
    c3 = (fah - 32) * 5/9
    print("Suhu celcius: ", c3, "C")
    return c3

while True:
    print('=== PROGRAM KONVERSI TEMPERATUR ===')
    print("\n1. Celcius -> Reamur\n2. Celcius -> Fahrenhit\n3. Celcius -> Kelvin\n4. Fahrenhit -> Kelvin\n5. Kelvin -> Fahrenhit\n6. Fahrenhit -> Celcius\n 7. Tutup")
    option = input("Option 1-4 : ")
    if option == "1":
        print('Anda Telah Memilih Option 1 (Celcius -> Reamur)')
        c_r()
    elif option == '2':
        print('Anda Telah Memilih Option 2 (Celcius -> Fahrenhit)')
        c_f()
    elif option == '3':
        print('Anda Telah Memilih Option 3 (Celcius -> Kelvin)')
        c_k()
    elif option == "4":
        print('Anda Telah Memilih Option 4 (Fahrenhit -> Kelvin)')
        k_f()
    elif option == "5":
        print('Anda Telah Memilih Option 5 (Kelvin -> Fahrenhit)')
        f_k()
    elif option == "6":
        print("Anda telah Memilih Option 6 (Fahrenhit -> Celcius)")
        f_c()
    elif option == "7":
        print("Anda Telah Menutup Program!")
        break
    else: 
        print("Keyword Anda Salah, Silahkan coba lagi!!")