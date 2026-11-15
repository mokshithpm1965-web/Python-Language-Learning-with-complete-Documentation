'''
EXCEPTION HANDLING#It is the basixcally error  that happens while the program is running
 for example
print(10/0)# cause you division by zeero error
to avoid this we use error handling method

we use TRY and  BLOCK method
try-something goes rong ,dont crash yet

try:
    print(10/0)
except ZeroDivisionError:
        print("You cannot dived by zero")

1
try:
     age=int(input("Enter you age:"))
     print(age)
except ValueError:
         print("Please enter numbers only,")
         
 1

#use of else statement in error handling
try:
     num=int(input("Enter your number"))
     print(100/num)
except ZeroDivisionError:
     print("cannot divisible by zero")
except ValueError:
     print("enter a correct value")
else:
     print(" no issues")


#use of finally code-its a block of code that always runs,wheather an error happens or not
try:
    print("Program started")
    print(10/2)
except ZerodivisionError:
        print("cannot divide by zero")
finally:
    print("program is ended")
    #professionals use finally because if any error hapes it prevemnts resources from being open
    #  #it can also used because for  closing database connections, releasingn network connections,unlocking resources
    #stopping timers or background tasks
    #for example
    #for example
    file =open("demo.txt","r")
    try:
         print(file.read())
    finally:
         file.close()
         

*************    
#modules
#A MODULE IS SIMPLY  PYTHON FILE(.PY) THAT CONTAIMS CODE YOU CAN  RESUSE IN OTHER PROGRAMS
#code(functions ,classses,variables)
import math#built in module
print(math.sqrt(25))
print (math.pi)
print(math.factorial(5))
import random#another module
print(random.randint(1,10))

#creating your own module in python
#Different ways to import modules
import math
print(math.sqrt(25))
#method1- import the entire module in python
import math
print(math.sqrt(36))
print(math.factorial(5));
#method2- import only the function you need
from math import sqrt
print(sqrt(36))#just  sqrt()function
#method3 import multiple functions
from math import sqrt, factorial
print(sqrt(29))#method4 give the module a nickname(alias)
import  math as m
print(m.sqrt(81))
#for professional  ai and datascience we use import numpy as np and import pandas as pd

***************
#Packages- a package is a folder that contains one or more python modules
#module= one .py file
#package= A folder containing multiple .py files (modules),
#inside  a package you may see __init__py,years ago, python required this file to recognize a folder as a package .
#Today(pathon 3.3+), oit is often oiptional ,butt many professional projects still include it,,,,,,,,,,,,,,,,
#for an example
#-doctors -package, cardiologist -modulle
then if cardiologist .py contains
def check_heart():
     print("Heart is healthy.")
    # then you can write
    #we use () because to indicate tht function takes parameters an empty() says that function doesnt has parameters
    from doctors.cardiolost import check_heart
    check_heart() notice that dotr(.) it means go inside the package and acess this module,,,,,,,,

    from shine import  car,bike
car.car_color()
bike.bike_color()
#go to the module car run the function  car_color
# when we  have to assess different modules of same packages
# here car is the function
#instead of underscrore we can also write this
def car():
pass
def carcolor()
pass
def car_color():
pass
#but of ten python programmmers use naming style called as snake_case

    ,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
