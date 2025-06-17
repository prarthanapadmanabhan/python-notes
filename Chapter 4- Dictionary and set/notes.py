# DICTIONARY
# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable and doný allow duplicate keys.
# dict["key"]="value" to assign or add new.
dict={
    "name":"Prarthana",
    "cgpa":9.6,
    "marks":[98,97,96],
}
print(dict)
print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])

# NESTED DICTIONARIES
student={
    "name":"Prarthana",
    "cgpa":9.6,
    "score":{
        "chem":98,
        "phy":97,
        "math":95,
    }
}
print(student)
print(student["score"]["math"])

# DICTIONARY METHODS
print(student.keys()) #Returns all keys
print(student.values()) #Returns all values
print(student.items()) #Returns all keys,val pairs as tuples
print(student.get("cgpa")) #Returns the key according to value
new_dict={"name":"Archana","age":16}
student.update(new_dict) #Inserts the specific item to the dictionary
print(student) 

# SET
# Set is the collection of unordered items.
# Ech element in the set must be unique and immutable.
nums={1,2,3,4}
set2={1,2,2,2} #Repeated elements stored only once, so it resolved to {1,2}

# EMPTY SET SYNTAX
null_set=set()

# SET METHODS
set2.add(3) #Adds an element.
print(set2)
set2.remove(3) #Removes an element.
print(set2)
set2.pop() #Removes a random value.
print(set2)
set2.intersection(nums) #Combines common values and returns new
print(set2)
set2.union(nums) #Combines both set values and returns new
print(set2)
set2.clear() #Empties the set
print(set2)
