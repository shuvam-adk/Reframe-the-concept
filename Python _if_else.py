##...Python If Statement
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.


###...If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
  
  
##..Checking if a number is positive:

number = 15
if number > 0:
  print("The number is positive")
  

##..Multiple Statements in If Block

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
  
  
##...Python Elif Statement
##...The Elif Keyword
#..The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


##..Multiple Elif Statements   ///  what is this in simplae word if score is greater then the value givenbelow it will print related to the marks is is easy ..
score = 88

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


###..When to Use Elif    ///  Use elif when you have multiple mutually exclusive conditions to check. 

day = 8

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
else:
    print("There is no any days. left in  calender ")



##...Python Else Statement     ///  The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
##..How Else Works   ///    The else statement provides a default action when none of the previous conditions are true
##..Note: The else statement must come last. You cannot have an elif after an else.

#.Checking even or odd numbers:

#..even numbers like = 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
#..odd numbers like = 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
# Store number to check
number = 7 

# Check even or odd
if number % 2 == 0:        # If remainder is 0    
    print("Even")          # Number is even
else:                      # Otherwise
    print("Odd")           # Number is odd



###..Complete If-Elif-Else Chain    ///    You can combine if, elif, and else to create a comprehensive decision-making structure.

##..Temperature classifier:

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")



##..Else as Fallback    //  The else statement acts as a fallback that executes when none of the preceding conditions are true
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
  
  
# ##,..Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

#    and - Returns True if both statements are true
#     or - Returns True if one of the statements is true
#    not - Reverses the result, returns False if the result is true


#    and - Returns True if both statements are true

a = 200
b = 33
c = 50
if a > b and c > a:
  	print("Both conditions are True")
else:
  	print("there is one mistake on this code ")
    
    
#.    or - Returns True if one of the statements is true   // Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#    not - Reverses the result, returns False if the result is true   ... Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


###...Python Nested If   /// You can have if statements inside if statements. This is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



##...Python Pass Statement    /// if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#..

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement


##..
























