import math
import random

n= random.randint(0, 100)
print (f"The number computer chose between 0 and 100 is :" , n)

def fizzbuzz(n):
    if n %3 == 0 and n%5 ==0 :
        print("and It returns :FizzBuzz")
    elif n%3 ==0 and n%5 !=0:
        print("and It returns :Fizz")
    elif n%5 ==0 and n%3 !=0: 
        print("and It returns :Buzz")
    elif n%5 !=0 and n%3 !=0:
        print ("and It returns :", n)


fizzbuzz(n)