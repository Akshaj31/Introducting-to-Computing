#Assignment 1

#Question 1

#Take input for 3 integers and seperate it by useing .split()
a, b, c = input('Write three numbers sepereated by space: ').split()
#The input taken will be in float so convert them into integers 
a = int(a)
b = int(b)
c = int(c)
#Average is the sum of 3 inputs taken and divided by 3. FLoat will be used as average can be decimal
avg = float((a + b + c)/3)
#Printing the code
print('The average of the three numbers is', avg, '\n')

#Question 2

# Input the gross income into a variable
gross_inc = int(input('Enter your Gross Income: '))
# Input for the number of dependents
depend = int(input('Enter number of dependents: '))
# The standard deduction is specified here
std_deduc = 10000
#The deduction per dependent is specified here
additional_deduc = 3000
#Taxable income function is here
taxable_inc = gross_inc - std_deduc - (additional_deduc * depend)
#Rate of interest is 20%
inc_tax = taxable_inc * 0.20
# if else statement to diplay the output
if inc_tax>0:
    print("Your income tax is $", inc_tax, '\n')
    
else:
    print('Your income tax is 0$', '\n')

#Question 3

#we take the inputs individually
Student_SID = input('Write your SID: ')
name = input('Whats your name?: ')
gender = input("Whats your gender(M/F/U): ")
course_name = input("WHat's your course?: ")
cgpa = float(input("Write your CGPA: "))
list1 = [Student_SID, gender, course_name, cgpa]
#finally printing the list
print(list1, '\n')

#Question 4

#Empty list to put all the data into
list1 = []
#Appending all the inputs
list1.append(input('Marks of first student: '))
list1.append(input('Marks of second student: '))
list1.append(input('Marks of third student: '))
list1.append(input('Marks of fourth student: '))
list1.append(input('Marks of fifth student: '))
# .sort() function to sort the list
list1.sort()
# Printing the list
print(list1, '\n')

#Question 5
#Part A

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del colour[3]
print(colour, '\n')

#Part B

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3:5] = ['Purple']
print(colour, '\n')
