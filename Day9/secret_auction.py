import os
from art import logo

print(logo)
print("Welcome to the secret auction program")

bid_record={}
end_of_game=False

while not end_of_game:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: "))
    
    bid_record[name]=bid
    choice=input("Are there any other bidders? Type 'yes' or 'no'. ")
    
    if choice=='no':
        end_of_game=True
        highest_bid=-1
        winner=""
        for bidder in bid_record:
            bid_amount=bid_record[bidder]
            if bid_amount>highest_bid:
                highest_bid=bid_amount
                winner=bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
    else:
        os.system('cls')