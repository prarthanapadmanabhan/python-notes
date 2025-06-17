# WRITE A PROGRAM TO INPUT USER'S FIRST NAME AND PRINT ITS LENGTH.
first_name=str(input("Enter your first name:"))
length=len(first_name)
print(length)

# WRITE A PROGRAM TO FIND THE OCCURRENCE OF "$" IN A STRING.
string="I got 50$"
print(string.count("$"))

# WRITE A PROGRAM TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN.
num=int(input("Enter a number:"))
rem=num%2
if(rem==0):
    print("The number is even")
else:
    print("The number is odd")

# WRITE A PROGRAM TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.
num1=int(input("Enter your 1st number:"))
num2=int(input("Enter your 2nd number:"))
num3=int(input("Enter your 3rd number:"))
if(num1>num2 & num1>num3):
    print("Your 1st number is the gretatest.")
elif(num2>num1 & num2>num3):
    print("Your 2nd numver is the greatest.")
else:
    print("Your 3rd number is the greatest.")

# WRITE A PROGRAM TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT.
number=int(input("Enter a number:"))
mult=number%7
if(mult==0):
    print("The number is multiple of 7")
else:
    print("The number is not the multiple of 7")