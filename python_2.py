# #36... Python Strings   ('hello' is the same as "hello".)
# #We can display our srting like this 
# print("hello !")
# print('okay.')


# #Quotes Inside Quotes..

# n="name"
# print(n)
# print("My "+ n +" is 'shuvam adhikari'")   # This is the  Quotes Inside Quotes ("My "+ n +" is 'shuvam adhikari'") 
# print()

# #38..Assign String to a Variable

# x="shuvam"     #x variable vo tyo " " string value assign gariyo  variable ma..
# print(x)


# #39..Multiline Strings  ("""   .. .. . . ..  """)

# name=""" MY name is shuvam adhikari ,
# I am from hetauda,
# I am doing good,
# I will be back."""
# print(name)



# #40...Strings are Arrays   (a=" My car is one of the best in the city.") yo ma chai k hunxa vane space lai in idex value le count garxa jastai (" a gate is open ") a vanda aagadi ko space lai ni count garyo .
  
# name=("shuvam adhikari.")
# print(name[3])

# #..
# shuvam="adhikari is good man."
# print(shuvam[3],shuvam [4])

# # #..
# a="My car is one of the best in the city."
# print(a[1],a[5],a[9],a[4],a[12],a[8])

# s="my name is shuvam adhikari "
# print(s[3],s[12],s[5],s[9],s[0])

# #41...Looping Through a String

# "shuvam" This is a string (a piece of text)
# for ... in This means: "go through each item, one by one"
# x This is a variable - think of it as a temporary container
# The colon (:)  It repeats the same action for each letter.

# # 
# for x in "shuvam ":   # "shuvam " is the word we want .
#     print(x)

# for a in "raja ko xora ":
#     print(a)
    
#
# for a in "raja":
#     print(a)

#
# for q in "anam":
#     print(q)



# #42..String Length

# a="shuvam"
# print(len(a))

# #
# s="raj"
# print(len(s))


# #.
# a="kriti_adhikari"
# print(len(a))


# #43..Check String    ( yo check string le check garxa  xa ki nai value vane ra.)

# #
# a=("my name is shuvam ")
# print("my"in a)

# # #
# # s=("my name is shuvam adhikari is that you boy ")
# # print("yes" in s )


# # #
# # q=("q w e r  t y  u tr ")
# # print("z"in q)

# # #
# # txt = "The best things in life are free!"
# # print("are" in txt)

# #44..Check if NOT   (the keyword  "not in".)

# #
# txt="if i was not there then what"
# print("a"not in txt)


# #
# sta="i am not thee person"
# print("text" not in sta)

# #
# txt="if i am not the person"
# print("not" not in txt )


##45..Use it in an if statement:  ("if  statement ")

# txt="i am the person you are  looking for "
# if " pers " in txt:
#  print(" yes, it is in the txt" )
# else:
#      print("not in the txt ")


# #..
# txt="i am not the good person for you. "
# if "bad" in txt :
#     print("No it is not in the txt.")
# else:
#     print("yes you are.")
    

# #46..Python - Slicing Strings

# q=("hello my boy ")
# print(q[2: ])

# #
# a="hello my name is shuvam adk,"
# print(a[3:9])

# a="my life my choice"
# print(a[0:7])

# # Slicing vane ko chai  yesati nai ho as you  can see ...


# # 47...Slice From the Start    ( yo vane o chai k ho vanda agadi bata nai  slice garne  value lai  like print(a[ :4])  as  we can see i give the space to print  variable  from start ..)

# a="my name is shuvam "
# print(a[ :7])


# w="hi kta ho k cha halkhaber ."
# print(w[ :10])

# #48...Slice To the End ( this is the opposit from the  slice from start  k garn evanda print(a[2: ]) garn eho yesma chai  like =)

# a="hi shuvam  my name is  kriti adhikari "
# print(a[2: ])   # as you can seee i  give the space to print the  all value from the variable...

# a="yo hsdh paue "
# print(a[2: ])



# txt="hello world"
# print(txt[2:5])



# #49....Negative Indexing  ( Use negative indexes to start the slice from the end of the string: )
 
# #
# s=" hi shuvam what are you doing today"
# print(s[-11:-6])    # As you can see negative value  the output is  doing 


# #..
# q="hi i am practicibg some negative indexing values"
# print(q[-24:-16])


# #.. Slice To the End 
# s="Hi there what are you doing today"
# print(s[-24: ])   #.We aslo can use like this  as youu can see


# #..
# h="hi raja ko chora rajkumar"
# print(h[ :-17])

# # Yo k hoo vanda aru time ma jasto negative index ma ( index 0 bata  haina -1 bata suru hunxa )


# #extra..
# txt = "Hello World"
# print(txt[2:5]) 



# #50...Python - Modify Strings

# #("The upper() method returns the string in upper case:")

# #Upper Case  variable. upper() function 

# a="Hi my namE iS sHuvaM ADhikARI"
# print(a.upper())

# hi="my name is shuvam adhikari "
# print(hi.upper())   # yo upper() function le   sabai case lai upper case ma change garxa..

# ss="this variable.upper() function  will change this letter into upper case"
# print(ss.upper())

# #Lower Case     variable.lower()

# a="HI MY NAME IS SHUVAM ADHIKARI "
# print(a.lower())


# ss="THIS VARIABLE.LOWER() FUNCTION WILL CHANGE THIS LETTER INTO LOWER CASE "
# print(ss.lower())


# #51....Remove Whitespace \  text.strip()  yo le chai  agadi ko ra paxade ko space lai hataoucha.

# # #like
# name="   Shuvam,adhiakri    "
# print(name.strip())

# #
# n="   my boy can do any thing    "
# print(n.strip())


# #52..Replace String  variable.replace function("a","b") this replace a thing to what thing you just give command to replace

# #variable.replace function("a","b")

# p="my name is kritik adhikari"
# print(p.replace ("kritik","shuvam") )


# s="me as a  boy i fell good "
# print(s.replace ("boy","man"))

# #53..Split String 
# # variable.split(" ")  yo ho ka ra k lai split garn evane ho 

# a="hello vai raja"
# print(a.split("e"))


# s="hi i am going to split this,'apple','babana','cherry,"
# print(s.split(' '))   # yesle sabai ko ma  , diyo 

# q="apple,banana,cheery"
# print(q.split(','))     #what it does it actually give space like you can see in output . 



# #54...Python - String Concatenation

# #To combine, two strings you can use the + operator.

# #Merge variable a with variable b into variable c:

# intro="Hi"
# name="shuavm"
# last_name="adhikari"
# full_name= intro +" "+name + " "+ last_name
# print(full_name)


# #..
# name="kri"
# full_name="ti"
# space=" "
# last_name="adh"
# full_last_name="kari"
# print(name+full_name+space+last_name+full_last_name)


# #55..Python - Format - Strings
# #we cannot combine strings and numbers like this:

# # age = 36
# # This will produce an error:
# # txt = "My name is John, I am " + age
# # print(txt)

# # but we can do this   (" F-Strings ")

# age = 36
# #This will not  produce an error:
# txt =f"My name is John, I am:{age} years old"
# print(txt)

# #56...Placeholders and Modifiers

# name="shuvam"
# last_name="adhikARI"
# print(f"Uper_case : {name.upper()}")


# #
# a,s=2,4
# print(f"Sum : {a+s}")

# #
# a,e=3,4
# print(f"Sum: {a+e}")


# #
# name="SHUVAM"
# last_name="adhikari"
# print(f"lower_case_a:{name.lower()}")
# print(f"upper_case_w :{last_name.upper()}")
# print(f"full name:{name.lower()},{last_name.upper()}")


# #..
# txt=f"The price is {49*33}$ dollars"
# print(txt)

# #57...Python - Escape Characters   ( \" .. ..   \") we do this .

# #...You will get an error if you use double quotes inside a string that is surrounded by double quotes
# #..To fix this problem, use the escape character \":

# #..
# txt = "We are from \"kathmandu\" but from diffrent locations ."
# print(txt)

# #..
# name="my name is \"Shuvam\" adhikari ."
# print(name)




# #58...Python - String Methods  ( there are so many  like )

# #..Python String capitalize() Method  ... (The capitalize() method returns a string where the first character is upper case, and the rest is lower case.)

# name="shuvam Adhikari "
# print(name.capitalize())   # this will halp to capitalize the first letter..

# #
# animal="tiger is a unharmed animal ?.. haha"
# print(animal.capitalize())


# #..Python String casefold() Method ... (The casefold() method returns a string where all the characters are lower case.)

# #... print(variable.casefold())
# name="SHUVAM, ADHIKARI.."
# print(name.casefold())      #..( this method well help to make capital  to small one)

# #
# a="SIJIOFN"
# print(a.casefold())


# #..Return the string without any whitespace at the beginning or the end.
# txt = " Hello World "
# x = txt.strip()


# #..onvert the value of txt to upper case.

# txt = "Hello World"
# txt = txt.upper()

# # 59...Python Booleans   (Booleans represent one of two values: True or False.)


# #.
# print(10>3) #( 10 is greater than 3)

# #.
# print(20==18)  # ( 20 is equal equal ti 18)


# #..

# q=20
# b=21
# if q > b:
#     print("yes it is. ")
# elif q==b:
#     print(" Both are same.")
# else:
#     print("They are not equal . as you can see.")



# #..60...Most Values are True

# #Almost any value is evaluated to True if it has some sort of content.
# #Any string is True, except empty strings.
# #Any number is True, except 0.
# #Any list, tuple, set, and dictionary are True, except empty ones.



# #..Some Values are False  Example  :-

# #.....The following will return False:

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

# # this all will return false ..

# #.61..Python Operators  =  Python divides the operators in the following groups:
#                     #.. Arithmetic operators
#                     #..Assignment operators
#                     #..Comparison operators
#                     #..Logical operators
#                     #..Identity operators
#                     #..Membership operators
#                     #..Bitwise operators   give this example of this operaters


# #62.. In Arithmetic operators there are =  

# # Addition            x + y	
# #..Subtraction        x - y	
# #..Multiplication     x * y
# #..Division           x / y
# #..Modulus	          x % y
# #..Exponentiation     x ** y
# #..Floor division	  x // y


# # Addition            x + y	
# x=2
# y=4
# print(x+y)


# #..Subtraction        x - y	
# x=22
# y=4
# print(x-y)

# #..Multiplication     x * y
# x=2
# y=4
# print(x*y)

# #..Division           x / y

# x=995
# y=40
# print(x/y)       #..24.875 it gaves the ans in float

# ##..Modulus	          x % y

# x=230
# y=7
# print(x%y)

# #..Exponentiation     x ** y

# x=26
# y=4
# print(x**y)

# #..Floor division	  x // y

# x=25327
# y=434
# print(x//y)      #.. it gaves the answer in integer .. "58"





# #..63.... In Assignment operator there are  =  Operators like  this =

# #1..     =	        x = 5	         x = 5	
# #2..    +=	        x += 3	         x = x + 3	
# #3..    -=	        x -= 3    	     x = x - 3	
# #4..    *=	        x *= 3	         x = x * 3	
# #5..    /=	        x /= 3	         x = x / 3	
# #6..    %=	        x %= 3	         x = x % 3	
# #7..    //=	        x //= 3	         x = x // 3	
# #8..    **=	        x **= 3	         x = x ** 3	
# #9..    &=	        x &= 3	         x = x & 3	
# #10..   |=	        x |= 3	         x = x | 3	
# #11..   ^=	        x ^= 3	         x = x ^ 3	
# #12..   >>=	        x >>= 3	         x = x >> 3	
# #13..   <<=	        x <<= 3	         x = x << 3	
# #14..   :=	       print(x := 3)	 x = 3
# #.                                   print(x)


# #1..   =	     x = 5	         x = 5	
# a=2
# print(a)      # (yo aru kai haina a vane variable ma 2 lai denote gare ko ho ) 

# #2..  + =	     x += 3	         x = x + 3	
# w=8
# w+=2           #..( yo ma w ko variable lai  afai le auta value diye ra add gare ko ho )  
# print(w)

# #3..    -=	        x -= 3    	     x = x - 3	
# a=10
# a-=2            #..(yo ma a ko variable lai  afai le auta value diye ra minus gare ko ho )
# print(a)

# #4..    *=	        x *= 3	         x = x * 3	
# a=9
# a*=10           #..(yo ma a ko variable lai  afai le auta value diye ra multiply gare ko ho 
# print(a)


# #5..    /=	        x /= 3	         x = x / 3	
# s=10
# s /=2          #..(yo ma s ko variable lai  afai le auta value diye ra divide gare ko ho 
# print(s)


# #6..    %=	        x %= 3	         x = x % 3	
# d=38
# d %=3         #..( In short divide 38 with 3 and remaining is 2 the output will be 2..)
# print(d)

# #7..    //=	        x //= 3	         x = x // 3	
# w=54
# w //=2
# print(w)


# #8..    **=	        x **= 3	         x = x ** 3	
# e=8
# e **=2      #..( " yo k vane ko ho vanda 8 le 2 lai 8*8 gare ko ho " )
# print(e)


# #9..    &=	        x &= 3	         x = x & 3	
# c=40
# c &=2         #..
# print(c)


# #10..   |=	        x |= 3	         x = x | 3	
# t=20
# t |=2
# print(t)


# #11..   ^=	        x ^= 3	         x = x ^ 3	
# v=80
# v ^=2
# print(v)


# #12..   >>=	        x >>= 3	         x = x >> 3	
# n=70
# n >>=20
# print(n)


# #13..   <<=	        x <<= 3	         x = x << 3	
# m=29
# m<<=2
# print(m)


# #14..   :=	       print(x := 3)	 x = 3
# w=38
# print(w:=3)



# # #.64...The Walrus Operator
# # number=[1,2,3,4,5,6,7,8,9]

# # if(total:= len(number))>3:
# #     print(f"list has {total} elements.. ")

# # #..
# # name="shuvam adhikari "
# # if(name := input("Enter your real name :")) != " ":
# #     print(f"hello {name}")



# #..65 This is the easy way to understanding this .... example of the Walrus operation 

# # Normal = (just saving):
# x = 5 + 3        # SAVE the result of 5+3 as x

# # Walrus := (do and save):
# if (y := 5 + 3) > 6:  # DO 5+3 AND SAVE as y, then check if >6
#     print(y)




# # 66..Python Comparison Operators

# #..  Operator        	 Name	                  Example	
# #       ==	             Equal	                   x == y	
# #       !=	           Not equal	               x != y	
# #       >	          Greater than	               x > y	
# #       <	           Less than	               x < y	
# #       >=	      Greater than or equal to	       x >= y	
# #       <=	       Less than or equal to	       x <= y


# # #The use of the operator..

# x = 5
# y = 3

# print(x == y)    #(5 and 3 is not equal ==  so it willl get false )
# print(x != y)      #("Just asking "Are they different?"  k yo 5 and 3  farak cha ta  vane ko ho like ya 5 and 5 va ko vaye false aaunthyo kina vane  farak chain atyo duita ma )
# print(x > y)       #(" x > y means: "Is x BIGGER than y? ")
# print(x < y)       #("x < y means: "Is x SMALLER  than y?")
# print(x >= y)      #(" x >= y means: "Is x BIGGER OR EQUAL to y? ")
# print(x <= y)      #(" x <= y means: "Is x SMALLER OR EQUAL to y? " )


# # x = 5    # 🟰
# # y = 3    # 🟰
# # print(x != y)  # "Is 5 different from 3?" → YES! → True



# #67..Chaining Comparison Operators


# #..Chaining Comparisons means:-
# # "Checking if a number is BETWEEN two other numbers"

# x = 5

# print(1 < x < 10)

# #..Think of it like this:
# #..We have number 5
# #..We ask: "Is 5 between 1 and 10?"
# #..Look: 1 ← 5 → 10 → YES, 5 is between them!
# #..So answer is: True ✅



# n=40
# print( 50 <  n  < 100 )  # Is 40 is between 50 & 100 .. the  answer is False .. 


# # 68..Logical Operators
# #Logical operators are used to combine conditional statements:

# #     Operator	               Description	                                         Example	
# #       and 	     Returns True if both statements are true	                    x < 5 and  x < 10	
# #        or	         Returns True if one of the statements is true	                x < 5 or x < 4	
# #       not	         Reverse the result, returns False if the result is true	     not(x < 5 and x < 10)



# #...Test if a number is greater than 0 and less than 10:
# x = 5


# print(x > 0 and x < 10)     #( True aauncha kina vane x is greater than  0 and  less than 10 so true )
# print(x < 5 or x > 10)     # ( False aauncha kin avane  5 is not less than x &  x is not greater than 10 )
# print(not(x > 3 and x < 10))  #( False aauncha kina vane  not value le garda (x > 3 and x < 10) ko vitra value 5 cha tara  the output wil be  false    )





# # # q=input("enter your name :")
# # # print(q)



# #69....
# w=1000
# print(w >= 999 or  w<=1002)
# if w >= 999 and w<=1002 :
#     print(f"you are correct the number {w} is right")
# else :
#      print("Nothing in impossible in this world ")








# #range
# w=range(21)
# print(w)
# print(type(w))
# print(list(w))












































# # # # name=input("enter your name :")
# # # # print(name)


# # # # name=67
# # # # n=float(name)
# # # # print(n)

# # # # num=56.4
# # # # i=int(num)
# # # # print(i)


# # # # a="shuvam"
# # # # def name():
# # # #   print("my name is " +" " + a  +" " +"adhikari .")
# # # # name()
 
# # # # #

# # # # a="eignt"
# # # # def a():
# # # #     print()

# # # # print("shuvam")

# # # # casting...

# # # # a=23
# # # # s=float(a)
# # # # print(s)
















