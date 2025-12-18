###....Using a While Loop.......

#..Python Loops
#..Python has two primitive loop commands:

#...while loops
#...for loops



##..
i=0
while i<=4:
    print(i)
    i=i+1
    

# # ##..
i=int(input("Enter your number :"))
while i>=99:
    print("Too high do it again sir give under num 99 ")
    i=int(input("Enter your number :"))
    
print("We are done! your number is under control :",i)


##..

i=int(input("Enter your number : "))
while(i<100):
    i=int(input("Enter your number : "))
    print(i)
print("Done the work ")


##..

i=int(input("Enter your number again sir : "))
while(i<200):
    i=int(input("Enter your number :"))
    print(i)
print("Completed the task .")





##..The break Statement   ///   What it does: When Python sees break inside a loop, it immediately STOPS the loop and jumps out, regardless of what the loop condition says.
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


##..
list_1=range(5)
for i in list_1:
    if i==4:
        break
    print(i)
        

#..
count=0
name=("shuvam","kriti","raja","muna")
for i in name :
    print(i)
    count +=1
    if count ==2:
        break


##
i=0
while i < 25:
    print(i)
    if i==21:
     break
    i+=1



##..
i=0
while i<=12:
    print(i)
    if i==5:
        break
    i+=1
    
    


##...The continue Statement     ///   With the continue statement we can stop the current iteration, and continue with the next:

i=0
while i<7:
    i+=1
    if i ==4:
        continue
    print(i)  


###.
i=0
while i<6:
    i+=1
    if i==2:
        continue
    print(i)


# ##..
i=0
while i<5:
    i+=1
    if i==2:
       continue
    print(i)


#...

name=("shuvam","dadr","raj","kavish","kalu")
conunt=0
for i in name:
    conunt += 1
    if conunt==3:
        continue
    print(i)      



##..
name=("shuvam","raja","bishnuj","shija","laxmi")
conunt=0
for i in name:
    conunt +=1
    if conunt ==1:
        continue
    print(i)



#...The else Statement  // With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:  # Keep going while i is less than 6
  print(i)    # Print current i
  i += 1      # Increase i by 1
else:
  print("i is no longer less than 6")  # This runs AFTER the loop finishes normally
  


##..
i=0
while i<9:
    print(i)
    i+=1
else:
    print("It is greater then this number .")
  
# ## **Simple analogy:**
# Imagine you're counting steps while walking to a friend's house:
#- **While** you haven't arrived yet → keep walking
# - **Else** (when you finally arrive) → say "I'm here!"

# The `else` is your arrival announcement that only happens when you reach your destination naturally.


#..
i=0
while i <10:
    print(i)
    i+=1
else:
    print("The number is geting higher  as you can see..")
    






##..
i=0
while i<3:
    print(i)
    i=1=i+1


    



##..
name=["shu","vam","raj"]
i=0
while i<len(name):
    print(name[i])
    i=i+1


##..
num=0
while num <=4:
    print("shuvam")
    num +=1

    
#..

i=0
while (i<4):
    print(i)
    i=i+1

##..
i=0
while (i<6):
    print(i)
    i=i+1

###..
i=1
while (i<4):
    print(i)
    i=i+1


##...print names..
i=0
while (i<4):
    print("shuvam")
    i=i+1



###..
i=0
while (i<5):
    print("shuvam","kriti")
    i=i+1
    

###..
i=0
while (i<4):
    print(5)
    i=i+1

###..
i=0
while i<4:
    print("You are doing well")
    i=i+1

###...
i=0
while (i<4):
    print("yhoo,nice")
    i=i+1

##..
i=0
while (i<6):
    print("uhu")
    i=i+1

###...
i=0
while i<=5:
    print(i)
    i=i+1


###...
i=10
while  0<=i:
    print(i)
    i=i-1


###..
i=5
while 0<=i:
    print(i)
    i=i-1


###..
i=9
while 0<=i:
    print(i)
    i=i-1
    
####..
    
i=0
while i<5:
    print(i)
    i=i+1


###..
i=0
while i<4:
    print(i)
    i=i+1

###..
i=0
while i<4:
    print(i)
    i=i+1
    
###....
i=0
while i <4:
    print("shuvam")
    i=i+1

###....
i=1
while i<=10:
    print(2*i)
    i+=1


###
i=1
while i<5:
    print("shuvam")
    i=i+1




##..
i=1
while i<10:
    print(8*i)
    i=i+1


###...
i=1
while i<11:
    print(6*i)
    i=i+1
 
###...i=0
while i<11:
    print(3*i)
    i=i+1






















































































