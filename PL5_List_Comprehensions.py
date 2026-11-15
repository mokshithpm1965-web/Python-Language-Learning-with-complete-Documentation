 '''
#List Comprehension with if
#suppose you only want even numbers from 1 to 10
#Normal Method
numbers=[]
for i in range(1,11):
    if i%2==0:
         numbers.append(i)
print(numbers)
#append is used because you want to keep adding values to the list instead of replacing the old one
#List comprehension method
numbers=[i for i in range (1,11)
         if i%2==0]
# i for i means take each value of i and put it into the new list
#i*i for i means take each valu of i ,squre it|(i*i) and put the result into the new list
# the general syntax of list comprehension is:
#[expression for variable in iterable]
#the first i means  -whar should i add first
#the second i means the current value from the loop  
print(numbers)
numbers=[i*i for i range(1,11) if i%2==0]
print(numbers)
*********

#Nested List Comprehensions
#lesson 17.3
#nested means one loop inside another loop
#normal method
#suppose we want all possible paoirs of numbers:
(1,1)
(1,2)
(2,1)
(2,2)
we write

pairs=[]
for i in range (1,3):#outer loop
    for j in  range(1,3):#inner loop
        pairs.append((i,j))
print(pairs)
#first i=1,j=1 then i=1;,j=2then i=2,j=1, then i=2,j=2
append()takes one argumnet we use(()) ,to tke two argumentrs,creating the tuple  inside the function call
# append() is designed to add   only one element at a time to a list,hence tuple is used to grop the elementys in to single pairs
#outer loop controls  the big cycle and inner loop controls the smalll cycle
#the inner loop finishes its entire  cycle before i changes
#The inenr loop (j) is completely executed for each single value of the outer loop(i)

#Now the  same program using a nested list comprehension
pairs=[(i,j) for  i in range(1,3) for j in range(1,3)]
print(pairs)


pairs=[(i,j) for i in range (1,3) for j in range (3,5)]
print(pairs)


#Lesson 17.4- List  Comprehension with an if ...else
#Suppose we want a list where:
#if the number is even,store "Even"
#if the number is odd,store "odd"
#Normal method:
result=[]
for i in range(1,6):
    if i%2==0:
        result.append("Even")
    else:
        result.append("odd")
    print(result)
    
#List comprehension version:
result=["Even" if  i%2==0
         else "odd" for i in range (1,6)]
print(result)
#In a list comprehension the if .... else comes before the for loop
#this is different from the previous lesson where we only had an if filter after the forv

**************

#lesson 18.1 - what is a Lambda Function
#lambda function is  a small function without a name
#normally ,we create functions using def
#for example
def square(x):
    return x*x
print(square(5))
# using lambda we can write same program as
square=lambda x:x*x
print(square(5))
#square used as avariable to store lambda
#lambda -key to small  not named function
#we use this to simplify length
multiply=lambda x: x*5
print(multiply(5))
add= lambda a,b: a+b
print(add(2,3))
#lambda can take several parameters more than one like a,b,c
lambda x:
    peint(x)
    return x*2
#we get error cause a lambda function can contain only one expression.it cannot  contain multiple statements like print() and return
#def -can have many  lines of code
lambda- Only one expression
lambda automatically returns the expression ,so you don't write return
lambda x:x*x- lambda automatically   returns the function not need to write return
'
******************
#Real power of lambda function
#map()
#filter()
#reduce()
#map - the map function is used  when you want to apply the same operation to every  item in a list,tuples,sets,other iterable objects
#Noraml method
#suppose  we have a list
numbers=[1,2,3,4,5]
#if we want to double every number
numbers=[1,2,3,4,5]
result=[]
for i in  numbers:
    result.append(i*2)
print(result)
#using map function we can  write it as
numbers=[1,2,3,4,5]
result=list(map(lambda x: x*2,numbers))
print(result)
# we use list(map())-because map() does not directly give a list
#It gives a special object called a map object
#to see the val;ues as a list we ,write -list(map())
numbers=[2,4,6]
result=list(map(lambda x:x+5, numbers))
print(result)

#lkesson 18.3

#filter()
# filter()  is used to keep only those el;emnts that satisfy a condition
#example
numbers=[1,2,3,4,5,6]
#if we want only  even number
result= list(filter(lambda x:x%2==0,numbers))
print(result)

#difference between map() and filter()
result =list(map(lambda x: x*2,[1,2,3]))
print(result)
#map() chnges every element
result=list(filter(lambda x: x>1,[1,2,3]))
print(result)
#It removes the lement that dont satisfy the condition
#it does not modify the remaining elements
numbers=[5,10,15,20]
result=list(filter(lambda x: x>10, numbers))
print(result)
names=["Ram","Krishna","Om","Ananya","jay"]
result=list(filter(lambda  x: len(x) >3 ,names))
print(result)

#Lesson 18.4
#reduce()
#map()-== transforms every element
#filter()-keeps selecetd  elements
#reduce ()-cobines all elements into a single value
#for example []1,2,3,4]
#can become 10
#it is used when we3 want to copmvbine all the element of a list ninto one final value
#before we must imp[ort it
#from functools import reduce
#it is in the functools module
#because reduce takes two values  and give sthem to your lambda
#normal method
numbers=[1,2,3,4,5]
total=0
for i in  numbers:
     total=total+i
     print(total)
#using reduce we have
from functools import reduce
numbers=[1,2,3,4]
total=reduce(lambda a,b: a+b,numbers)
print(total)
from functools  import reduce
numbers=[2,3,4]
result=reduce(lambda a,b:a*b,numbers)
print(result)
#because reduce repeatedly takes two values and gives them to your lambda function
# if a+b is the operation if first number is 1 nad second 4 then a+b =5 again first number will be 5 and second number will be  next number


****************

#Lesson 19 Iterators and Generators
#lesson 19.1
# An iterable  is any object that you can go through  one element at a time
#qn iterable is an object whose elements can be accessed one by one
#c0 is for calling function
#[] is for  accessing a list element
#int (single) object is not iterable
#lise indexes must be integers or slices not tuple

#for example
numbers=[10,20,30]
# this list is an iterable because you can  use a for loop
for i in numbers:
    print(i)
# the for loop automaticallyy takes one vale at a time
#but whatr happens inside a for loop
# p[ython secretly creates an iterator

#you can create it yourself using iter()
#example
numbers=[10,20,30]
it=iter(numbers)
#here numbers-iterable (the list) , it  iterator
#Getting values  using next()
numbers=[10,20,30]
it =iter(numbers)
print(next(it))
print(next(it))
print(next(it))

#Each call to next() moves the iterator forward by one element
#print(next(it)) -  if we call again when no iterations are left  python gives erro =-StopIteration
#why-because thete are no more elemnts left in the iterator
colors=["Red","Blue","Green"]
it=iter(colors)
print(next(it))
print(next(it))
#exaples for iterables
#List,Tuples,Strings,Sets,Dictionaries,int
#An iterator is an object that keeps track of the current position while going through an irterable one element at a time
text="Hi"
it =iter(text)
print(next(it))
print(next(it))

#Lesson 19.2 -Generators and the yield Keyw0rd
#for example
def numbers():
    return[1,2,3]
print(numbers())
#here return sends all the values at once

#now let  us us eyield
def numbers ():
    yield 1
    yield 2
    yield 3
gen=numbers()
print(next(gen))
print(next(gen))
print(next(gen))
#it does not finish the function
#it pauses the function and returns 1
#when w ecall next(gen) again, the function continues from where it stopped
#it does not start from the beginning
# so: .first next(gen)-1, secpnd next(gen) -2 ,third next(gen)-3
# if we again try to print next(gen) we get error  Stop Iteration
#Difference between  return and yield
#return  end s the function immediately
# returns one final result
                        #example
def add():
     return 010
    #afeter return ,the function is finished
     yield-pauses the function
     #remembers  its position
      #xcontinue from same position
     
def fruits():
    yield "Aplle"
    yield "Banana"

g=fruits()
print(next(g))
print(next(g))
#friuts-generator, g =fruits() creates a generator object ,geneartor nfuncyion isa function that contqains yield
#yield is a keyword that turns a function into a generator and allows it to return values one at atime while pausing its execution and
remembering its state   

def count():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
g=count()
print(next(g))
print(next(g))
def demo():
    yield "A"
    yield  "B"
    yield  "C"
g= demo()
for value in g:
    print(value)# values is thye variable that understands by python to stoire values in the g
    #here afer a,b,c the for loop catches one moren  next(g) but  for loop catches the stopiteration excep[tion so program doesnt crash 
    #loop willend
    '''


















                                                         
      
