import random

card_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
print("Blackjack program started.")

users_card=[]
computers_card=[]

users_card.append(random.choice(card_list))
users_card.append(random.choice(card_list))
computers_card.append(random.choice(card_list))
computers_card.append(random.choice(card_list))

print(f"users card : {users_card}")
print(f"computers card : {computers_card}")

def blackjack():
    users_card_total=0
    computers_card_total=0
    for card_value in users_card:
        users_card_total+=card_value
        
    for card_value in computers_card:
        computers_card_total+=card_value

    print(users_card_total)
    print(computers_card_total)

    if users_card_total==21 or computers_card_total==21:
        if users_card_total==21 and computers_card_total==21 :
            print("Draw.")
            return
        elif users_card_total==21 :
            print("You win.")
            return
        elif computers_card_total==21 :
            print("You lose.")
            return

    else:
        if users_card_total > 21:
            print("You lose.")
            return
        else:
            another_card=input("Do you want to get annother card : ")
            if(another_card=='yes'):
                users_card.append(random.choice(card_list))
                print(f"users card : {users_card}")
                blackjack()
            else:
                while(computers_card_total<17):
                    computers_card.append(random.choice(card_list))
                    print(f"users card : {users_card}")
                    print(f"computers card : {computers_card}")
                    computers_card_total+=computers_card[-1]
                    if(computers_card_total>21):
                        print("You win.")
                        return
                if users_card_total>computers_card_total :
                    print("You win.")
                elif users_card_total<computers_card_total :
                    print("You lose.")
                else:
                    print("Draw.")
                    
blackjack()
