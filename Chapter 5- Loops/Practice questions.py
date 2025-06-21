# PRINT NUMBERS FROM 1 TO 100. [WHILE LOOP]
count=1
while count<=100:
    print(count)
    count+=1
    
print("LOOP ENDED")

# PRINT NUMBERS FROM 100 TO 1. [WHILE LOOP]
i=100
while i>=1:
    print(i)
    i-=1

print("LOOP ENDED")

# PRINT THE MULTIPLICATION TABLE OF A NUMBER n. [WHILE LOOP]
mul=2
while mul<=20:
    print(mul)
    mul+=2

print("LOOP ENDED")

# OR

mult=1
while mult<=10:
    print(2*mult)
    mult+=1

print("LOOP ENDED")

# PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP.
# [1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1

print("LOOP ENDED")

# SEARCH FOR A NUMBER x IN THIS TUPLE USING LOOP.
# (1,2,9,16,25,36,49,64,81,100)
nums=(1,2,9,16,25,36,49,64,81,100)
x=36
j=0
while j<len(nums):
    if(nums[j]==x):
        print("FOUND AT INDEX", j)
    j+=1

print("LOOP ENDED")

# PRINT NUMBERS FROM 1 TO 100. [RANGE]
for el in range(1,101):
    print(el)
print("LOOP ENDED")

# PRINT NUMBERS FROM 100 TO 1. [RANGE]
for number in range(100,0,-1):
    print(number)
print("LOOP ENDED")

# PRINT MULTIPLICATION TABLE OF A NUMBER N. [RANGE]
n=int(input("Enter a number:"))
for table in range(n,21):
    print(n*table)

print("LOOP ENDED")

# WRITE A PROGRAM TO FIND THE SUM OF FIRST N NUMBERS. [WHILE]
number=int(input("Enter your number:"))
sum=0
k=1
while k<=number:
    sum+=k
    k+=1
print("Your total sum:",sum)

print("LOOP ENDED")

# WRITE A PROGRAM TO FIND THE FACTORIAL OF FIRST N NUMBERS. [FOR]
Number=int(input("Enter your number:"))
fact=1
for f in range(1,Number+1):
    fact*=f
print("Factorial=",fact)

print("LOOP ENDED")
