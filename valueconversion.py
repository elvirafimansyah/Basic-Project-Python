def predikat():
    print("========= VALUE CONVERSION =========")
    score = int(input("Enter a score : "))
    if (score <= 100 and score >= 90):
        print("Predikat A")
    elif (score <= 89 and score >= 75):
        print("Predikat B")
    elif (score <= 74 and score >= 50):
        print("Predikat C")
    elif (score <= 49 and score >= 0):
        print("Predikat D")

while True: 
    predikat()
    