##..The built-in range() function returns an immutable sequence of numbers, commonly used for 
# looping a specific number of times.

##.syntax= range(start,stop,step)

# a=range(2,9,1)
# print(list(a))                  ##.It will print this  [2, 3, 4, 5, 6, 7, 8]

##..start= start position.starting integer of range sequence.
##..stop=end position.sequence ends at stop-1.
##..atep=increment between each integer in sequence.


##..Creating ranges // The range() function can be called with 1, 2, or 3 arguments, using this syntax:
###..range(start, stop, step)


###...Call range() With One Argument  //  If the range function is called with only one argument, the argument represents the stop value.
###..range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).

# a= range(10)
# print(a)              ##.It will print range(0, 10)

# ##..And if we do this like :
# print(list(a))        ##..It will print this   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



##..Call range() With Two Arguments   // If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value
##..range(3, 10) returns a sequence of each number from 3 to 9:

# # s= range (3,10)
# # print(list(s))              ##...It will print this [3, 4, 5, 6, 7, 8, 9]


# ##...
# a=range(4,9)
# print(list(a))


###..Call range() With Three Arguments    //  If the range function is called with three arguments, the third argument represents the step value.
##...The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.

# a=range(3,20,2)
# print(list(a))                ##.It will print this [3, 5, 7, 9, 11, 13, 15, 17, 19]


# ##..
# a=range(2,9,1)
# print(list(a))                  ##.It will print this  [2, 3, 4, 5, 6, 7, 8]



####....Using ranges   //  Ranges are often used in for loops to iterate over a sequence of numbers.

# for i in range(10):
#  print(i)


# ##..
# for i in range(2,10):
#     print(i)




##..Using List to Display Ranges   // The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.


# a=range(2,25)
# print(list(a))                ##..The out put will be like this [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# print(list(range(3,12)))     ##..The output will be like this [3, 4, 5, 6, 7, 8, 9, 10, 11]



# ###..Slicing Ranges   // Like other sequences, ranges can be sliced to extract a subsequence.
# r = range(10)
# print(r[ :7])


###..Membership Testing  // Ranges support membership testing with the in operator.
# q=range(1,10,2)
# print(5 in q)
# print(7 in q)      ###..This will print True


# ##..
# w= range(3,14,3)
# print( 2 in w)
# print(7 in w)          ###..This will print  False


# ##..Length  // Ranges support the len() function to get the number of elements in the range.

# q= range(1,3,1)
# print(len(q))              ##..This will print 2 


# ##..
# q= range(1,7,2)
# print(len(q))            ##..This will print 2



####....Python Arrays  // In Python, an array is a data structure that stores a collection of elements, all of the same type. 
##..Arrays are used to store multiple values in one single variable:

##.What is an Array?
#>.An array is a special variable, which can hold more than one value at a time.

# # ##..This is an examplle of the array 
# # Your array
# nname = ["shuvam", "adhikari"]

# # Add your age to the array
# nname.append(25)  # Assuming age 25
# print(nname)  # ['shuvam', 'adhikari', 25]

# # Make first name uppercase
# nname[0] = nname[0].upper()
# print(nname)  # ['SHUVAM', 'adhikari', 25] 

# ##..
# name=["shuvam","adhikari","is ","a ","good","man"]
# name.pop(1)        ##You can also use the remove() method to remove an element from the array.
# print(name)   


# # ##..Python Iterators  // An iterator is an object that contains a countable number of values.
  
  
## iteratio= (1)..__iter__() > returns the iterator object itself
#            (2).. __next__() > return the next item in the sequence


# my_tupl=("apple","banana","cherry")
# iteration=iter(my_tupl)
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))


# ##..
# my_list=["shuvam","raj","lamphu"]
# it=iter(my_list)
# print(next(it))
# print(next(it))
# print(next(it))




##..
 




