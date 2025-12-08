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

if len(password) >= 15:
    print ("longitud correcta")
else:
    print ("longitud incorrecta")
for letra in password:
    if  letra in "capitalletters" :
     capitalletters = True
    if  letra in "lowercase" :
     lowercase = True
    if letra in "number" :
     number = True
    if letra in "special" :
     special = True
    




