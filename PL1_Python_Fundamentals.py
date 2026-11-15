 #printing  name class name clg name etc
name="Mokshith PM"
Class= 4
age =20
print(name)
print(Class)
print(age)

#lets us to have user vtgive values
name=input("Enter your name: ")
print(name)

#let us try with numbers
age=int(input("enter your age: "))
print(age)
/
#home work my name my cgpa, my age
name=input("Enter tyour name:")
age=int(input("Enter your age: "))
cgpa=float(input("Enter your cgpa: "))
print(name)
print(age)
print(cgpa)

#operations using python
a=2
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)


#comparison operators
a=2
b=2
print(a>b)
print(a<b)
print(a==b)
print(a!=b) 
print(a<<b)-yhis is shifting (left shift) - multiply by 2
print(a>>b)-this is right shift divide by 2
#home work
a=4
b=8
print(a+b)
print(a*b)
print(a>b)

    # AND IS ALOGICAL OPERATOR
    #it works withtrue and false values
    #& is a bitwise operator .it works on the binary bits of integers
    for example 1:
    a=5
    b=10
    print(a>10 and b>5)
    #ans is true or faslse
    #example 2
    a=5
    b=3
    print(a&b)
    binary values:
    5=101
    3=011
      001
       output=1
       #but why do they give same results
       #this happens because in Python ,True is represented  internally as 1 and faslse as 0
       #but they behave differently in many cases
       for example print(5 and 3)- ourtput is 3 -based on true or fasle
       #where as print(5&3)-output 1 -because it performs a bit by bit and operation

       #we use or ,and operations based on the situations
  

#if else statements

a=10
b=0
if a>b:
    print("a is greater")
else:
   
marks =80
if marks>=80:
    print("Grade A")
elif marks>=75:
    print("Grade A")
elif marks>=50:
    print("Grade A")
else:
    print("Fail")
 
#logioal operators
#both conditiuons must true
age=20
if age>=18 and age <=25:
    print("Eligible")
    
#atleats one condition is true
age =61
if age<18 or age>60:
    print("Special Category")
    
    ******

#not, reversestrue or false
#it just reverse the boolean value
#if you are a student then print true
#else not
#it is just flipping of true to false or vice versa

is_Studen9t =True
if not is_Student:
#or you can write
if is_student==False:
     print("Not a student")
     
age=int(input("Enter your age:"))
if age>=18:
    print("Eligeble for voting")
else:
    print("You'r not eligeble")
    
age=int(input("Enter your age:"))
if age >=18 | age <=25:
    print("Young adult")
else:
     print("No")
     
     ********

#WHILE LOOPS AND FOR LOOPS
#while loop must have a condition
#If the condition never becomes False ,the loop runs forever
#to stop press ctrt+c
# to print a nam ewithout any copndition we use
while True:
print("Mokshith")
count =1
while count <=5:
    print(count)
    #count=count+1

#list is a class
#str is a class
#int is a class
#range is a classe
#they are blue print to create the objects

*******************
#FOR LOOPS
for i in range(5):
     print(i)

     ##
     for i in range(5):
       print(10)#to print same number
     
#WECAN GIVE RANGE TO IT
#range(start,stop, step)
for i in range(1,6):
    print(i)

#REVERSE LOOP
#WE CAN USE  FOR LOOP FOR REVERSE COUNT
#here -1 indicates the gap
for i in range(10,0,-1):
    print(i)
    
num=int(input("Enter number: "))
for  i in range(1,11):
    print(num, "x",i,"=",num*i)
    #comma is used to manintain starting of the next unction or values
    
#home work for even numbers
for i in range(1, 21):
    if i%2==0:
        print(i)
        
#to print plain text
for i in range(4):
    print("****")
    # range is designed to  genetare a sequence of numbers ,not text
    #if you want loop of sting
    #then
 for letter in"Mokshith":
     print(letter)
#for prints letter separatly
    ****************
    
#FUNCTIONS
#IT HELPS US TO REUSE THE CODE
#function with parameter
def greet(name):# it is a keyword in python  it stands for define 
    print("Hello" , name)#greet-the name of the function
greet("Rahul")-this calls the function and passes rahul as the argument
# name-a parameter it is a variable  that receives the value you pass

def greet(name):
     print("Hello",greet)-shows the memory  of function greet stored in hexa decimal value
     
#function with return value
def add(a,b):
    return a+b
result =add(2,18)
print(result)

#HOME WORK
def square(a):
    return a*a
result=square(18)
print(result)

#lists
#what is lists
numbers=[12,45,11,34]
print(numbers)
#CALLING A NUMBER OR PRINTING A NUMBER FOR LIST
print(numbers[1])
#changing a value or number from the list
numbers[1]=59
print(numbers)
#ADDING THE VALUES OR  NUMBER TO THE LIST
numbers.append(24)
print(numbers)
#LOOP THROUGH THE LIST
for i in numbers:
    print(i)
#Homework
bikes=["ROYAL ENFIELD", "KAVASAKI","DUGATI","BMW","HERO"]
for i in bikes:
    print(i)
    
#strings
name="Mokshith PM"
print(name)
#string indexing
print(len(name))
#CONVERT TO UPPER CASE3
print(name.upper())
#convert into lower case
print(name.lower())
#checking text
message=" hello Python"
print("Python" in message)
#sTRING CONCATENATION
first="Hello"
second="world"
print(first +"  " +second)
print(name + "   " + message)
#loop through the string
name = "Python"
for i in name:
    print(i)
#homework
name="Mokshith PM"
print(len(name))
print(name.upper())
print(name.lower())
for i in name:
    print (i)
strings are immutable ,once  a string object is created , its charecter cannot be cahneged
append on strings  does not works we  can't add cahrecters to  existring strings

    
    
