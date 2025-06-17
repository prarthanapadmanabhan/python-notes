# WRITE A PROGRAM TO ASK USER TO ENTER NAMES OF THEIR 3 FAVORITE MOVIES AND STORE THEM IN A LIST.
movie1=str(input("Enter your first movie name:"))
movie2=str(input("Enter your second movie name:"))
movie3=str(input("Enter your third movie name:"))
movies=[movie1,movie2,movie3]
print(movies)

# OR

movie=[]
mov1=str(input("Enter your first movie name:"))
mov2=str(input("Enter your second movie name:"))
mov3=str(input("Enter your third movie name:"))
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)

# WRITE A PROGRAM TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.
# [1,2,3,2,1] , [1, "abc", "abc", 1]
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("The list contains palindrome elements ")
else:
    print("The list doesnot contain palindrome elements")

list2=[1, "abc", "abc", 1]
copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list2==list2):
    print("The list contains palindrome elements ")
else:
    print("The list doesnot contain palindrome elements")

# WRITE A PROGRAM TO COUNT THE NUMBER OF STUDENTS WITH A GRADE IN THE FOLLOWING TUPLE. STORE THE ABOVE VALUES IN LIST AND SORT THEM FROM A TO D.
# ("C","D","A","A","B","B","A")
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))

grades=["C","D","A","A","B","B","A"]
grades.sort()
print(grades)


