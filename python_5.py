# ####...92..Python - List Comprehension

# ###...Yes, you're absolutely right! List comprehension is just a shorter way 
# # to write the same logic as the traditional for-loop.

# #SO what is this vanda 

# ##..yo..and 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)  # ['apple', 'banana', 'mango']



# ###... yo autai ho optional ho jun tarika le garda ni huncha 
# ##malai yo tareka maan paryo 

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)  # ['apple', 'banana', 'mango']




# ###..93...Python - Sort Lists==  List objects have a sort() method that will sort the list alphanumerically

##.Iportant info ...
##.sort() - A method that works only on lists and changes the original list
##sorted() - A function that works on any iterable (list, tuple, string, etc.) and

###..
value=[9,8,7,6,5,4,3]
value.sort()
print(value)


###..
name=["shuvam","raja","aabishek","cannal"]
name.sort()
print(name)

###...
element=["raja","bab","kaka","aas"]
element.sort()
print(element)


##..
value=(2,43,1,6,7,5,4)
sorted(value)
print(sorted(value))


###..



###.94   ...Sort Descending..         It is the procss of "Arrange things from BIGGEST to SMALLEST in a simple way"
##..lik this...

##..
var=["shuvam","aasdish","dacs","python"]
var.sort(reverse=True)        ###...This is the output (thulo bata sanu jane) ['shuvam', 'python', 'dacs', 'aasdish']
print(var)    

##..
var=["shuva","raj","aashik"]
var.sort(reverse=True)
print(var)



##..
number=[2,3,12,45,6,54,23]
number.sort(reverse=True)
print(number)

##...
name=["shuv","aadi","baspa"]
name.sort(reverse=True)
print(name)


### 95...Case Insensitive Sort..(" ↑ uppercase first   ↑ lowercase second")
##like..this 


##..
list=["Shuvam","adhikari","is","A","good","Man"]
list.sort()
print(list)


##..
variable=["Hi","my","Name","Is","shuvam","adhikari"]
variable.sort()
print(variable)

##..
value=["hi","My","name","Is","kartik"]
value.sort()                  ##..the output will be like this ['Is', 'My', 'hi', 'kartik', 'name']
print(value)               


##>

value=["hi","My","dame","cap","artik"]
value.sort(key= str.lower)             ##...The output will be this (['artik', 'cap', 'dame', 'hi', 'My'])
print(value)


##..
value=["hi","my","cherry","banana","apple"]
value.sort(key=str.lower)                ##..The output will be like this ['artik', 'cap', 'dame', 'hi', 'My']
print(value)

##..
var=["HU","SASA","asg","cat"]
var.sort(key=str.lower)
print(var)


##... Reverse Order   (  reverse()  )
##.
name=["aabishek","raj","hari","syam"]
name.reverse()
print(name)


##...
var=["a","s","w","e","t"]
var.reverse()
print(var)



##...Python - Copy Lists  ==  Use the copy() method
###..
var=["shuvam","raja","rara"]
my_list=var.copy()             ##..The out put will be like this ['shuvam', 'raja', 'rara']
print(my_list)            ##..  You can use the built-in List method copy() to copy a list.


##...
value=["shu","haha","dada","kaka"]
output=value.copy()
print(output)


##>>>..Use the list() method or copy method() .. Another way to make a copy is to use the built-in method list().

animal=["tiger","lion","croco"]
animal_copoy =animal.copy()           ##..The out put will be like this ['tiger', 'lion', 'croco']
print(animal_copoy)

##..
jaja=["kaka","haha","dadd"]
result=jaja.copy()
print(result)


###..Use the slice Operator      Make a copy of a list with the : operator:

anme=["haha","code","dodo"]
var_ie=anme[:]
print(var_ie)


###.....Python - Join Lists      One of the easiest ways are by using the + operator.

a=["a","s","d"]
b=[1,2,3]
c=a+b
print(c)


a=["saaa","kask","dasa"]
b=[2,3,4,5]
c=(a+b)
print(c)



###..









