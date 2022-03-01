# Q1
print("\nQ1 \n")
#count to see how many steps required
count = 0
#defining a function for solving the tower of Hanoi
def towerofHanoi(n,start_rod,end_rod,aux_rod):
    global count
    if n == 0:
        return
    count += 1
    towerofHanoi(n-1,start_rod, aux_rod, end_rod)
    print("Move disk", n, "from rod", start_rod, "to rod", end_rod)
    towerofHanoi(n-1, aux_rod, end_rod, start_rod)

#Taking the input for the number of discs 
n = int(input("Write the number of discs: "))
print(towerofHanoi(n, 'A', 'C', 'B'))
# Printing number of steps
print('The number of steps will be', count)


# Q2
print("\nQ2 \n")
# Taking input for the number of rows
n = int(input("Write the number of rows: "))
# USing the iterative procedure to solve the question using loops
print("Using iterative procedures: ")
# Empty list to store the pascal's triangle values 
list_1 = []
for i in range(n):
    # Creating a temporary list to append into 
    temp_list = []
    for j in range(i+1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(list_1[i-1][j-1]+ list_1[i-1][j])

    list_1.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2" ), end="")
    for j in range(i+1):
        print(format(list_1[i][j], "<3"),end=" ")
    print() 
print("\n")   

# Using recursion method to solve the question
print("Using Recursion:")
def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)


# Q3
print("\nQ3 \n")
int1 = int(input("Enter the dividend:- "))
#Loop to make sure int2 != 0(i.e. denominator must not be 0)
while True:
    int2 = int(input("Enter the divisor:- "))
    if int2 != 0 and int2>0:
        break
    else:
        print("\nThe divisor must be greater than 0.\nPlease enter the divisor again.")
Quotient=int1//int2
Remainder=int1%int2

print("Quotient = ", Quotient)
print("Remainder = ", Remainder)

#part (a)
print("(a) \n")
print("Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))
print("\n")

#part (b)
print("(b) \n")
if (Quotient == 0 & Remainder == 0):
    print("Both quotient and remainder are zero. \n")
if (Quotient == 0 & Remainder !=0):
    print("Quotient is zero while remainder is non zero. \n")
if (Quotient != 0 and Remainder == 0):
    print("Quotient is non zero while remainder is zero. \n")
if (Quotient != 0 and Remainder != 0):
    print("Both quotient and remainder are non zero. \n")
print("\n")

#part (c)
print("(c) \n")
list = [Quotient + 4, Remainder + 4, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f"The filtered numbers that are greater than 4 are : {result} \n")

#part d)
print("(d) \n")
setresult = set(result)
print("Set:",setresult) 
print("\n")

#part (e)
print("(e) \n")
immutableSet = frozenset(setresult)
#Frozen Set makes the set immutable.
print("Immutable set:- ",immutableSet)
print("\n")

#part (f)
print("(f) \n")
print("Hash value of the max value from the above set:- ", hash(max(immutableSet)))
print("\n")


#Q4
print("\nQ4 \n")
class Student:
    def __init__ (self, student,rollno):
        self.name = student
        self.rollno = rollno

    def __del__(self):
        print("Object deleted.")


#Creating object
student1 = Student("Akshaj Paintola", 21105030)
print("Object created")
#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.rollno}.")
#deleting object
del student1
print("\n")


#Q5
print("\nQ5 \n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))
#Creating Employee records 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#Printing the initial values
print("The current database is:")                                                                       
for i in [employee1,employee2,employee3]:
    i.print_data()

#a) Updating salary
employee1.salary = 70000
print("a) \n")
print(f"The updated salary of {employee1.name} is {employee1.salary} \n")
#b) Deleting a record
print("b) \n")
print("Record of Viren deleted", end='')
del employee3
print("\n")


#Q6
print("\nQ6 \n")
#Defining anagram function
def anagram(word):
    if len(word)==1:
        return [word]
    other_words=anagram(word[1:])
    char=word[0]
    list1=[]
    for combination in other_words:
        for i in range(len(combination)+1):
            list1.append(combination[:i]+char+combination[i:])
    return list1      

# Taking the 3 inputs
George_word=input("George's word: ").lower().replace(" ","")     # Using replace to take care of the space
Barbie_word=input("Barbie's word: ").lower().replace(" ","")     # Using replace to take care of the space
other_words=anagram(George_word)
print("Other possible words are:",other_words)
print("If Barbie's word is present in the list , then their friendship is real. \n")

# Printing the result 
if Barbie_word in other_words:
    print("The Friendship is real.")
else:
    print("The Friendship is fake.")


