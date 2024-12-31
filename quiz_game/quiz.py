import random
from questions import quest

def Quiz_game():
    random_question = random.choice(quest)
    print("------------------------------------------")
    print(random_question["question1"])
    for i, option in enumerate(random_question["option"], 1):
        print(f"{i}.{option}")

    guess_answer = input("your answer: ")
    if guess_answer == random_question["Answer"].lower():
        print("correct!..")
    else:
        print("wrong!..")
Quiz_game()