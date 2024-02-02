from art import logo

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def encrypt_decrypt(choice):
    print(choice)
    word=input("Type your message : ")
    shift_amount=int(input("Type the shift number : "))
    plain_text=""
    for letter in word:
        position=alphabet.index(letter)
        new_position=position
        if choice=='encode':
            new_position+=shift_amount
        elif choice=='decode':
            new_position-=shift_amount
        new_letter=alphabet[new_position%26]
        plain_text+=new_letter
    print(f"Here's the {choice}d result : {plain_text}")
        
print(logo)
end_of_cipher=False

while(not end_of_cipher):
    choice1=input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()   
    if choice1=='encode' or choice1=='decode':
        encrypt_decrypt(choice1)
        choice2=input("Type 'yes' if you want to go again. Otherwise type 'no' : ").lower()
        if choice2=='yes':
            end_of_cipher=False
        else:
            end_of_cipher=True
    else:
        print("Wrong input. Type 'encode' to encrypt, type 'decode' to decrypt : ")
    
    
    