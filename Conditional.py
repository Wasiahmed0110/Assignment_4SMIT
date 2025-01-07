# 1
number = int(input())
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2
age = int(input())
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 3
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(num1)
else:
    print(num2)

# 4
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 5
age = int(input())
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 6
day = int(input())
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Error: Invalid input")

# 7
weight = float(input())
height = float(input())
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

# 8
mark1 = float(input())
mark2 = float(input())
mark3 = float(input())
average = (mark1 + mark2 + mark3) / 3
if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else:
    print("F")

# 9
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)
    print(root1, root2)
elif d == 0:
    root = -b / (2 * a)
    print(root)
else:
    print("Complex roots")

# 10
nums = sorted([int(input()) for _ in range(3)])
print(*nums)

# 11
nums = [int(input()) for _ in range(3)]
print(max(nums))

# 12
char = input().lower()
if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 13
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("NOT a Leap Year")

# 14
calls = int(input())
if calls <= 100:
    bill = 200
elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60
elif calls <= 200:
    bill = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40
print(bill)