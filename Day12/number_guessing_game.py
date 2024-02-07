import random
from art import logo

answer=random.randint(0,100)

print(logo)
print("Welcome to the Number Guessing Game!")
choice=input("Choose a difficulty. Type 'easy' or 'hard' : ")

if choice=='easy':
    attempts=10
elif choice=='difficult':
    attempts=5

while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number=int(input("Make a guess: "))
    if guessed_number>answer:
        print("Too high.")
    elif guessed_number<answer:
        print("Too low.")
    else:
        print(f"You got it. The answer was {answer}")
        break
    attempts-=1
    if attempts==0 :
        print("You have ran out of attempts. You lost.")