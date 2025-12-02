#1..
print("Hello! world")


#2..
import sys
print(sys.version)


#3..
##sys Full Form = sys stands for System


#4..
import sys 
print(sys.version_info)


#5..
print("hello")


#6..python indentation (Yo vane ko space ho  like this 
# if 5 > 2:
#   print("Five is greater than two!")   )
if 5 > 2:
 print("Five is greater than two!")
 
 
#7..✅ Correct Indentation:
if 5 > 2:
    print("Five is greater than two!")  
    print("This is inside the if block") 
# #... ❌ Wrong Indentation: vane ko chai bina space ko print(" ") garnu ho 
# if 5 > 2:
# print("This will cause an error!") 


#8..Correct Indentation:
if 5<8:
    print("Five is less then eight ")


#9..Introduction to statement = It is an instruction for the computer to do something)
name="shuvam"  # Name is a variable , "Shuvam adhikari  "  String  So, a string is simply any text you put inside quotes.
print(name)  #print is an instruction to print(name) is statement
 
 
 
#10..Semicolons (Optional, Rarely used)  (;) this is Semicolons
  # Semicolons are optional in Python. You can write multiple statements on one line by separating them with ;
print("shuvam");print( "raj")  # yo semicolons (;) ko use chai huna tyati 



#11.. function in python 
#print() is a function.
print()                    # Function with NO input
print("Hello")            # Function with string input
print("Hello", "World")   # Function with multiple inputs
print(name)               # Function with variable input


#12..What's inside () is called ?
   #Arguments = The information you give to a function
print("name")  #name is an argument
print("Hi,shuvam adhikari ") #Hi,shuvam adhikari  this whole ting is an argument


#13..Double Quotes
print("Apple is a fruit") # this is inside a Double Quotes (" ")
print( " " )


#14.. What is the use of this     ( end=" " )
   #If you want to print multiple words on the same line, you can use the ( end=" " ) parameter:
  #Note that we add a space after ( end=" " )for better readability.
print("Shuvam",end=" ")
print("Adhikari",end=" ")
print("is",end=" ")
print("doing",end=" ")
print("well. ",end=" ")


#.. 

print("Shuvam",end =" ")
print("Adhiakri",end= " ")


#15..
print("Hello",end=" ")
print("Shuvam",end=" ")

print("Hi shuvam",end=" ")
print("where are you going")



#16..Print Numbers (You can also use the print() function but we dont use double quotes )
print(1,2,3,4,5)
print(2183) #we dont use any quotes in number value 



#17.. You can do maths inside the print() function like =
print(3+3)
print(20*4)


#18..Mix Text and Numbers
print( "Hi shuvam  i'am ",22,"years old ")
print("shuvam is doing well but he is " , 12,"min late for work today")
print("One:",1,"Two:",2,"Three:",3,"Four:",4,"Five:",5,"six:",6,"Seven:",7,)
print("yhoooo:",1000,)



#19.. Python Variables =( Variables are containers for storing data values.)
name=("Shuvam Adhikari !")    #Name is a variable ( "Shuvam Adhikari") is a string.
city=("Kathmandu")     #This (=) is a action
print(name)          # This is a instruction to print name but this is an statement
print(city)          # print is an function  # name and city is an variable 



#20...Whatever value you gave MOST RECENTLY is what will print. 
 
a="shuvam"    # The a = "shuvam" is forgotten because you changed it! into "3" 
a=3           # a = 3  comes right before .  it will print 3.
print(a)   # It will print "3"  because it is recebtly  added 

#More example like 
name="shuavm"
name="kriti"
print(name)  # It will print kriti because it is recently added in variable .



#21.. CASTING  = Changing a value from one type to another type
#  like 


a=11                #This is a int value  if i have to change the a value into any other  value like float we can do this like 
f=float(a)          # a valiable ma we have int value  so if we have to change this value into any other value we cad do like that .. 
print(f)

#.... we are changing numm value into the hexa value like that 

num=233             # num variable bho  #233 int value ho 
h=hex(num)          # To change  int value into hexa decimal we do this.   ???  h : is the  Variable that stores the hexadecimal result
print(h)

#....
x = str('3')
y = int(12)
z = float(3.09)

print(x)
print(y)
print(z)


#...
a=9393
s=float(a)
print(s)

#..
w="0033"
s=float(w)
print(s)


#...

e=112.3
q=int(e)
print(q)




#22...Get the Type = (You can gat the data type of a variable with the like  print(TYPE(....))

# like you can do like this

a=28
s=21.2
print(type(a))  # If you want's to find the type like this you can do like this  print(type(...))
print(type(s))

q="Shuvam Adhikari,"
print(type(q))

#23..Single or Double Quotes?  ( String variables can be declared either by using single or double quotes:)

a="Shuvam" # Yo double quotes garnu  ra  single garnu same ho.
b='Adhikari'


#24..Case-Sensitive  ( They can all hold different values without interfering with each other because their names are different in case.)

a = 4
A = "Sally"
print(a)
print(A)



#25..Variable Names  (A variable name can be any thing like  "x","v" or any thing like name ,age )

#
A_w="shuvam"
print(A)

#
name="shuvam"
print(name)

#
_age="23"
print(_age)

#
MARK=("light")
print(MARK)

#
boom2="boom"
print(boom2)


#26..Multi Words Variable Names 
             # Variable names with more than one word can be difficult to read.
                  # There are several techniques you can use to make them more readable#


# Camel Case  (Camel Case  vane ko chai agadi ko word small letter small hunxa ani arko word ko name  ra baki chai capital latter hunxa )

myVariableName= "kriti" #(As you can see the first letter is small and remaning are capital)
print(myVariableName)

#
myBoy="shuvam"
print(myBoy)

# #
# name=input("enter your name :")
# print(name)


##...Pascal case  (Each word starts with capital letter.) Like this

MyName = "raj"       # like this the first both letters are  capital  "MyName"
AgeOfMyFriend = 22     
DayOfTheDay  = "what"
print(MyName,AgeOfMyFriend, DayOfTheDay, end = " ")


##..Snake Case (In this  Case we do like this name_of_the_charaacter ) like this 

my_name_is="shuavm"   
print(my_name_is)

my_variables_is_this="what is this "   # We do some thing like this is snake case   we do under score 
print(my_variables_is_this)


#27..Output Variables = "The print() function is often used to output variables."

x = "Python is awesome"
print(x)

a="apple"
print(a)


#.. In the print() function,
#Example 
x="python"
q="is"
w="great"
z="to"
c="learn"
print(x,q,w,c,z,)   # output of the variables can be seperated by the comma like this = (,) 


# You can also use the ("+") to output multiple variables 

a="Shuvam "   #Yo code ma all line has space as you can see ("Python "), 
w="Is "       #yo spacee gare ko reason le hare k ma (Shuvam Adhikari Is Geting Better) vaye ko ho natra vane yesto hunxa(ShuvamAdhikariIsGetingBetter) 
z="Geting "
c="Better "
print(a+w+z+c)




#28..Global Variables  (def..)    (YO  AJAI BUJNI   AAYENA MALAI .????)

name = input("enter your name:")

x="name"
def n():       # n = function name  j rakhe ni hunxa  , def = keyword to define a function  ,  (:)=WHERE the function instructions BEGIN 
  print("my"+ " "+ x +" is shuvam adhikari .")
n()

#...
 
# a="Kriti"
# def name():
#         print("my name is " +" " + a  +" " +"adhikari .")
# name()
 
# #


def name(s):
  print("My name is "+ s + " "+"adhikari.")

name("shuvam")
name("kriti")
name("alish")



# #29..


def car(a):
  print("we haave a "+ a +" "+ " car .")
print("Mustang")
print("Ford")
print("rolce royel")

#
n="is"
def name():
    print("my name "+n+" shuvam adhikari .")

name()



#30.python Built-in Data Types
# Text Type=     	  str
# Numeric Types=  	int, float, complex
# Sequence Types= 	list, tuple, range
# Mapping Type=	    dict
# Set Types=    	  set, frozenset
# Boolean Type= 	  bool
# Binary Types=	    bytes, bytearray, memoryview
# None Type=	      NoneType


#31..Getting the Data Type

#string

a="hello vai"     #<class 'str'>
print(type(a))

#intiger

a=20
print(type(a))    #<class 'int'>


#list
a=["apple","banana","cabage","mango"]    #<class 'list'>
print(a)
print(type(a))

#tuple
a=("apple","banana","cabage","mango")    #<class 'tuple'>
print(a)
print(type(a))


#set
a={"apple","banana","mango"}    #<class 'set'>
print(a)
print(type(a))

#  range
w=range(21)
print(w)
print(type(w))
print(list(w))

#.dictionery
q={"name":"shuvam","age":92}
print(q)
print(type(q))

x={
  "name":"shuvam",
  "age":23,
  "studying":"it",
}
print(x)

#


#32....Python Numbers
#There are three numeric types in Python:("int,float,complex ")

x=1              # it is the int type
print(type(x))

x=20.22 # it is the float type 
print(type(x))  


s=1j    # it is the complex type    ("Complex numbers are written with a "j" as the imaginary part:")
print(type(s))


#33..Type Conversion    ( to  change one  value into  another like )

s=44
a=float(s)         #( in this lin ewe are changing  integer value 44 into float value like this )
print(a)


#  float value into a integer value 
a=22.3
s=int(a)
print(s)

#
z=5
s=float(z)
print(s)


#34..Random Number   (" python does't have a random () function to make the  random number python has the built in function  that can  be used to make a random numbers.)
import random
print(random.randrange(1,23))       # Yesle chai 1 bata 23 samako ma random number output ma nikalxa..

#

import random
print(random.randrange(2,9))


#
import random
print(random.randrange(1,33))

#import random
print(random.randrange(28,38))

#
import random
print(random.randrange(848,33333))

#
import random
print(random.randrange(111,3923))


#35...   ( Aba  Ko Baki  practice python_2.py Ma cha )














