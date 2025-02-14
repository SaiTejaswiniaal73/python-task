# 1. If else and if else ladder
# a. Easy Questions:
# i. Write a program to check if a given number is positive,
# negative, or zero.
number_to_check=int(input("enter a number to know  +ve,-ve or zero: "))
if number_to_check>0:
    print(" given number is postive")
elif number_to_check==0:
    print(" given number iszero")
else:
    print("given number isnegative")

# ii. Determine if a number is odd or even.
if number_to_check%2==0:
    print("given number iseven")
else:
    print("given number isodd")
# iii. Check if a person is eligible to vote (age >= 18).
person_age=int(input("enter your age: "))
eligible_result='he can vote' if person_age>18 else 'he cannot vote'
print(eligible_result)
# iv. Write a program to find the greatest of two numbers.

num1=int(input("enter a number to know greatest of two numbers "))
num2=int(input("enter a number to know  greatest of two numbers "))
check_greater_num='num1 is grate rthen num1' if num1>num2 else 'num2 is greater than num2'
print(check_greater_num)

# v. Print "Pass" if a student scores more than 40 marks;# otherwise, print "Fail."

student_marks=float(input("enter student marks"))
if student_marks>40:
    print("you a pass")
else:
    print("you ar fail")

# vi. Write a program to display the day of the week based on a
# number input (1 for Monday, 2 for Tuesday, etc.).

def get_day(num):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[num - 1] if 1 <= num <= 7 else "Invalid input! Enter a number between 1 and 7."

num = int(input("Enter a number (1-7): "))
print(get_day(num))

# num = int(input("Enter a number (1-7): "))

# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else:
#     print("Invalid input! Enter a number between 1 and 7.")


# vii. Implement a simple calculator to perform addition,
# subtraction, multiplication, and division.

def simple_operation(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
print(simple_operation(10,15))

# viii. Write a program to display the name of a month based on
# the month number (1 for January, 2 for February, etc.).

num = int(input("Enter a month number (1-12): "))

if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("March")
elif num == 4:
    print("April")
elif num == 5:
    print("May")
elif num == 6:
    print("June")
elif num == 7:
    print("July")
elif num == 8:
    print("August")
elif num == 9:
    print("September")
elif num == 10:
    print("October")
elif num == 11:
    print("November")
elif num == 12:
    print("December")
else:
    print("Invalid input! Enter a number between 1 and 12.")

# b. Medium Questions:

# i. Write a program to find the greatest of three numbers.

number1=int(input("enter your num : "))
number2 =int(input("enter your num : "))
number3 =int(input("enter your num : "))
if(number1>number2  and number1>number3 ):
    print("num1 is big")
elif(number1==number2  and number1==number3 ):
    print("all are equal")
elif(number2 >number1 and number2 >number3 ):
    print("num2 is big")
else:
    print("num3 is big")

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))
# number3 = int(input("Enter your third number: "))

# if number1 > number2 and number1 > number3:
#     print(f"The greatest number is: {number1}")
# elif number2 > number1 and number2 > number3:
#     print(f"The greatest number is: {number2}")
# elif number3 > number1 and number3 > number2:
#     print(f"The greatest number is: {number3}")
# else:
#     print("All numbers are equal")

    
# ii. Check if a year is a leap year.

year=int(input("enetr a year number: "))
o_p='given year i leap' if (year%100!=0 and year%4==0) or (year %400==0) else 'it is not leap year'
print(o_p)

# if (year%100!=0 and year%4==0) or (year %400==0):
#     print("leap year")
# else:
#     print("not a leap year")

# iii. Write a program to classify a character entered by the user
# as a vowel, consonant, or neither.

user_string = input("Enter a character: ").lower()

if len(user_string) != 1 :
    print("I need only one character")
else:
    if user_string in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    elif user_string.isalpha():
        print("Consonant")
    elif user_string.isalnum():
        print("number")
    else:
        print("NOT a alphabet")

# iv. Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail.

marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Fail")



# v. Write a program to check if three sides length form a valid
# triangle.

side1 = int(input("Enter first side length: "))
side2 = int(input("Enter second side length: "))
side3 = int(input("Enter third side length: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Triangle is possible")
else:
    print("Triangle is not possible")


#loops

#  a. Easy Questions:
# i. Print all numbers from 1 to 100 using a for loop.
# i=0
for i in range(1,101):
    print(i)
# ii. Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)
n = int(input("Enter a number: "))
sum_n = 0
for i in range(1, n + 1):  
    sum_n += i
print(f"Sum of first {n} natural numbers is: {sum_n}")

# iii. Print all even numbers between 1 and 50 using a while2

# num = 2
# while num <= 50:  
#     print(num, end=" ")  
#     num += 2  

num = 2
while num <= 50 and num%2==0:  
    print(num, end=" ")  
    num += 2  


# loop.
# iv. Write a program to display the multiplication table of a given
# number. First 20

num = int(input("Enter a number: "))

# for i in range(1, 21):
#     print(f"{num} x {i} = {num * i}")

i=1
while(i<=20):
    print(f"{num}*{i}={num*1}")
    i=i+1
# v. Reverse a number using a while loop.
num = input("Enter a number: ")  
rev = num[::-1]  # Reverse the string  

print("Reversed number:", rev)  
