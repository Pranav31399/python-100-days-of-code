import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','_']
numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to password generator.")
no_of_letters=int(input("How many letters would you like in your password. : "))
no_of_symbols=int(input("How many symbols would you like. : "))
no_of_numbers=int(input("How many numbers would you like. : "))

password_list=[]

for char in range(0,no_of_letters+1):
    password_list.append(random.choice(letters))
    
for char in range(0,no_of_symbols+1):
    password_list.append(random.choice(symbols))
    
for char in range(0,no_of_numbers+1):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

password=""

for char in password_list:
    password+=char
    
print(f"Here is your password : {password}")

