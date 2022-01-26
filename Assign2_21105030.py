#Q1
#Taking input from the user
string_1 = "Python is a case sensitive language"
print(len(string_1))
print(string_1[::-1])
string_2 = string_1[10:26]
string_2 = "object oriented"
print(string_2)
print(string_1.find("a"))
print(string_1.replace(" ", ""))

#Q2
name = 'Akshaj Paintola'
SID = 21105030
department_name = "ECE"
CGPA = '9.9'
print("Hey, %s Here!" %(name))
print("My SID is %d" %(SID))
print("I am from %s department and my CGPA is %s" %(department_name, CGPA))

# Question 3
# Initiating a and b with values 56 and 10 respectively.
a = 56
b = 10
# Implementing bit-wise operator and (&)
print('Calculated a&b = ', a & b)
# Implementing bit-wise operator or (|)
print('Calculated a|b = ', a | b)
# Implementing bit-wise operator xor (^)
print('Calculated a^b = ', a ^ b)
# Implementing left shift bit-wise operator
print(f'After left shifting both a and b by 2 bits, a = {a<<2} and b = {b<<2}.')
# Implementing right shift bit-wise operator
print(f'After right shifting a with 2 bits and b with 4 bits, a = {a>>2} and b = {b>>4} \n \n')

# Question 4
# Taking input of the three numbers as integers
first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
third_num = int(input('Enter the third number: '))
# Applying the logic using if else statements and printing the greatest number of the three.
# It first compares the first number with the second and then with the third returning whichever is the greatest.
if first_num > second_num:
       if first_num > third_num:
          print('The greatest  number is: ',  first_num,'\n\n')
       else: 
           print('The greatest  number is: ', third_num, '\n\n')
# If the second number is greater than the first than it compares it with third number and returns the greatest number.
elif second_num > third_num:
         print('The greatest  number is: ', second_num, '\n\n')
else:
    print('The greatest  number is ', third_num, '\n\n')

#Q5
user_input=input("Give a word:")
if("name"in user_input):
    print("Yes")
else:
    print("No")

#Q6
len_1 = int(input('Write the length of first side: '))
len_2 = int(input('Write the length of second side: '))
len_3 = int(input('Write the length of third side: '))
if len_1 + len_2 < len_3 or len_2 + len_3 < len_1 or len_3 + len_1 < len_2:
    print('No')

else:
    print('Yes')