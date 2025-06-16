# WHAT IS PYTHON?
# - Python is simple and easy
# - Free and open source.
# - High level language.
# - Developed by GUIDO VAN ROSSUM
# - Portable

# FIRST PROGRAM
print("hello world")

# PYTHON CHARACTER SET
# - Letters: A to Z, a to z
# - Digits: 0 to 9
# - Special symbols: +,-,*,/ etc...
# - Whitespaces: Blank space, tab, carriage return, newline, formfeed
# - Other characters: Python can process all ASCII and unicode characters as part of data or literals.

# VARIABLES
# A variable is a name given to a memory loction in a program.
name="Prarthana"
age=19

# RULES FOR IDENTIFIERS
# - Identifiers can be combination of uppercase and lowercase letters, digits or an underscore(_). So myVariable, variable_1, variable_for_print all are valid python identifiers.
# - An indentifier can not start with a digit. So while variable1 is valid, 1variable is not valid.
# - We can't use special symbols like !, #, @, %, $ etc... in aur identifier.
# - Identifier can be of any length.

# DATA TYPES
# - Integers [int]
# - String [str]
# - Float [float]
# - Boolean [bool]
# - None
print(type(age))
print(type(name))

# KEYWORDS
# Keywords are reserved words in python.
# for eg: and, else, True, False, break, if, elif, while, for etc...

# PRINT SUM
sum=1+3
print(sum)

# TYPES OF OPERATORS
# An operator is a symbol that performs a certain operation bwtween operands
# - ARITHMETIC Operators: +, -, *, /, %, **.
# - RELATIONAL/COMPARISON Operators: ==, !=, <, >, >=, <=.
# - ASSIGNMENT Operators: =, +=, -=, *=, /=, %=, **=.
# - LOGICAL Operators: not, and, or.

# TYPE CONVERSION
a,b=1,2.0
sumnum=a+b
print(sumnum)

# c,d=1,"2"
# sumnum2=c+d
# print(sumnum2) ERROR

# TYPE CASTING
c,d=1,"2"
e=int(b)
print(c+e)

# INPUT IN PYTHON
# input() statement is used to accept values [using keyboard] from user.
# input() result is always a string.
# int(input()) result is integer.
# float(input()) result is float.
