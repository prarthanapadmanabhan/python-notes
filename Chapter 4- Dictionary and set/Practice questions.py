# STORE FOLLOWIG WORD MEANINGS IN A PYTHON DICTIONARY.
# table:"a piece of furniture","list of facts and figures"
# cat:"a small animal"
meanings={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(meanings)

# YOY ARE GIVEN A LIST OF SUBJECTS FOR STUDENTS. ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT. HOW MANY CLASSROOMS ARE NEEDED BY ALL STUDENTS.
# "python","java","C++","python","javascript","java","python","java","C++","C"
subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subjects))

# WRITE A PROGRAM TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY. START WITH AN EMPTY DICTIONARY AND ADD ONE BY ONE. USE SUBJECT NAME AS KEY AND MARKS AS VALUE.
marks={}
marks1=int(input("Enter your first mark:"))
marks2=int(input("Enter your second marks:"))
marks3=int(input("Enter your third mark:"))
marks["mark1"]=marks1
marks["mark2"]=marks2
marks["mark3"]=marks3
print(marks)

# FIGURE OUT A WAY TO STORE 9 AND 9.0 AS SEPARATE VALUES IN THE SET. [TOU CAN TAKE HELP OF BUILT-IN DATA TYPES].
val={9,"9.0"}
print(val)
