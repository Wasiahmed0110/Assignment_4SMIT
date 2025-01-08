# Assignment 1
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print(vowel_count)

# Assignment 2
string = input("Enter a string: ")
uppercase = sum(1 for char in string if char.isupper())
lowercase = sum(1 for char in string if char.islower())
digits = sum(1 for char in string if char.isdigit())
whitespace = sum(1 for char in string if char.isspace())
print(uppercase, lowercase, digits, whitespace)

# Assignment 3
string = input("Enter a string: ")
new_string = string[-1] + string[1:-1] + string[0] if len(string) > 1 else string
print(new_string)

# Assignment 4
string = input("Enter a string: ")
reversed_string = "".join(string[i] for i in range(len(string) - 1, -1, -1))
print(reversed_string)

# Assignment 5
string = input("Enter a string: ")
shifted_string = string[1:] + string[0] if len(string) > 1 else string
print(shifted_string)

# Assignment 6
name = input("Enter your full name: ")
initials = "".join(f"{char}. " for char in name if char.isupper()).strip()
print(initials)

# Assignment 7
string = input("Enter a string: ")
is_palindrome = all(string[i] == string[len(string) - 1 - i] for i in range(len(string) // 2))
print("Palindrome" if is_palindrome else "Not Palindrome")

# Assignment 8
string = "SHIFT"
for i in range(len(string)):
    shifted = string[i:] + string[:i]
    print(shifted)

# Assignment 9
password = input("Enter a password: ")
valid = (
    len(password) >= 8
    and any(char.isupper() for char in password)
    and any(char.islower() for char in password)
    and any(char.isdigit() for char in password)
)
print("Valid password" if valid else "Invalid password")
