#####........84..Python - Add List Items
#..Append Items  ( To add an item to the end of the list, use the append() method:)


#>>..
name=["name","level"]
name.append("adhikari")
print(name)

##>..
cls=["my","name","is"]
cls.append("shuvam")
cls.append("adhikari")
print(cls)




#..
name=["shuvam","keitik","raj"]
name.append("adhikari")
name.append("acharya")
name.append("rai")
print(name)

##..
var=["apple","berry","cherry"]
var.append("mango")
var.append("banana")
print(var)


#...
rav=["tiger","lion"]
rav.append("hippo")
print(rav)

#.85......Insert Items  ( To insert a list item at a specified index, use the insert() method. )

#..the variable. insert (where to add like index num , " what we are adding ")

#.. like this    the_list.insert(0,"parrot")

the_list=["tiger","lion","hippo"]
the_list.insert(0,"parrot")
print(the_list)

# ###>>..
name=["tiger","lion","crow"]
name.insert(2,"is an dangers animal")
print(name)

#>>..
may=["name","boy"]
may.insert(0,"shuvam")
print(may)

##.>>
name=["shuvam","kriti"]
name.insert(3,"adhikaris")
print(name)



##..like more..
_thelist=["name","place","studying"]
_thelist.insert(0," shuvam adhikari")
_thelist.insert(2," kathmandu")
_thelist.insert(4,"Bca")

print(_thelist)


##.86.......Extend List  ( a.extend(b) ) variable.1 . extande(variable.2)

##>>..
a=["a","b","c","d"]
b=["e","f","g"]
a.extend(b)
print(a)

##>..
name_1= ["shuvam","kriti"]
name_2=["raj","sunny"]
name_1.extend(name_2)
print(name_1)


##>..
name=["bike","car","bye-cycle"]
chr=["raj","shuvam"]
name.extend(chr)
print(name)

##>..
a=["lalmon","banana","cow","dog"]
b=["eagle","fox","giraf"]
a.extend(b)
print(a)



##>>.87...Add Any Iterable

##..>>  The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


list=["aashish","ra","shuvam"]
tuple=("name","it","example")
list.extend(tuple)
print(list)


##.>>.
lisu=["name","var","you"]
usil=("cast","lower","bowwaa")
lisu.extend(usil)
print(lisu)

##..>>..
namae=["can","i","do","it"]
var=("can","i","complete","this","task")
namae.extend(var)
print(namae)




##..88...Python - Remove List Items
#..Remove Specified Item

name=["shuvam","raj","basnet"]
name.remove("raj")
print(name)

##..
name=["suvam","kriti","raj"]
name.remove("kriti")
print(name)


##..
char=["my","name","is","shuvam"]
char.remove("is")
print(char)


##..
value=["sa","sd","da","tata"]
value.remove("sd")
print(value)


##..
name=["shuvam","kriti","billu","rani"]
name.remove("billu")
print(name)


#..
var={"shuvam","raj","car","bullet"}
var.remove("car")
var.remove("bullet")
print(var)



##..89...Remove Specified Index  ( The pop() method removes the specified index)

##..



# #..
n=["shuvam","ram","hari"]
n.pop(1)

#..
mna=["raja","ko", "xora "," is ","good"]
mna.pop(2)
print(mna)                #..The output will be like this ['raja', 'ko', ' is ', 'good']


##..
name=["this ","song","is "," good ","better"]
name.pop(3)
print(name)

##..90..The del keyword also removes the specified index:

the_list=["name","is","going","to","be ","best"]
del  the_list                 #..yo le k garyo vanda yesle list lai nai delete gardyo 


##....
name=["del","function","will","delete ","the","name","list"]
del name


##..91..Clear the List     Clear the list content:  


name=["shuvam","is","a ","good","person"] 
name.clear()
print(name)


# # ##..
vat=["my ","name","is ","what","is","it ","shuvam"]
vat.clear()
print(vat)


##.
value=["shuvam","shubash"]
value.clear()
print(value)




##..