import random as rd
import string

print("Secure Password Generator\nThe Secure Password Generator creates random passwords with uppercase and lowercase letters, numbers, and special characters.")

options = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("Enter the desired password length: "))

password = ""

for i in range(password_length):
    password += rd.choice(options)

print("-" * 30)
print("Your generated password is:\n", password)
print("-" * 30)

input("Press Enter to exit...")
