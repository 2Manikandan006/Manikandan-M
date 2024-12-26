import random
from random_list import words
from man_pose import stages 

def get_words():
    lives = 6
    random_words = random.choice(words)
    print(f"Hint: the word starts with {random_words[0]}")
    
    display = [random_words[0]]
    for i in range(1, len(random_words)):
        display += '_'  
    print(display)

    game_over = False
    
    while not game_over:
        guess_word = input("Enter your guess: ").lower()
        for position in range(len(random_words)):
            letter = random_words[position]
            if letter == guess_word:
                display[position] = guess_word
        print(display)
        
        if guess_word not in random_words:
            lives -= 1
            if lives == 0:
                game_over = True
                print("The game is over!.. you lose...")
        if '_' not in display:
            game_over = True
            print("Guess you win!... Congratulation")
        print(stages[lives])

get_words()


