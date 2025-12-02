# #..so what you are trying to say is like when we divide this 38 
# # now 3*1 is 3 now renaimaing 8 so what we do is
# # 3*2 is 6 now we have  remaning is 2 this is what i trying to say 

# d=38
# d %=3
# print(d)

# c=40
# c &=2         #..
# print(c)



#70.....Identity Operators  :-  Identity operators are used to compare the objects, 

# not if they are equal, but if they are actually the same object, with the same memory location:

#       Operator	            Description	                        Example 
#                                                                
#         is         	Returns True if both variables               x is y
#                          are the same object	                    
#                                                                  	
#        is not	        Returns True if both variables              x is not y
#                         are not the same object	                





#..The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      #..Returns True if both variable  are the same objec
print(x is y)       #,, reaturn False
print(x == y)       #..Reaturn true cause same look.


 #Cookie Example:

# x = ["apple", "banana"]   Bake cookie "x"

# y = ["apple", "banana"]    Bake identical cookie "y"

# z = x =  Give cookie "x" a second name "z"

# Results:
# x is z = Same cookie? ✅ True
# x is y = Same cookie? ❌ False (different cookies)
# x == y = Same look? ✅ True (look identical)
# Simple rule:
# is = Same object?
# == = Same contents?




#...The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# What I'm trying to say:

# You have two separate cookie jars 🍪🍪

# Both jars have the same fruits inside: "apple" and "banana"

# But they are different jars

# x is not y means: "Are x and y different jars?"

# ✅ YES! They are different jars.

# So print(x is not y) shows True because they are NOT the same jar, even though both have the same fruits.







#71...Membership Operators  = Membership operators are used to test if a sequence is presented in an object:


##..       Operator                       Description	                                     Example	
##..          in 	               Returns True if a sequence with the                   
#                                specified value is present in the object                    x in y     
          	
##..        not in	              Returns True if a sequence with the specified
#                                    value is not present in the object                     x not in y




#Check if "banana" is present in a list: using (in) operator 
fruits=["banana","apple","cherry"]
print("apple" in fruits)

#..
a=["a","s","w"]
print("n" in a)


#..Check if "pineapple" is NOT present in a list: (using not in) operator
fruits=["apple","banana","grapes"]
print("coconut"  not in fruits )

#..
a_groups=["a","s","d","q"]
print("h" not in a_groups)



#..Membership in Strings  = The membership operators also work with strings:

text="HI my name is shuvam"

print("H" in text)
print("h" not in text)
print("shuvam" in text) 




#72...Python Bitwise Operators


#..Bitwise operators are used to compare (binary) numbers:

##              Operator	       Name	                                              Description	                                              Example	
#         	         
##..               &               AND	                                 Sets each bit to 1 if both bits are 1                        	          x & y	
#          	        
##..               |                OR	                                  Sets each bit to 1 if one of two                           
#                                                                                   bits is 1	                                                  x   | y	
#          	         
##..               ^               XOR	                                Sets each bit to 1 if only one of two
#                                                                                   bits is 1	                                                    x ^ y	
#         	                                     
##..               ~               NOT	                                        Inverts all the bits	                                             ~x	
#          	     
##..               <<           Zero fill left shift	                 Shift left by pushing zeros in from 
#                                                                    the right and let the leftmost bits fall off                                    x << 2	
#                  
##..               >>          Signed right shift	              Shift right by pushing copies of the leftmost bit in  
#                                                                  from the left, and let the rightmost bits fall off	                             x >> 2


#..Bitwise operator like =  ( & , | , ^ , ~ , << , >> )  This are the operators and some examples  as well..

#.. using of  "&" operator..


# Yo buje ko xaina ajai try garnu parcha..

q=3
w=5
print(q  &  w)

a=34
x=37
print( a & x )



#..using of  "|" operator.


q=3
w=5
print(q  |  w)


#..using of  "^" operator.


q=34
w=53
print(q  ^  w)


#..using of  "~" operator.
w=73
e=32
print(~w,~e)

#..using of  "<<" operator.
w=44
y=33
print(w<<y)

#..using of  ">>" operator.
w=45
q=66
print(w>>q)


#73...Python Operator Precedence
   # it means that in order like [ / , * , + , - ] etc..


a=20
s=5
print((a/s)-(a+s))   # Parentheses () = FIRST PRIORITY  and other after that ..



#74...Precedence Order...

#...   ()                        = Parentheses                              (ALWAYS FIRST)
 
#...   **                        =  Exponents                                (powers)

#...   * ,  /                    =  Multiplication & Division

#...   + , -                     =  Addition & Subtraction

#...   == , > , <                =  Comparisons                           (equal, greater, less)

#..   and , or, not              =  Basic Logic


##..Some examples.. of Exponents ..

##...  ( ** )         =  Exponents   ( " The second number tells you how many times to multiply the first number by itself." )
#..like.

print(2 ** 3)  # 2 × 2 × 2 = 8 (2 appears 3 times)
print(4 ** 2)   
print(5 ** 3)  # 5 have to multiply it self for 3 times like ( 5 * 5 * 5 = 125 )


##..  (  *, / )       =  Multiplication & Division

a=20
s=2
print(s*a)

#..

w=90
r=3
print(w/r)


##...   + , -        =  Addition & Subtraction

#.
num_1=20
num_2=10
print(num_1+num_2)


#.
var=38
rav=3
print(var-rav)



##...   == , > , <     =  Comparisons     (equal, greater, less)

#. ( == )

w=20
e=20
if e==w:
    print(f"It is an equal number {w} == {e}")
else:
    print("Happy journey")


#..  ( > )
r=20
e=21
if e > r :
    print(f"My number {e}, is Greater then  you'r..{r}.")
else:
    print("Not as greater as mine boy ..")


#.. (<)
r=200
e=21
if e < r :
    print(f"My number {r}, is Greater then  you'r..{e}.")
if e>=r:
    print(f"My number {e} is greater then you'rs")
else:
    ("Not as greater as mine boy ..")




##...   and , or, not  =  Basic Logic

#.. and = 	Returns True if both statements are true
#..or =	Returns True if one of the statements is true
#..or = Reverse the result, returns False if the result is true





##.75...Python Lists = " Lists are used to store multiple items in a single variable. "
#..some example..

list=["apple","banana","cherry"]  # this is the  called list..
print(list)



#..76..Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#... List   "[]"     = is a collection which is ordered and changeable. Allows duplicate members.
#... Tuple   "()"    = is a collection which is ordered and unchangeable. Allows duplicate members.
#... Set      "{}"   = is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#... Dictionary  = is a collection which is ordered** and changeable. No duplicate members.


##..77..Python - Access List Items

#..
a=["shuvam","adhikari","kriti"]
print(a[2])

#..
s=["a","s","f","g","d","s"]
print(s[4])


##..Negative Indexing = ( -1 refers to the last item, -2 refers to the second last item etc. )

a=["haha","dada","wawa","jaja","qoqo"]
print(a[-3],a[-4])

x=["ai","wu","ey","rr","tt"]
print(x[-4],x[-2],x[-1])



##..78...Range of Indexes      ( ":" we use slicing method this the sign of slicing method )
#..For example..

#..
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # It will retaurn  "cherry", "orange", "kiwi" ... .

##. Note: The search will start at index 2 (included) and end at index 5 (not included).


#..

txt=["s","h","u","v","a","m"]
print(txt[0 : 6])


#..

txt=["s","h","u","v","a","m"]
print(txt[  0 : ])


##79...Range of Negative Indexes

txt=["sh","uv","am","ad","hi","ka","ri"]
print(txt[-7:-4])




##.80..Check if Item Exist
var=["shuvam is a good guy.. "]
if "prank" in var:
    print("yes the name prank in txt ")
else:
   print("I am just kidding..")




##.81..Python - Change List Items  (" To change the value of a specific item, refer to the index number:")


a=["shuvam","kriti","raj","hari"]
a[2] = "ram"
print(a)    # Ya  k huncha vane ram saga  raj o replace va ok ho  ( The out put will be like this ['shuvam', 'kriti', 'ram', 'hari'])

##..
name=["Hi", "my", "name", "is", "shuvam ","adhikari", ".", "i'am", "from", "hetauda "]
name[4]="kriti"
name[9]="kathmandu"

print(name)


##..
name=["a","c","c1","c","d","e"]
name[1]="b"
name[2]="c"
name[3]="d"
name[4]="e"
name[5]="f"

print(name)



##.82...Change a Range of Item Values

##..To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

##..Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":


##.
name=["apple","shuvam","banana","cherry","mango"]
name[1:3]=["kriti","maya"]
print(name)        # The output will be like this = ['apple', 'kriti', 'maya', 'cherry', 'mango']



##..
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)


##.83..Insert Items  ( variable . insert(where , "value")) like ..

##.
name=["shuvam","kriti","ashu"]
name.insert(1,"Adhikari")
name.insert(3,"Adhiakri")
print(name)


##..
my_list=["apple","banana","mango"]
my_list.insert(1,"and")
print(my_list)

##..
mylist1 = ['apple', 'banana', 'cherry']
mylist1[0] = 'kiwi'
print(mylist1)








##..Left-to-Right Evaluation

#..If two operators have the same precedence, the expression is evaluated from left to right.

#.Like this one = 1..What is the result of   ( 10 - 5 + 3 )?

# a=10
# w=5
# s=3
# print( a - w + s )  # 10-5 = 5 and now 5+3 + 8 the ans is 8...



# t=20
# t |=2
# print(t)


# v=80
# v ^=2
# print(v)




