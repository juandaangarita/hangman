import os
import random

HANGMAN = {
    "0": """
 ____
|/   |
|    |
|    
|    
|    
|    
|
|_____
""",
    "1":
        """
 ____
|/   |
|    |
|   (_)
|    
|    
|    
|
|_____
""",
    "2":
        """
 ____
|/   |
|    |
|   (_)
|    |
|    |    
|    
|
|_____
""",
    "3":
        """
 ____
|/   |
|    |
|   (_)
|   \|
|    |
|    
|
|_____
""",
    "4":
        """
 ____
|/   |
|    |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
    "5":
        """
 ____
|/   |
|    |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
    "6":
        """
 ____
|/   |
|    |
|   (_)
|   \|/
|    |
|   / \.
|
|_____
""",
    "7":
        """
 ____
|/   |
|    |
|   (_)
|   /|\.
|    |
|   | |
|
|_____
"""
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_print():
    print('''

             _   _                                         
            | | | |                                        
            | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |                      
                               |___/                       


    Welcome!!! The goal of this game is to guesst the hidden word.'''
          )
    instructions()
    input('''    
    Good luck!!!

    Press enter key to start'''
          )


def open_data():
    with open("./files/WORDS.txt", "r", encoding="utf-8") as f:
        words = [word for word in f]
    return words


def open_hangpics():
    with open("./files/HANGMANPICS.txt", "r", encoding="utf-8") as f:
        pics = f
    return pics


def choose_word(list_words):
    chosen_word = random.choice(list_words)
    return chosen_word.strip()


def game_logic(data_list):
    lifes = 7
    original_answer = choose_word(data_list).upper()
    show_answer = list("_" * len(original_answer))
    while lifes > 0:
        clear()
        instructions()
        print(HANGMAN.get(str(7 - lifes)))
        print(f'The word has {len(original_answer)} characters\n\n')
        print(' '.join(show_answer))
        print(f'\nYou have {lifes} lifes')
        user_answer = input('\n\nEnter just one letter: ').upper()
        if len(user_answer) > 1:
            input('\n\nRemember only enter one letter! \n\nPress enter to keep playing')
        elif not user_answer.isalpha():
            input('\n\nRemember only enter alphabetic characters! \n\nPress enter to keep playing')
        elif user_answer in show_answer:
            input(f'\n\nYou already enter the letter {user_answer}. \n\nPress enter to keep playing')
        elif user_answer not in original_answer:
            lifes -= 1
        else:
            for count, element in list(enumerate(original_answer)):
                if user_answer == element:
                    show_answer[count] = user_answer
        if "_" not in show_answer:
            clear()
            print('Congratulations! You win.')
            break
        if lifes == 0:
            clear()
            print('Sorry you could not make it. Try again')
            print(HANGMAN.get(str(7)))
            print(f'The correct answer was: {original_answer}')
            break
    play_again = input('\n\nDo you wanna play again? (Y/n): ').upper()
    if play_again == 'Y':
        game_logic(data_list)
    elif play_again == 'N':
        print('Thank you for playing. Good bye')


def instructions():
    print('''
    Instructions:
    1. Count the number of lines that will appear, this will be the number of characters that the word has.
    2. When the system asks you for a letter enter one to see if the word contains it.
    3. If the letter is not in the word you will lose a life.
    4. You will have 7 lifes, which means 7 attends to guest the word    
    ''')


def run():
    clear()
    welcome_print()
    data_list = open_data()
    game_logic(data_list)


if __name__ == '__main__':
    run()
