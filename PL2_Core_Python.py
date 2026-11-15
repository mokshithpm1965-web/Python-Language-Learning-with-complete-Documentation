'''
#DICTIONARIES
#IT STORES DATA  IN KEY:VALUE PAIRS
#IF WE THINK LIKE REAL DICTIONARY THEN ;
#WORD- MEANING ,KEY-VALUE
student={
    "name":"svcddfj",
    "age":10,
    "cgpa" :20
    }
print(student)
#if we want to acees the values
print(student["name"])
#to change values
student["age"]=50
print(student)
print(student["name"]="moksh")#we cant to this because both print and assigning operations are differentgggggggg
#to add new value to student
student["COLLEGE"]="KVGCE"
print(student)
#loop through the dictionary
#items() is a method of a dictionary,it tells python give me all the key-value pairs in the dictionary
#each pair is atuple b bbb
for key,value in student.items():
    print(key ,value)
#home work
MYbio={
    "name":"Mokshith PM",
    "age":20,
    "Favorite bike":"Royal Enfield"
    }
print(MYbio["name"])
print(MYbio["age"])
print(MYbio["Favorite bike"])

*******

#FILE HANDLING
#THERE ARE TWO TYPES READING FROM FILES AND WRITING INTO FILES
#THIS IS HOW PROGRAM SAVE DATA PERMANENTLY
#1. WRITING TO A FILE
file=open("demo.txt","w")
file.write("Hello python")
file.close()


#READING FROM THE FILE
file=open("demo.txt","r")
content=file.read()
print(content)
file.close()

#Append mode
file=open("demo.txt","a")
file.write("\nis good language")
file.close()

#file=open("demo.txt","r")
#print(file.read())

#content=file.read()
#print(content)
#file.close()

#file = open("demo.txt","a+")
file.write("is good  looking")
file.seek(0)
content=file.read()
print(content)
file.close()
#when you open a file in a+ mode python places th file pointer at the end of the file becuase you are appending
# if you immedatley call file.read there is nothing left to read so you will get an empty string
#that's why we usee seek here
#a file pointer is the current position inside a file from which will read or wite next

#BETTER MODERN WAY WITH WITH
with open("demo.txt","r") as file:
    print(file.read())
#your dada may not be saved immediately becuase when you are writting python often  keeps the dat in atemporary memory area
#before writing it to the disk
#The file stays open -that may lead to decrease  os speed
#other programs may have trouble accessing it -another program  cant modify or delete the file when your program still ha it open

    ********
#CLASSES AND OBJECTS(OOP)
#CLASS IS THE BLUPRINT
#OBJECT IS THE REAL THING THAT IS CREATED BY THE CLASS
class Student:
    def details(self):
        print("This is a student")
s1=Student()
s1.details()
#()-this tells to run the function
# print(s1.name())-if we do this theree is no return statement to this

#CLASS WITH VARIABLES
class Student:
    def __init__(self, name,age):
        self.name=name
        self.age=age
s1=Student("Mokshith", 21)
print(s1.name)
print(s1.age)
s1.name
s1.cake
#string cant be cslled as function


class Bike:
    def __init__(self,brand ,color): __ this is called double unfderscores or informally dunder
       self.brand=brand
       self.color=color
s1=Bike("Royal Enfield", "dapper greay")
print(s1.brand)
print(s1.color)
#class-blueprint
#object-actual item
#variable-properties
#method-actions/functions
#__init__- is a special method (called a constructor) thta is automatically executed when an object of a class is created
#it is used to initialize the object's attributes(variables)

'''
#HOME WORK
class Car:
    def __init__(self,brand, color):
        self.brand=brand
        self.color=color
s1=Car("BUGATI","BLACK")
print(s1.brand)
print(s1.color)

    
    

