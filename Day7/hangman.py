import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

chosen_word=random.choice(word_list)
word_len=len(chosen_word)


end_of_game=False
lives=6

print(logo)

display=[""]*word_len

# print("the solution is : "+chosen_word)

while not end_of_game:
    guess=input("Guess a letter : ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}")
        
    for position in range(word_len):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if(lives==0):
            end_of_game=True
            print("You lose. Answer was "+chosen_word)
            
    print(f"{' '.join(display)}")
    
    if '' not in display:
        end_of_game=True
        print('You win.')
        
    print(stages[lives])
    


    


# generate as nay blanks as letters in the word

# ask the user to guess a letter 

# is the guessed letter in the word?
# if yes then replace the blank with the letter and check if all the blanks filled if yes then you win and game over, if no then repeat this process
# else you lose a life and check if all the live have run out, if yes then game over and you lose and if no then repeat this process 