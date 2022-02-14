# Q1
# Defining a function to calculate occurrences of string elements
def occurrence_calculator(lst):
    empty = []
# Using dictionaries to display number of occurrences of the elements
    occurrence = {lst[i]: 1 for i in range(0, len(lst))}
# Loop to update values of different elements
    for char in lst:
        if char in empty:
            occurrence[char] += 1
        else:
            empty.append(char)
    print(occurrence, '\n')


# Taking input string from the user
string = input("Enter the string: ")
# Checking if the entered string is a single word or a sentence
if " " not in string:
    letters = list(string)
    occurrence_calculator(letters)

else:
    words = string.split()
    occurrence_calculator(words)


#Q2
#We take input of the day here
day = int(input('Write the day: '))
#Condition C2 for day 
1<=day<=31
#We take input of the month here
month = int(input('Write the month: '))
#Condition C1 for month
1<=month<=12
#We take input for the year here
year = int(input('Write the year: '))
#Condition C3 for the year
1800<=year<=2025

#Using if statements to check if the year is a leap year  
if year % 4 == 0:
    #Condition for the month December
    if month == 12:
        if day < 31:
            print(f'{day + 1}/{month}/{year}')
        elif day == 31:
            print(f'01/01/{year+1}')
        else:
            print('Invalid date, check again!')
    #Condition for month February 
    elif month == 2:
        if day<29:
            print(f'{day + 1}/{month}/{year}')
        elif day ==29:
            print(f'01/{month +1}/{year}')
        else:
            print('Invalid date, check again!')
    #Condition for months having 30 days
    elif month == 4 or 6 or 9 or 11:
        if day< 30:
            print(f'{day + 1}/{month}/{year}')
        elif day == 30:
            print(f'01/{month +1}/{year}')
        else:
            print('Invalid date, check again!')
    #Condition for months having 31 days
    elif month == 1 or 3 or 7 or 8 or 10:
        if day < 31:
            print(f'{day + 1}/{month}/{year}')
        elif day == 31:
            print(f'01/{month +1}/{year}')
        else:
            print('Invalid date, check again!')

#If not a leap year and the same logic works as explained above
elif year%4 != 0:
    if month == 12:
        if day < 31:
            print(f'{day + 1}/{month}/{year}')
        elif day == 31:
            print(f'01/01/{year+1}')
        else:
            print('Invalid date, check again!')
    elif month == 2:
        if day<28:
            print(f'{day + 1}/{month}/{year}')
        elif day ==28:
            print(f'01/{month +1}/{year}')
        else:
            print('Invalid date, check again!')
    elif month == 4 or 6 or 9 or 11:
        if day< 30:
            print(f'{day + 1}/{month}/{year}')
        elif day == 30:
            print(f'01/{month +1}/{year}')
        else:
            print('Invalid date, check again!')
    elif month == 1 or 3 or 7 or 8 or 10:
        if day < 31:
            print(f'{day + 1}/{month}/{year}')
        elif day == 31:
            print(f'01/{month + 1}/{year}')
        else:
            print('Invalid date, check again!')

#Q3
#List to be used for the question
list1 = map(int, input('Enter space seperated integers to input into the list: ').split())
#Empty list as we will append from the for loop 
output_list = []
#Using for loop to append tuples into the output list
for i in list1:
    output_list.append((i,i**2))
#Printing the output list
print(output_list)


#Q4
#Taking grade input from the user
user_grade = int(input('Write your Grade: '))
#Making a list to store tuple
Logic = [('Outstanding','A+'), ('Excellent','A'), ('Very Good','B+'), ('Good','B'), ('Average','C+'), ('Below Average','C'), ('Poor','D')]
#Making a Grade list to find the index of the tuple
Grade = [10, 9, 8, 7, 6, 5, 4]

#Using if else according to the question
if 4<= user_grade <= 10 :
    #Using .index() function to find the index of the list
    a = Grade.index(user_grade)
    print(f"Your Grade is '{Logic[a][1]}' and {Logic[a][0]} Performance.")
else :
    print('Error : Out of range!')


#5
#Import string library to take a string as the uppercase alphabets
import string 

#Taking the input for number of rows 
rows = int(input('Enter the number of rows: '))

#string that contains the alphabet
alpha = string.ascii_uppercase

#Using for loop
for i in range(rows,0,-1):
    #Using another for loop to print the spaces and the alphabets
    for j in range(0,rows-i+1):
        print(end=" ")
    print(alpha[0:(2*i-1)])

#Q6
# Initialising an empty dictionary
stu_details = {}
resp = 'Y'
# Looping to get Name and SID of the students and adding them as key-value pairs to the dictionary
while resp.upper() == 'Y':
    name = input("Enter name of the student: ")
    SID = int(input('Enter SID of the student:  '))
    stu_details.update({SID: name})
    resp = input('Do you want to continue(Y/N)? ')
# Part (a)
print(stu_details)
# Part (b)
print(sorted(stu_details.items(), key=lambda x: x[1]))
# Part(c)
for i in sorted(stu_details):
    print((i, stu_details[i]), end=' ')
    print('\n')
# Part (d)
# Taking name of the student whom details are to be searched
search_SID = int(input('Enter SID of the student to be searched: '))
if search_SID in stu_details:
    print('Name of the student: ', stu_details[search_SID])
else:
    print('Student details with this SID is not present in the hash.')

# Q7

#Taking input for the terms required.
print("Question 7")
Total_Terms=int(input("Enter the number of fibonacci terms you want:- \n"))
First_Term=0
Next_Term=1
Nth_Term=0
Sum=0
#Using for loop to get the n terms

for i in range(1,Total_Terms+1):
    
    if(i==1):
        print(0)
    elif (i==2):
        print(1)
        Sum=Sum+1
    else:
        Nth_Term=First_Term+Next_Term
        Sum=Sum+Nth_Term
        print(Nth_Term)
        First_Term=Next_Term
        Next_Term=Nth_Term
print("The Average of the numbers is:-", float(Sum/Total_Terms))

print()
print("-"*80)
print()

# Q8
# Initialising Sets 
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# Part (a)
Part_a = Set1 ^ Set2
print('Part a: ', Part_a)
# Part (b)
Part_b = Set1 ^ Set2 ^ Set3
print('Part b: ', Part_b)
# Part (c)
Part_c = Set1 & Set2 | Set2 & Set3 | Set1 & Set3
print('Part c: ', Part_c)
# Part (d)
Part_d = set(range(1, 11)) - Set1
print('Part d: ', Part_d)
# Part (e)
Part_e = Part_d - Set2 - Set3
print('Part e: ', Part_e, '\n')