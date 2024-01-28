import random

numbers=["rock","paper","scissor"];
your_choice=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. : "))
computer_choice=random.randint(0,2)
print(f"Your choice {numbers[your_choice]}, computer choose {numbers[computer_choice]}")

if your_choice==0:
    if computer_choice==1:
        print("computer wins")
    elif computer_choice==2:
        print("you win.")
    else:
        print("draw.")
elif your_choice==1:
    if computer_choice==0:
        print("you win")
    elif computer_choice==2:
        print("computer wins.")
    else:
        print("draw.")
else:
    if computer_choice==0:
        print("computer wins.")
    elif computer_choice==1:
        print("you win.")
    else:
        print("draw.")
        

