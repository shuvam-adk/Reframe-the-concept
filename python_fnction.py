#...Python Functions..

##..Python Functions
# -A function is a block of code which only runs when it is called.
# -A function can return data as a result.
# -A function helps avoiding code repetition.


"""

def function_name(pare1,para2..):
    function_statement
 
    
"""
student_1=[27,54,45] #sum , 3
sums_of_marks_2=sum(student_1)
totl_sub=len(student_1)
averag_e=sums_of_marks_2/totl_sub
print("Average of student 1 is ",averag_e)

#..Istead of this we use this (def) function to do fast code ..

##..
def sum(a,s):  #parameter
    i=a+s
    print("sum is ",i)
sum(20,22)  #argunment
    
    
    
##..
a=2
s=3
out_1=(a*s)//(a+s)
print(out_1)

##..

c=3
q=6
result_2=(c+q)//(q-c)
print(result_2)


##..

def out_2(a,s):
    mean=(a*s)/(a+s)
    print(mean)



##..Example of making pizza..
def making_pizza():
    print("First buy dough")
    print("Add sauce")
    print("Add cheese")
    print("Bake")
    print("You'r! pizza is ready to teast it..")
making_pizza()



##..
def making_masu():
  print("masu",end=' ')
  print("Frying",end=' ')
  print("for 20 min",end=' ')
  print("In low flame",end=' ')
  print("After 10 min more ",end=' ')
  print("You'r chicken is ready",end=' ')
making_masu()


##..Arguments  //Information can be passed into functions as arguments.

# ##..A function with one argument:

def my_function_3(replace_with_names):
  print(replace_with_names + " "+"Adhikari")

my_function_3("Emnar")
my_function_3("Tobi")
my_function_3("Linu")  


## ##...
def full_names(empty_name):
  print(empty_name+" "+ "Adhikari" )
full_names("shuvam")
full_names("Kriti")
full_names("Aashish")


#..

def food(drinks):
  print(drinks+" " + "with cook")
food("Pizza")
food("Noodles")
food("Momo")


##..
def function_s(name):
  print("Hello",name+'.')
function_s("shuvam")
function_s("salon")
function_s("kriti")
function_s("Niranjan")




##...Parameters vs Arguments::

#From a function's perspective:
###.. A parameter is the variable listed inside the parentheses in the function definition.
###.. An argument is the actual value that is sent to the function when it is called.

def my_function_0(name):  #..name is parameater
    print("Heelo",name)
my_function_0("Shuvam")    #.."shuvam" is an argument



#...Default Parameter Values   //  You can assign default values to parameters. If the function is called without an argument, it uses the default value

def my_functio(name="friends"):
    print("Hello", name)
    
my_functio("shuvam")
my_functio("raja")
my_functio("kritik")
my_functio()
my_functio("kailash")


##...
def my_functon(name="Srk"):
  print("Hi",name)
my_functon("Raj")
my_functon("kaka")
my_functon("Messi")
my_functon()



###..
def food_s(name="Momo"):
  print("yummy",name)
food_s("samosa")
food_s()
food_s("chocolate")



# ##...
def my_fen(name="raja"):
    print("Hi",name)
my_fen("Shajan")
my_fen("Rakesh")
my_fen()



##..
def citie_s(names="Poland"):
    print("I would like to travel to this country one day:",names)
citie_s("Sweden")
citie_s("China")
citie_s()



#..

def average(a,s):
    print("the average is ",(a+s)/2)
average(20,2)


# ##..

def person(name="shuvam"):
    print("Hi",name)
person("Raj")
person("Kashab")
person()


def my_fuction(name="friends"):
    print("Hello", name)
    
my_fuction("shuvam")
my_fuction("raja")
my_fuction("kritik")
my_fuction()
my_fuction("kailash")



#..Keyword Arguments // You can send arguments with the key = value syntax.

def output(animal,name):
    print("I have a ",animal)
    print("My",animal+ "'s name is",name)
    
output(animal="Tiger",name="summer")


###..
def animal(animals,human):
    print("I have a dangerous species of animal name ",animals," it is cute  wanna get inside his cage. ")
    print("I have a worst species of human being and it's ",human)
animal(animals="Tiger",human="we all know")


###...
def value_9(planet):
    print("I am in planet ",planet )
value_9(planet="earth")




##..
def val(person,name):
    print("I have a friend " +"'s name", name)
    print("I have a friend",person)
val(person = "Donkey",name="ujjal")



###..
def value_7(gold,money):
    print("I have a treasour"+ " " +"it' a", money +'.')
    print("It will become our treasour",gold)
value_7(gold="money",money="gold")



##..Return Values   //   Functions can return values using the return statement:

def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)


###..
def greeting():
  print("Welcom to python class")
greeting()


###..
def add_2_number(a,s):
  out_put= a+s
  print("The result is:", out_put)
add_2_number(10,30)


####..
def min_2_numbers(q,w):
  out_put=q-w
  print("The output will be like this :",out_put)
min_2_numbers(200,122)


##...

def vec():
  print("I have a mustang.")
vec()


##...
def bike():
  print("I love bullet bikes..")
bike()

###..
def name():
  print("Hi shuvam ")
name()


####....
def greetins():
    print("Hello i am Shuvam.")
greetins()

# ####.. creat  a function to add 2 number 
def add_2_num(a,s):
    result=a+s
    print("The sum is : ",result)
add_2_num(20,22)
add_2_num(23,21)
add_2_num(s=200,a=2000)

# ###..
def addo(q,w,u,e):
    output=q//w-u+e
    print("The output of the value is :",output)
addo(100,100,33,1980)

    
###..function with return statement 

def numbers(q,w,k):
    return q+w//k

value_1 =numbers(10, 200, 100)
print(value_1)

###...
def value(q,w,e,r):
    return q-w+e//r
result=value(100,99,800,1111)
print(result)


# ###..function to convert celsius_to_fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5)+32
    return fahrenheit
#call function
tem_f=celsius_to_fahrenheit(25)
print(tem_f)
print("With return :",type(tem_f))


##..
def room_temprature(tempreture_1):
    heat=(tempreture_1 * 2/1)+22
    return heat
h_t=room_temprature(20)
print(h_t)


####..
def room(tamt_3):
    heata=(tamt_3*2/2)+33
    return heata
pop=room(20)
print(pop)



# ###...function to convert celsius_to_fahrenheit without using of return 
def celsius_fahrenheit(celsius_1):
    fahrenheit_2=(celsius_1 * 9/5)+32
    print(fahrenheit_2)
tem_f2=celsius_fahrenheit(20)
print(tem_f2)
print("Without return :",type(tem_f2))

###..The pass statement - 
def anything():
    pass
print("Hello")





