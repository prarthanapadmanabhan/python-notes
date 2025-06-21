# LOOPS
# Loops are used to repeat instructions.
# Loops are used for sequential transversal. For transversing list, string, tuples etc.  

# while Loops
count=1
while count<=5:
    print("hello")
    count+=1

# BREAK AND CONTIBUE
# Break: Used to terminate the loop when encountered.
# Continue: Terminates execution in the current iteration and continues execution of the loop with the next iteration.

# for Loops
list=[1,2,3,4]
for el in list:
    print(el)

# for loop with else
for el in list:
    print(el)
else:
    print("END")

# range()
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 [by default], and stops before a specified number.
# range(start,stop,step)
for el in range(5):
    print(el)

for el in range(1,5):
    print(el)

for el in range(1,5,2):
    print(el)

# PASS STATEMENT
# Pass is a null statement that does nothing. It is used as a placeholder for future code.
for el in range(10):
    pass