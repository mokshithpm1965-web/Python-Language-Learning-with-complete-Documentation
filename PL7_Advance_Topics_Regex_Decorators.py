#REGULR EXPRESSIONS(Regex)
#Regex is used to search ,match and validate pattern  in text
#For Example
#check the emaol address is vcal;oid
#check if a phone number has exactly 10 digits
#Find all numbers in a sentence
#Search for spevcific words in a file
#to use regex  in Python  we import the re module
import re
#ex: re.search()
import re
text="I LOVE python"
result=re.search( "python",text)#searches for the first occurence  of the pattern in the text
print(result)#if fond returns a match object else not
result =re.search("JAVA",text)#none java is not present
print(result)
# python uses end -exclusive indexing if 16 then consider it as 15 same idea usd for slicing  text[0:5]
import re
text="Electronics and Communication"
result=re.search("Communication",text)
print(result)

import re
text="Python Java c++"
result=re.search("Java",text)
if result:
     print("Found")
else:
m    print("Not Found")
 
# output is stored in result if   object is mtched  when doing sercjh thyen python conside it a strue   no match result  contains none

****************
#re.findal
#re.findall() searches the entire string and returns all matching occurence as a list
import re
text=" apple banana apple mango"#re.findall searches the whole string it finds apple twice ,so it returns a list containing all matches
result=re.findall("apple",text)
print(result)


import re
text=" flight   car  jeep bike flight"
result=re.findall(" flight",text)
print(result)
#re.search() returns only the first match
#re.findall() searches the entire string

#using for loop converting list to string
import re
names=["Joseph","Jack","mangifera","Marriage"]
for name in  names:
    result=re.findall("Jack",name)
    if result:
        print(result)

#Another way  to convert list into one string
 text= " ".join(["jospeh", "jack", "lena", "Marriage"])
 result=re.findall("lena",text)
 print(result)
 #here join () function i used to combine  a sequence  of strings  into one single string  with specified separator
 # here you have a list of ["jospeh", "jack", "lena", "Marriage"] , the join takes the listand cobines them into a one string
 # after this, txt  is a single  strimng "joseph jack lena Marriage"
# so it is not that re.findall() only works with a for loop ,a for loop is just way to give it strings one by one
#the main rule :
re.findall() -input must be string (or bytes), not a list/tuple directly


**********************


#re.sub()
#re.sub(0 means substitute(replace)
import re
text="I like Java"
new_text=re.sub("Java","Python",text)#RE.SUB(OLD ,NEW,TEXT)

print(new_text)

import re
text="red green red blue"
result=re.sub("red","yellow",text)#re.sub() replaces all occurrences of the pattern by default
print(result)

import re
ex=["I" ,"like", "java"]
for i in range(len(ex)):
    ex[i]=re.sub("like"," new ",ex[i])# we use ex[i] to serch an change  the string in ceratain posityion and again we use same ex[i]  to strore that sreing in certain position
for  result in ex:
             print(result)
#key difference is  that re.findall() returns  a l;ist of all matches ,but it doesn't change the original string
#it just extracts what uou asked for  but re.sub() returns a new  string with with replacements ,but it doesn't modify  the original list  or string unless
#you  explecitly assign it
# why is len|(ex)
# len(ex) simply returns the number of elements  in the list ex.so if you have say three strings in ex ,len(ex)
 will be 3 this is uesful because  you wantr to loop over all the items in the list by their index
# what is ex[i]
#ex[i] means you are accesssing the element at poision i inthe list ex.For example if i=0,then ex[i] is the first string  in the list,if 1 then it will be  second
#why use ex[i]= re.sub- the reason we assign ex[i] is that we want to update  the original list  when re.sub() returna a new string it sodes'nt alter the list directly ,so we store that new string back into ex[i],in short
 3 we are replacoing  the old  value  in the list with the updated string.Without this assignment the list woul   df stay same
 #result is tjhe temp[orary varaiable there  ,it stroes the returned string  from re.

 *******************
 
#DECORATORS
#this is one of the  advanced python cocepts and is commanly asked in interviews
#A decorator is afunction that adds extr functionality to another function without changiging its original code
#for an example3You have a bike .You add a helmet.The bike doesn't chnage but you add extra safety
#similarly a decorator adds extra behavior to a function
# example
def decorator(func):#func is the function we want to decorate (greet)
    def wrapper():#wrapper is anew function
        print("Before function")
        #runs before greet()
       func()
        #calls the original function(greet())
        print("After function")
        #Runs after greet()
    return wrapper# Replace the old function with this new function that has extr features
   #Returns the new function
@decorator
def greet(): #greet=decorator(greet)
        print("Hello")#Python automatically decorates the greet()function
greet()

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper#we are returning the function itself
#That means Python replaces thye original  functionj with the wrapper
@decorator
def test(): #here python does test=decorator(test)
    #test is sent to decorator() as  func
    #decorator () creates the wrapper function
    #decorator() returns wrapper
    #now
    #test=wrapper
    #so after decoration ,test is no longer the  og function
    #it now refers to wrqapper
    #the original function doesnt change the decorator simply adds code before  and or after it
        print("python")
test()
************************
#map() function
#map() is used to apply  the same function to every elemnet in a  list(or another iterable)
#example
numbers=[1,2,3,4,5]
result=list(map(lambda x:x*2,numbers))
print(result)

#filter# this is used to select only those elemnts that satisy the condition
numbers=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,numbers))
print(result)

#zip()
#it is used tocombine two or more lists elemnt by elemt
names=["ram","Shyam","Mohan"]
marks=[85,90,95]
result=list(zip (names,marks))

print(result)#zip() pairs the first elemnt with the first elemnt the second with the second and so on
fruits=["apple","Mango"]
prices=[50,50]
print(list(zip(fruits,prices)))# we get outputr in tuple min list
#python uses a tuple because  a tuple is immutable(cannot be changed).Once the pair is created ,it stays together

#enumerate()
#enumarate() is used when you want both the index and the value while  looping through a list

#Example

fruits=["APPLE","BANNANA","MANGO"]
for index , fruit in enumerate(fruits):
    print(index,fruit)#starts from m0,1,2,3,4,5......
#first value index ,secpnd value fruit, now look at this part
#for index,fruit  python takes the first pairrrrrrr as (0,apple) index=0,fruit=apple

#you get both indexd and values
colors=["Blue","red", "orange", "yellow","green"]
for index, color in enumerate(colors):
    print( index ,color)

colors=["Blue","red","violes","green","maze"]
for i , color in enumerate(colors):
         print(i,color)# color represents the current  element of the list  not thewhole list
         # for example
         #first iteration-color ="red"
         #second iteration -color="Green"
         #third iteration -color ="blue"
         #it can be used for list , dictnories,set,tuple,string

***********************************
         
#*args and **kwargs
*args  (10,20) ,( a tuple of positional argument)
**kwargs {'name','Moksh','age':20}( a dictionary of keyword arguments)
         #these are used when a function needs to accept any numbers of arguments

#*args
#*args allows a function to accept any number of positional arguments
         #Example
         def add(*numbers):
             print(numbers)
         add(10,20,30)
# Notice the output uses parentheses()
#why?
#Because *args stores all the arguments in atuple
*numbers in the function dfinition -collect values into atuple
numbers in print - use thetuple as its, to store the values as a tuple
**numbers in print- unpack the tuple and send each value separately
#anothe example

def add(*numbers):
    print(sum(numbers))
add(10,20,30)

#we use *args because
#if we write
def add(a,b):
     return a+b
    #this accepts only 2 numbers
    #but what if you want
    # add(10,20,30)
    #or
    # add(10,20,30,40,50)
    

def show(*names):
    print(names)
show("Ram","shyam","Mohan")          
# Python doesnt use a tuple because it is immutable ,rather *args is designed by python to collect positiuonal
#arguments into atuple,Tuples are agood choice because they are lightweight and  presrve the order of the arguments
#what are the positional Arguments
#A positional argument is an argument whose value is assigned based on its position

#for an example
def student(name,age):
    print(name)
    print(age)
student("Mokshith",20)
#output
#Mokshith
#20
#Here:
#"Mokshith" is assigned to name because it is  in the first position
#20 is assigned to age because it is in the  second position
#these are called positional arguments

##witrh *args
 def show(*numbers):
     print(numbers)
show(10,20,30,40)
#output will be
#10-first,20-second,30- third-40-fourth
#args collects all p[ositional arguments into one tuple

def demo(a,*b):
    print(a)
    print(b)
demo(5,10,15,20)
#An argument is the actual value you pass to a function when calling it

#in programming language ,a number starting with 0 was trditionally used to represent octal numbers
#because octal digits only go from 0 to
#if we want it in octal write like print(0o11)

#**kwargs
#**kwargs allows a function to accept any number of keyword arguments

#a keyword argumnet is an argument passed using its parameter name
def student(**details):
    print(details)
student(name="ravi", age=20)
#the output  uses curly braces {}
#because **kwargs stores the arguments as a dictionry
# why it is  called a keyword argument
#example:
#name:="Mokshith", age=20#name and age refers to keyword argument
#*args-Stores positional arguments in adictionary
#**kwargs -Stores keyword arguments in adictionary
def info(**data):
     print(data)
info(city="Puttur", state="Karnataka") 3 q dictionary stroes data as key-values pairs

def demo(**b):
   # print(a)
    print(b)
demo(nam="dvhcb", age=22, usn=122311221133 ,clg="kvg" , gf="no")
    # for only keyword argument

    def demo(a, **b):
    print(a)
    print(b)
demo("dvhcb", age=22, usn=122311221133 ,clg="kvg" , gf="no")
#a=positional argument
#b =keyword argument
##python looks nfor a , so you need to give  in print stament

******************************
    
#__name__=="__main__"
#This is used to check wheather  Python file is being run directly or imported into another file
#Example
def greet():
    print("Hello")
if __name__== "__main__":#if this file being executed directly ,run the code inside the block
        greet()
        #so the condition becomes if "__main__"=="__main__" # for this progrm its true and prints Hello becuase it is in the same file 
#if this file is imported into another Python file,
#the code inside this if  block will not run
#this is useful because you may want a file to;
        #act as a program when run directly
        #Act as a module when imported into another program
        # if we do


def greet():
        print("Hello")
if __name__ =="__main__":
        greet()
        #this is for  demp.py

#file 2:main.py
import demo
print("welcome")
#now if you run main.py the correct output is\
#welcome
#why?
#when main.py imports demo.py
import demo
#Python sets
__name__="demo"
#inside demo.py not ""__main__"
#so th condition is
#if __name__ == "__main__":
#  becomes
#if "demo"== "__main__":
#therfore greet is not called
#only prints  welcome
# if demo.py and main.py are in the same folder ,then:
import demo
# not  works perfectly
#name  ia built in variable in Python.It tells Python the name of the current file or module and how it is being used
#Run this code only if this file is the main else not
#if
print("Start")# it prints start mpython  imports demo but not main so its false main is not printed
#then python continues to execute remaning n top level code
if __name__= "__main__":
    print("Hello")
print("end")
#this is in demo.py
#in main.py
#if we call
# then output is start  and end
#if the nme is not equal to main it  doest not prints the statement below the conditiopn but   oit still executes all the other top -=level code
#import demo
#we use this __name__ =="__main__"
#suppose demo.py has 100 functions
#you wnt to reuse those functions in other prograns because below the statement it doesn't executes 
# if thete were no if_name_=="__name__ :, block then every time you import demp.py  kit would automatically run automtixcally all its test code
#thats what e want

#so we write
#if_name=="__main__"
#run this code only if this file is executed directly, not whenits is imported           



#assert   CC
#the assert statement is used to check whether  a condition is True
#if the condition is True ,the program continues
#if the condition is False ,Python raises an AssertionError
age=20
assert age>=18
print("Eligible to vote")
age =15
assert age >=18
print("Eligible to vote")

#pip(PYTHON PACKAGE INSTALLER)
#what is pip?

#pip is atool used to install,update,and remove Python package(libraries)
# for an example
#Python is your mobile phone
#Packages are the apps
#pip is the playstore that installs those apps
# if you want to use
#numpy-mathematics
#pandas-Data analysis
#opencv-Computer vision
#requests-Internet requestts
#you intsall them by using pip
#for an example
#open copmmand promt or terminal and type
#pip install numpy
#after installation ,you can use it in Python
#import numpy

#pip install opencv-python
#then use it
import cv2
 #useful pip Commands
#install package
pip install pakage_name
#example
pip install requests
#update pip install  --upgrade requests
#pip uninstall requests

#VIRTUAL ENVIRONMENT(venv)
#Avirual environment is an isolated python environment for a project
#This means each project can have its own packages and versions without affecting other projects
#why dowe need it
#project a needs numpy version 1.24
#project b needs numpy version 2.0
#withoput a virtual enviroment,both projects use the same python installation ,causing version conflicts
#with a virual enviroment each project has its own separate packges
#How to create a virtual enviroment
#open Command prompt and type
#pythom -m venv myenv
#This createsa a virtual enviroment named myenv
#to activate itr on windows
#myenv\Scripts\activate
# you'll see something like:
(myenv) c:\users\....
#Now ,if you install a package
pip[ install numpy
#it is installed only inside myenv,not gobally

**********************************

 #Global variable
# A global variable is avariable created outside any function
x=10
def show():
    print(x)
show()
print(x)
#10- inside the function, 10- outside the function , global variable can be accessed  by inside the function also


#Local variaavble
#A  local variable created inside a function
 def show():
     x=103 after the xecution completes  that x i removed becaus ex is local to the function
     print(x) 3 x exists only inside show()
 show()
Global variable- Notice board in the college hallway
#everyone can see it
#local variable  -notes inside your classroom  note book
#only available inside btht classroom

#eXamples:
name ="Moksh"
def student():
    age=20
    print(name)
    print(age)
student()
print(name)
print(age)
     
#one more thing if you want to mnodify  a glovbal variable inside a function you need the glopbal keyword
x=5
def change():
    global x #this  tells python the x I am going to use inside function  is the same global x , not a new local variable
    x=10
    change()#The function rujns and changes x
    print(x)
    #without global, Python  creates a new local x instead of changing the global one
 
x=5
def change():
    x=20#-pythgon thinks it is thge variable only belongs to this function
change()
print(x)
















 






















































                  


        
        

        





