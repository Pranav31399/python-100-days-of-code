# instagram followers comparision

from game_data import data
from art import logo
from art import vs
import random

print(logo)

data_length=len(data)

a=data[random.randint(0,data_length-1)]

current_score=0
end_of_game=False

while not end_of_game:
    b=data[random.randint(0,data_length-1)]
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    choose=input("Who has more followers? Type 'A' or 'B': ").lower()
    if a['follower_count'] >= b['follower_count'] and choose=='a':
        current_score+=1
        print(f"\nYou're right! Current score: {current_score}.\n")
        a=b
    elif b['follower_count'] >= a['follower_count'] and choose=='b':
        current_score+=1
        print(f"\nYou're right! Current score: {current_score}.\n")
        a=b
    else:
        end_of_game=True
        print(f"\nYou're wrong! Final score: {current_score}.\n")
    

