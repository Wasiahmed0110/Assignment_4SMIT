# 1
for i in range(1, 11):
    print(i)

# 2
i = 20
while i > 0:
    print(i)
    i -= 1

# 3
for i in range(2, 11, 2):
    print(i)

# 4
n = int(input())
for i in range(1, n + 1):
    print(i)

# 5
n = int(input())
for i in range(1, n + 1, 2):
    print(i)

# 6
for _ in range(5):
    print("Happy Birthday!")

# 7
n = int(input())
print(" ".join(str(i ** 2) for i in range(1, n + 1)))

# 8
n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 9
start, diff = 3, 4
for i in range(8):
    print(start + i * diff, end=" ")
print()

# 10
start, ratio = 2, 3
term = start
for _ in range(6):
    print(term, end=" ")
    term *= ratio
print()

# 11
n = int(input())
print(sum(range(1, n + 1)))

# 12
n = int(input())
print(f"The sum of reciprocals from 1 to {n} is: {sum(1 / i for i in range(1, n + 1)):.2f}")

# 13
total = 0
for _ in range(5):
    total += int(input())
print(f"The final running total is: {total}")

# 14
n = int(input())
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

# 15
base = int(input())
exponent = int(input())
result = 1
if exponent < 0:
    base = 1 / base
    exponent = -exponent
for _ in range(exponent):
    result *= base
print(result)
