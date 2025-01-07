# 1
lst = input().split()
print(lst[::2])

# 2
lst = input().split()
reversed_lst = lst[::-1]
print(reversed_lst)

# 3
lst = list(map(int, input().split()))
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print(largest)

# 4
lst = input().split()
rotated_lst = lst[1:] + lst[:1]
print(rotated_lst)

# 5
string = input()
word_to_delete = input()
result = string.replace(word_to_delete, "").strip()
print(result)

# 6
date = input()
month, day, year = date.split('/')
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
formatted_date = f"{months[int(month)-1]} {int(day)}, {year}"
print(formatted_date)

# 7
def capitalize_words(string):
    return " ".join(word.capitalize() for word in string.split())

sentence = input()
print(capitalize_words(sentence))

# 8
rows = int(input())
cols = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
for i, row in enumerate(matrix):
    print(f"Sum of row {i + 1} = {sum(row)}")

# 9
rows, cols = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
matrix2 = [list(map(int, input().split())) for _ in range(rows)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
for row in result:
    print(*row)

# 10
rows1, cols1 = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(rows1)]
rows2, cols2 = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(rows2)]

if cols1 != rows2:
    print("Matrix multiplication not possible")
else:
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) 
              for j in range(cols2)] for i in range(rows1)]
    for row in result:
        print(*row)
