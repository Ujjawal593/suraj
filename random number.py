import random
a = random.randint(1,100)
b = int(input("please enter your number "))
if b<a :
        print("your number is less than",a)
elif a<b :
        print("your number is greater than ",a)
else :
        print ("your number is equal to ",a)
