# STRINGS
# String is a data type that stores a sequence of characters.

# BASIC OPERATIONS

# Concatenation
a="hello"+"world"
print(a)

# Length of string
print(len(a))

# Indexing
# a[0]=first character , a[1]= second character
print(a[0])
print(a[4])

# Slicing
# Accessing parts of a string
# str[starting_index : ending_index]
# str[1:] is same as str[1:len(str)]
print(a[1:4])
print(a[:4])
print(a[1:]) 

# Negative indexing
# Always starts from -1.
print(a[-3:-1])

# STRING FUNCTIONS
str="My name is Prarthana"
print(str.endswith("na")) #Returns true if string ends with substring.
print(str.capitalize()) #Capitalizes 1st character.
print(str.replace("Prarthana","Archana")) #Replaces all occurrences of old with new.
print(str.find("Archana")) #Returns 1st index of 1st occurence.
print(str.count("na")) #Counts the occurrence of substring in string.

# CONDITIONAL STATEMENTS
# if-elif-else[SYNTAX]
marks=int(input("Enter your mark:"))
if(marks>=90):
    print("Your grade is A")
elif(marks>=80):
    print("Your grade is B")
elif(marks>=70):
    print("Your grade is C")
else:
    print("Your grade is D")