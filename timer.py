# must use import time
import time

# input data about How many a second for set timer ? 
timee = int(input("Enter e Second for set timer : "))

#set timer code
for x in range(timee):
    print(str(timee - x) + " seconds remind")
    
    # we need time.sleep() because for 1 second between each iteraction
    time.sleep(1) #parameter 1 untuk menghitung mundurnya detik setiap 1 detik
    
print('Timer has Over !');
