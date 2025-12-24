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
    if  letra in "capitalletters":
     capitalletters = True
    if  letra in "lowercase":
     lowercase = True
    if letra in "number":
     number = True
    if letra in "special":
     special = True

desire_length = 16
max_attemps = 50
attemps= 0
secure_password = ""


while attemps < max_attemps:
    attemps += 1
    password = "your secure password: "
    
    character_sets = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "abcdefghijklmnopqrstuvwxyz",  
        "1234567890",
        "!#$%&/()¡."
    )
    
    all_characters = []
    for char_sets in character_sets:
        for character in character_sets:
            all_characters.append(character)   
    
    for _ in range(desire_length):
       secure_password += random.choice (all_characters)

       character_types = {
         "capitalletters" : character_sets[0],
         "lowercase" : character_sets[1],
         "numbers" : character_sets[2],
         "special" : character_sets[3],
         }
       
       criteria_met = {"capitalletters" : False, "lowercase": False, "numbers": False, "special": False}

       for charcater in secure_password:
          for type_name, char_set in character_types.items():
             if character in char_set:
                criteria_met[type_name] = True

                if all(criteria_met.values()):
                   break

print(f"\nImproved password:{secure_password}")
print(f"Length:{len(secure_password)}characters")

type_counts =  {"capitalletters" : 0, "lowercase": 0, "numbers": 0, "special": 0}

for character in secure_password:
    if character in character_types["capitalletters"]:
     type_counts["capitalletters"]+=1
    elif character in character_types["lowercase"]:
     type_counts["lowercase"]+=1
    elif character in character_types["numbers"]:
     type_counts["numbers"]+=1
    elif character in character_types["special"]:
     type_counts["special"]+=1

print("\nCharacter distribution:")
count_items = list(type_counts.items())
index = 0
while index < len(count_items):
   character_type, count = count_items[index]
   print(f" {character_type}: {count }")
   index += 1

final_statistics = (
   f"generated password:{secure_password}",
   f"total length:{len(secure_password)} characteres",
   f"capitalleters: {type_counts["capitalletters"]}",
   f"lowercase: {type_counts["lowercase"]}",
   f"numbers: {type_counts["numbers"]}",
   f"special: {type_counts["special"]}",
   f"generated attemps: {attemps}",
   f"ls secure: {all(type_counts.values()) and len(secure_password)>=15}"
)

print( "\n" + "="*50 )
print("final tuple with statistics:")
print("=50")
for item in final_statistics:
   print(f"·{item}")

   
     










    

    
  