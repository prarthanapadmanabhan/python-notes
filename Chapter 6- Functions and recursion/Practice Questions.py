# WRITE A FUNCTION TO PRINT THE LENGTH OF A LIST.[LIST IS THE PARAMETER].
list1=[1,2,3,4,5]
list2=[33,66,29,0,18,76]
def len_list(a):
    print(len(a))
    return a
len_list(list1)
len_list(list2)

# WRITE A FUNCTION TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.[LIST IOS THE PARAMENTER]
def print_list(list):
    for el in list:
        print(el,end=" ")
print_list(list2) 

print(end="\n")

# WRITE A FUNCTION TO FIND THE FACTORIAL OF N.[N IS THE PARAMETER]
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)

# WRITE A FUNCTION TO CONVERT USD TO INR
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD =",inr_val,"INR")
converter(2)

# WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum=calc_sum(10)
print(sum)

# WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.
def print_list(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["Mango","Litchi","Apple","Banana"]
print_list(fruits)