import random
import string

capitalletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special = "!#$%&/()¡."
chars = capitalletters + lowercase + number + special

print("your secure password: ")
password = " "
for x in range(16): 
    password += random.choice(chars)
print(password)

