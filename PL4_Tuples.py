#Tuples
#Tuples  are just like list but it continsd immutable typer of data
fruits=("Apple","Banana", "Mango")
print(fruits)
#list use  square brackets
#tuple uses parentheses()..
#can we change  atuple lets try
fruits =("apple","Banana","Mango")
fruits[0]="orange"
#we use tuples   for date bof births  like that should never accidentally change in your program
#and for days,months,gps coordinates ,rgb color values.
#ascessing tuples is similar top accessing lists
numbers=(12,23,33)
print(numbers[1])..
3tuples can contain  different data types  just like lists for example
student=("Mokshith",20,8.5,True)
print(student)...
numbers=(5,8,5,2,5,9)
print(numbers.count(5))
print(numbers.index(2))

 #Tuple packing  and unPacking
#tuple packing
 #suppose you write
student=("Mokshith",20,"ECE")
#THEN THIS IS THE TUPLE
#BUT PYTHON ALSO LETS  YOU WRITE
student="Mokshith", 20, "Ece"
print(student)
python automaticallty  pavcks these values into atuple
#this is called tuple packing'
#TUPLE UNPACKING
student=("qxsdvfg", 20,"ECE")
name,age,branch= student
print(name)
print(age)
print(branch)
#packing-put three items into one box(tuple)
#unpacking-take the three items back out into separate variable
#another exapmple
point=(10,20)
x,y=point
print(x)
print(y)
student=("Mokshith",20,"ECE")
name,age=student
#this gives an error because  there are 3 values but only 2 variables
a,b=(100,200)
print(a)
print(b)
#python unpacks tuple lile
a=100
b=-200

*********

#HERE IS SOMETHING INTRESTING
#PYTHON ALSO LETS YOU SWAP TWO VARIABLES WITHOUT USING A THIRD VVARIABLE
 #IN C++ ,YOU CAN WRITE
temp =a;
a=b;
b=temp;
#but in python 
a=10
b=20
a,b=b,a
print(a)
print(b
#This works because  python is using tuple pcking and unpacking behind scenes

*********

#Lesson 15.4 -Tuple Slicing
#just like lists and strings ,tuples support slicing
numbers =(10,20,30,40,50)
print(numbers[1:4])
#Starts from 1 and stop  before  index 4  note that slicing returs another tuple (20,30,40)
print(numbers[:3])
print(numbers[2:])
print(numbers[-1])
#negetive imdexing works same as it does for lists

********
# sets
#very imp python data structiure
numbers=[10,20,10,30,20,40]
#The numbers 10 and 20 are repeated  sometimes we dont want duplicate valueas
#this is when sets are used
#a set is a collection of unique values ,it automatically remove duplicates
numbers={10,20,10,30,20,40}
print(numbers)
#mutable
#unordered ,list and tuple are ordered
#uses
students={"Rahul","Mokshith","Rahul","Ajay"}
print(students)#does not allow repeatation in attendece list
#can we acesss a set by index?? no
numbers={10,20,30}
print(numbers[0])
#sets do not have indexes
#sets do not support item assignment

# adding an element
numbers={10,20,30}
numbers.add(40)
print(numbers)
#removing an element
numbers={10,20,30}
numbers.remove(20)
print(numbers)
#can we change an elemne
numbers={10,20,30}
numbers[0]=100

#not because they are immutable -they are actually mutable  but the reason is sets do not have indexes

  
#you can add  elememnts and remove elements but you cant acess or modify abn element by its position
#lesson 16.2 useful set methods
#1add
numbers={10,20}
numbers.add(30)
print(numbers)
#2remove
numbers={10,20,30}
numbers.remove(20)
print(numbers)
#discard()
#looks similar  to remove(),but there is an important difference
numbers={10,20,30}
numbers.discard(50)
print(numbers)
#no error id simply does nothing  
MM#QUICK SUMMARY OF ERRORS
SYNTAX ERROR-YOU WRITE INVALID PYTHON SYNTAX
NameError-You use a variable or function that doesn't exist
Type error-you perform an operation on the wrong data type
Value error-the data type is correct but the value is invalid(eg,int("hello"))m
ZeroDivisionError-You divide by zero
KeyError-You try to access or remove a key that doesn't exist
IndexError -you use an index that is out of range in a list or tuple


************

#LESSON 16.3-SET OPERATIONS

#this is where sets become really powerful
#imaginbe two groups of students
#GROUP A
A={ "Rahul","Mokshith","Ajay"}
#group b
B={"Ajay","Kiran","Rahul"}
#Now let's perform different operations
#1.Union(|)
#Meaning:Combine both sets without duplicates
A={ "Rahul","Mokshith","Ajay"}
B={"Ajay","Kiran","Rahul"}
print(A|B)
#2 intersection(&)
#Find the common elements
A={ "Rahul","Mokshith","Ajay"}
B={"Ajay","Kiran","Rahul"}
print(A&B)
#.Difference(-)
A={ "Rahul","Mokshith","Ajay"}
B={"Ajay","Kiran","Rahul"}
print(A-B)
print(B-A)
#Find elements that are in the first set but not in the second
#Find elements that are in the second set but not in the first
#Symmetrical Difference(^)
#elements that are in either set ,but not in both
A={ "Rahul","Mokshith","Ajay"}
B={"Ajay","Kiran","Rahul"}
print(A^B)
#LESSON 17

*************
#LIST COMPREHESIONS

#This is one of Python's most powerful features.It lets you write  shorter , cleaner and faster code
#consider normal method
numbers=[]
for i in range(1,6):
    numbers.append(i*i)
print(numbers)
#append is used to add one new item to the end of a list
#list Comprehension
numbers=[i*i for i in range(1,6)]
print(numbers)
#normal method had 3 stems ,creating a list,loop, append but na list comprehension  comprhends(building) the list in
#a single statement
numbers=[i for  i in range(1,6)]
print(numbers)
numbers=[i+10 for i in range(1,6)]
print(numbers)
numbers=[i*2 for i in range(1,6)]
print(numbers)











