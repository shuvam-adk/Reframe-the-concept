#python dectionaries
thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"
    
}

print(thisdict)


##..Dictionary Items  Print the "brand" value and the model value of the dictionary:
thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"
    
}

print(thisdict["brand"])
print(thisdict["model"])


##..Dictionary Length  Get the number of items in the dictionary:

person={
    "name":"shuvam",
    "cast":"adhikari",
    "age":23,
    "city":"kathmandu"
}
print(len(person))


##...Dictionary Items - Data Types

thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"

}

print(type(thisdict["year"]))


##..
name={
    "name":"shuvam",
    "age":23,
}
print(type(name["age"]))


##..
vechical={
    "brand":"toyota",
    "model":"corolla",
    "year":1990,

}
print(type(vechical["brand"]))



# #..Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List         = is a collection which is ordered and changeable. Allows duplicate members.
# Tuple        = is a collection which is ordered and unchangeable. Allows duplicate members.
# Set          = is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary   = is a collection which is ordered** and changeable. No duplicate members.



##..Python - Access Dictionary Items
##...You can access the items of a dictionary by referring to its key name, inside square brackets:


this_dict = {
    "brand": "Ford",
    "model":"mustang",
    "year": 1290,
    "colour":"red",
    "price":29019999
}
out_put = this_dict["brand"]
print(out_put)



##..
country= {
    "nepal":"kathmandu",
    "location":"near lalitpur",
    "numbe_r": 1437,
    
}
out_put_value = country["location"]
print(out_put_value)


##...Check if Key Exists

country= {
    "nepal":"kathmandu",
    "location":"near lalitpur",
    "numbe_r": 1437,
    
}
if "nepal" in country:
    print( "yes ther it is ..")
print()


##..
this_dict = {
    "brand": "Ford",
    "model":"mustang",
    "year": 1290,
    "colour":"red",
    "price":29019999
}

if "model" in this_dict:
    print("Yes there it is ")
    
    

##...Python - Change Dictionary Items //  You can change the value of a specific item by referring to its key name:

thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"
    
}
thisdict["year"] = 2938
print(thisdict)

 
##...
 
thisdct = {
    "brand": "Ford",
    "model":"mustang",
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    
}

thisdct["colour"]= "black"
print(thisdct)

###..Python - Remove Dictionary Items


thisdct = {
    "brand": "Ford",
    "model":"mustang",
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    
}
out_put=thisdct.pop("price")
print(out_put)


##...

thisdct = {
    "brand": "Ford",
    "model":"mustang",
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
}
out_put=thisdct.pop("price")
out_put=thisdct.pop("brand")
out_put=thisdct.pop("colour")

print(out_put)


##...The del keyword removes the item with the specified key name:
##..The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
##..The clear() method empties the dictionary:


##..Python - Loop Dictionaries  //  Loop Through a Dictionary
#..You can loop through a dictionary by using a for loop.

##..

thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"

}
for i in thisdict:
    print(thisdict[i])
    

##..


the_value = {
    "name":"suhvam",
    "cast":"adhikari",
    "age":23,
}
for i in the_value:
    print(the_value[i])
    
    
#..Python - Copy Dictionaries    //  Make a copy of a dictionary with the copy() method:

##..    The syntax for this is output=the_value.copy()

the_value = {
    "name":"suhvam",
    "cast":"adhikari",
    "age":23,
}
output=the_value.copy()
print(output)    


###...Python - Nested Dictionaries   //   A dictionary can contain dictionaries, this is called nested dictionaries.

nested_dictinaries={
"the_value":{
    "name":"suhvam",
    "cast":"adhikari",
    "age":23,
},
"thisdict" : {
    "brand_1": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"
},
"thisdct" : {
    "brand_2": {
        "name":"ford",
        "brand":"shuvam"
    },
    "model":"mustang",
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
}
}
print(nested_dictinaries["the_value"]["age"])
print(nested_dictinaries["thisdct"]["price"])
print(nested_dictinaries["thisdict"]["brand_1"])




##...
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


##.. Start with these 3 for DevOps:

# .get() - Always use this instead of dict[key] in scripts
# .update() - For combining configurations
# .items() - For processing configuration files

#.. (.get) method.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)


##..
value={
  "model":"mustang",
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
}
wout_put_value= value.get("price")
print(wout_put_value)


##..
thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "owner":"shuvam",
    "is_new":"true"

}
reasult=thisdict.get("brand")
print(reasult)



##>..# .update() - For combining configurations
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


##...
thisdict = {
    "brand": "Ford",
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "is_new":"true"

}
thisdict.update({  "owner":"shuvm"})
print(thisdict)



##>..
thsdict = {
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "is_new":"true"

}
thsdict.update({"brand": "Ford",})
print(thsdict)



##..# .items() - For processing configuration files
#...Return the dictionary's key-value pairs:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()     #..The output will be like this  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

print(x)



###....
thsdict = {
    "model":"mustang",
    "year":1290,
    "colour":"red",
    "price":29019999,
    "is_new":"true"
}
out=thsdict.items()   #.. the output will be like this dict_items([('model', 'mustang'), ('year', 1290), ('colour', 'red'), ('price', 29019999), ('is_new', 'true')])
print(out)







