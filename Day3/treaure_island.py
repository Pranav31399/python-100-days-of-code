print("Welcome to Treasure Island\nYour mission is to find thr treaure")
direction = input("You are at a cross road, where do you wanna go. Type 'left' or 'right' ")

if direction=="left":
    wait_or_swim=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    
    if wait_or_swim=="wait" :
        color=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if color=="yellow":
            print("You win.")
        elif color=="blue":
            print("You enter a room of beasts. Game Over.")
        elif color=="red":
            print("Game Over.")
        else:
            print("Invalid input.")
        
            
    elif wait_or_swim=="swim" :
        print("Game Over.")
        
elif direction=="right" :
    print("Game Over.")
    
else:
    print("Invalid input")