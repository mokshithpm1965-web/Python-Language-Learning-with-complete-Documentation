#lesson 23-Polymorphism
#the word Polymorphism comes from many forma, it means one the can have many forms
#Example
class Dog:
    def sound(self): #ha ssame method sound()
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
d=Dog()
c=Cat()
d.sound()
c.sound()

class Bird:
    def move(self):
        print("Flying")
class Fish:
    def move(self):
        print("Swimming")
b=Bird()
f=Fish()

b.move()
f.move()

class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
vehicles =[Car(),Bike()]
for v in vehicles:
      v.start()
      
#ENCAPSULATION
#LESSON 24
#encapsulation is the on eof the four piullers ogf ooops
#encapulation means keeping data and the methods that Work on that data together, while preventing direct access to important data
#think like atm deposite monet-withdraw money- check balace
#the atm poretects its data
class Bank:
    def __init__(self,balance):
        self.__balance=balance #__ two underscores this makes it a private attribute #that means don't access this variable directly from outside the class
    def deposit(self,amount):#instead of changing __balance directly ,we use amethod
        self.__balance +=amount#The class itself is allowed to acces its private data
    def show_balance(self):
        print(self.__balance)
b=Bank(1000)
b.deposit(500)
b.show_balance()#to see the balance we don't do
#instead we use b.show_balance()
#the method prints the balavce safely


class Student:
    def __init__(self,marks):
        self.marks=marks
    def show(self):
            print("Marks:",self.marks)
s=Student(95)
print("Before  changing:")
s.show()
s.marks=-500
print("After changing:")
s.show()

#now its not valide someone changed data


class Student:
    def __init__(self,marks):
        self.__marks=marks
    def show(self):
            print("Marks:",self.__marks) #here self.__init_- has original attribute to sotre
s=Student(95)
print("Before  changing:")
s.show()
s.__marks=-500#here it has new attribute to store
print("outside changing:",s.__marks)
s.show()#this method is use o show original attribute
# the cannot change the original mark


#lesson 25-Abstraction
#in encapsulatrion hide and protect your data
#in abstraction =hoide unnecessary implementation details and show only what the user needs
#example car# you start the car bur you dont need to know how engine works
#You only know how to use the car ,not how everything inside works
#this is called abstrction
#for an example

class Car:
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
c=Car()
c.start()#you dont care how the engine starts, you have only business with starting and stoippimng so you just call the function
c.stop()
#Encapsulation vs Abstraction
#WEncapsulation
#protects the dat
#3abstraction
#hides the complexity
#example clickinga a pic from aphoibne you dont have to know the inner process
class Fan:
    def turn_on(self):
        print("Fan is ON")
f=Fan()
f.turn_on()

#File handling
#file handlinfg allows your python program to store the data permanently
#yused in
#A Student management system
#A bnk appilication
# A librey management system
#opening the file
file=open("Student",'r')

#diff modes
r- read the file
w -write to the file  or overwrite the old content,create a file if doesn't exist
#a-append data to the end of the file  without deleting the exiusted data ,crete a file if doesnt exist
x-create a new file(fails if it already exists)
filke=open("marks.txt","w")
file.write("95\n") to write  one up and another in n line else it will write 9587
file.write("87")
file.close()


#read
file=open("marks.txt","r")
data=file.read()
print(data)
file.close()
#what will; be stored in the variable dat
#answer is  dat=file.read()
file.read()reads the entire file and stores it as one string
so if the  file contains 95
                         87
                         76
  we get "95
          87
          76"
#it is string nnopt three separate variable
#to check that
data=file.read()
print(type(data))
 if we want add any integer to string file we must do
 
data=int(file.read())
print(data+50)

#File handling readline()
Eread line sonly reads one line at a time
#suppose marks.txt contains
95
87
76
file=open("marks.txt","r")#python opens the file#->95|87|76 The arrow (->)shows the cursor position
line1=file.readline()#python reads only the first line
line2=file.readline()#now cursore mmoves to the second python reads the second line
print(line1)#prints line 1
#prints line 2
print(line2)
file.close()
# if there is extra readline then python  dooes not raises error but it create a empty string

 #READLINES
 #readlines
 file=open("fruits.txt","r")
 data=file.readlines() read-one string-readline one string line - readlines  all the lines
 print(data)
 file.close()
 #read lines out put is alist for example
 [ "Apple\n","Banna\n","Mango"]
 #Each lime is a separable string inside the list
 3 so type of data list if they ask type of data(for exqample 5 data's are present then its a string indside  list)

 #WITH OPEN
 #This is the recommended way to work with files un python
 files=open("marks.txt","r")
 data=file.read()
 print(data)
 file.close()
 #the better way of above program is written as
 with open("marks.txt","r")as#with says use the file only inside this with block so file.close is not needed
 file:
 data=file.read()
 print(data)
 #this does not require file.close(0 because when the with block finishes ,python automatically closes the file
 #why is with better
  with open("marks.txt","r")as file:
  data=file.read()
  x=10/0
  #the program crashes because of dision by zero
   if you used the old method:
   file=open("marks.txt","r")
   the file might ever get closed becayuse the program crashed before reachingf
   filke.close()
   #but with pytthon still closes the file automatically ,even if an error occurs
   #that's why professional Pythopn programmers prefer with open()


   #suppose the file contains python ,java,c++
   # program:
   with open("languages.txt","r") as file:
   print(file.readline())
   print(file.read())
 #first iit printes  python and the cursor will be starting point of the next line we get command read henxce it reads  java ,c++ so final output will be python,java,c++

#Writinfg Multiple lines
 with open("student.txt","w") as file
 file.write("Rahul\n")
 file.write("Anu\n")
 file.write("mokshith\n")
 #eachg writes one string and \n moves to the next line\



 3method 2:writelines()
 lines=["Rahul\n","Anu\n","Mokshith\n"]
 with open("student.txt","w") as file:
 file.writelines(lines)
 output
 Rahul
 anu
 Mokshith
 # writelines(_) does not automatically add \n you must include \n youserself if you wamnt each item on anew line


#SEEK()
#this is the most important pointer methods
#for an example file
Python
Java
C++
with open("language.txt" ,"r")as file:
print(file.read(6))
#output will be python noyw ciursor will e en dof the python
#now if you write
print(file.read())
#output will b java,c++
#because vcursor has already moved
#now comes seek()
with open("language.txt","r")as file:
print(file.read(6))
file.seek(0)
#means move the cursor back to position 0 (the beginning of the file)
#so the second read() starts from the begoining again output will be python,python,java,c++



#tell()
#tell() tells you the current position of the cursor
with open("language.txt","r")as file:
print(file.tell())#first output is zero 
file.raed(6)
print(file.tell())# noew cutrsor is at 6 amnd the tell gives position 6n        n 
#if we have 95
then tell  prints the cursor position
9-1charecter
5-1  charecter
\n -1 charector
total=3 charector
#read(2)- only reads two charecter
#append mode("a)
#add new dat vat the end of the existing file withoput deleting old data
Exmple;
#file contains  Rahul,Anu
with open("studentr.tgxtr","a") as file:
file.write("\nMokshith")
# after running Rahul,Anu,Mokshith|#The old dat remains .New dta is added at the end
#old data stys in append and old data is erased  in write



#craete mode(x)
#x means  create anew file,but don't overwrite existing file
with open("newfile.txt","x")as file:
file.write("hello_)


#Advanced Exception handling
#Multiple except blocks
#Habndling different errors separately
#Example
try:
   a= int(input("Enter number:"))
   b= int(input("Enter divisor:"))
   print(a/b)
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
#if the user enters "abc" - Value error
#if the user enters 0 as diovisor ZeroDivisionError



#2.Exception object(as e)
#instead of only printing a fixed message, we can get the actul error
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)#here e stores the exception message

#ValueError catches the error
#HCere e stores the actul error messahge 


#raise
#raise is used when we want to create an error ourselves
#eXAMPLE
age=-5
if age<0:
    raise ValueError("Age cannot  mbe negative")#Python normally accepts age=-5  but we decide that it is invalid and raise an error

#Custom  Exceptions
#creating our own exception class
#example
class InvalidAgeError(Exception):
    pass
age=-2
if age<0:
    raise InvalidAgeError("Invalid age")

#Multiple except Blopcks
#priviosly you learned
tey
#risky code
except:
    #handle error
    #But in real programs ,different errors need different solutions
    #for example:
    #Wropng input-ValueError
    #Divsion by zero - ZeroDivisionError
    # so we can use multiple except bl;ocks

 Example:
    try:
   a= int(input("Enter number:"))
   b= int(input("Enter divisor:"))
   print(a/b)
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
#Custokm  exceptions

3 for exam-ple a cust0omer tries to withdraw $10000 but their balance is only $5000
#we use our own exceptions like
#InsufficientBalanceError

class InsufficientBalanceError(Exception):
#creates anew exception cc;ass
        pass 
#means it inherits from pythons exception class
#use it
balance = 5000
withdraw = 10000
if withdraw > balance:
       raise InsufficientBalanceError("Insufficient balance")
#raise and insufficientBalaceerror must be in the same line
    

#Even better handle with try and except
class InsufficientBalanceError(Exception):
    pass
balance =10000;
withdraw=200000;
try:
    if withdraw>balance:
        raise InsufficientBalanceError("Insufficient Balance")
    print("Withdrawal successful")
except InsufficientBalanceError as e:
    print(e)
    
class InvalidAgeError(Exception):
    pass
age=-1
try:
    if age<0:
        raise InvalidAgeError("age xcannot be negative")
    print("Valid age") 
except InvalidAgeError as e:
    print(e)# e contains the message passed to the exception  (age cannot be negaative)

#Modules
#A module is simply a python file that contains functions ,variables or classes which can be module like:
#python already has built in modules like
#math,random,#datetime
# instead of wqriting everything yourself ,you import the module
import math
print(math.sqrt(25))
import random
print(random.randint(1,10))
#importing only the functions
from math import sqrt
print(sqrt(8))
import math
print(math.pow(2,3))#math.pow always returns float like 1.0
from math import sqrt
a=sqrt(81)
print(a)
from math import pow
print(pow(3,2))

#Alias
#sometimes module names are long ,so we give them ashort name
import math as m
print(m.sqrt(49))

from math import sqrt,pow
print(sqrt(64))
print(pow(2,4))


 #PACKAGES IN PYTHON
#module=one python file(math.py)
#Package= a folder that contains multip[le python modules
#My packages
#math_operations.py
#srtring_operations.py
#file_operations.py
#The folder MyPackage is called apackage
#Real -life example
#Think  of your college
#college-Package
#Departments-(ec,cs)=modules
#Students=Function/Classes
#uaing a package
#Calculator/
#>operation.pu
#>
def add(a,b):
    return a+b
    # we can use it like
    from Calculator.operations import add
print(add(5,3))

#examples for packages numpy,pandas

#Built in packages
#numpy- Mathemtics
#pandas- Data analysis
#matplotlib-Graphs
#sklearn-Machine Learning
def meow():
  print("meow meow")
from  Animal.cat import meow
meow()


#ITERATORS
#an iterator is an object that allows you t o access one element ata time from a collection a list ,tuple, or string
numbers=[10,20,30,40,50]
it=iter(numbers)#creates the iterator
print(next(it))
print(next(it))
print(next(it))#returns  the next element
#Generators(yield)
#This is very important topic it in troduces the yield keyword instead of return
#It is also main difference between
#return-returns the value once and the function ends
#yield-returns a value one at a time and remembers where it stopped
#Example

def numbers():
    yield 10#it creats a generator object
    yield 20
    yield 30
g=numbers()
print(next(g))#starts the functions afeter execution stops here
print(next(g))#it continues from where it paused 
print(next(g))
def demo():
    yield "A"
    yield "B"
g=demo()
print(next(g))
print(next(g))\

#Lambda Function
#A lambda function is a small anonymous (nameless)function
def add(a,b):
    return a+b
#you can write this in one line
add=lambda a,b:a+b
print(add(5,3))
#syntax lambda  arguments:exptression
#lambda -keyword
#arguments-inputs
#expression-what to return
#A lambda function automatically returns the result of the expression
square=lambda x:x
print(square(6))
#return  function contains namee but lambda is notx








      
    

    

  


    
 

















































 
 

 
 
          




















































