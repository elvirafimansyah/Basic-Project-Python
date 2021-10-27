def add(a, b):
    add = float(a) + float(b)
    return add
def sub(a, b):
    sub = float(a) - float(b)
    return sub
def mult(a, b):
    mult = float(a) * float(b)
    return mult
def div(a, b):
    div = float(a) / float(b)
    return div

while True:
    print("========== SIMPLE CALCUALTOR ==========")
    a = input("Enter First Number: ")
    b = input("Enter Second Number: ")
    print("\n1. Add\n2. Substract\n3. Multiply\n4. Divide\n5. Close")
    option= int(input('Option 1-5: '))
    if option==1:
        print("The Result is: ", add(a, b))
    elif option==2:
        print("The Result is: ", sub(a, b))
    elif option==3:
        print("The Result is: ", mult(a, b))
    elif option==4:
        print("The Result is: ", div(a, b))
    elif option==5:
        break
    else:
        print('Invalid Input')