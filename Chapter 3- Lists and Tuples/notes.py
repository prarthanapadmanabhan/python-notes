# LISTS
# A bulit-in data type that stores set of values.
# It can store elements of different types [integer, float, string etc..]
marks=[87,65,34,90] 
student=["Prarthana",85,"Kerala"]
print(marks)
print(student)
print(student[0])
print(len(marks))

# LIST SLICING
# Similar to string slicing
# list_name[starting_index : ending_index] Ending index is not included.
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

# LIST METHODS
list=[2,1,3]
list.append(4) #Adds one element at the end.
print(list)
list.sort() #Sorts in ascending order.
print(list)
list.sort(reverse=True) #Sorts in descending order.
print(list)
list.reverse() #Reverse list.
print(list)
list.insert(1,5) #Adds one element at the index.
print(list)
list.remove(1) #Removes first occurence of element.
print(list)
list.pop(1) #Removes element at index.
print(list)

# TUPLES
# A bult-in data type that lets us create immutable sequence of values.
# tup[0]=43 NOT ALLOWED IN PYTHON
tup=(87,64,33,95,76)
print(tup)

# TUPLE METHODS
print(tup.index(87)) # Returns index of first occurrence.
print(tup.count(1)) # Counts total occurrence.

