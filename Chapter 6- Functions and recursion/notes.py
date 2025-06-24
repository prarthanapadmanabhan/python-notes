# FUNCTIONS
# Block of statements that perform a specific task.
# def function_name(parameter1,parameter2): function defenition
#       #some work
#       return val
# function_name(arg1,arg2...) function call
def sum(a,b):
    s=a+b
    print(s)
    return s
sum(2,3)
sum(4,7)

# No parameter function
def print_hello():
    print("hello")
print_hello()

# Function to calculate average of 3 numbers
def calc_avg(a,b,c):
    avg=a+b+c/3
    print(avg)
    return avg
calc_avg(1,2,3)
calc_avg(20,30,40)

# BUILT-IN FUNCTIONS                               USER DEFINED FUNCTIONS
# print()                                          functions written by the programmer
# len()
# tyoe()
# range()

# DEFAULT PARAMETERS
# Assigning a default value to parameter, which is used when no argument is passed.
def calc_prod(a=1,b=1):
    print(a*b)
    return a*b
calc_prod()

# RECURSION
# When a function calls itself repeatedly.
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
show(7)

def fact(i):
    if(i==0 or i==1):
        return 1
    else:
        return i*fact(i-1)
print(fact(4))