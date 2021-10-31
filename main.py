import os
import random


def erase_screen():
    os.system("cls")

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
    with open("./files/WORDS.txt","r", encoding="utf-8") as f:
        words = [word for word in f]
    return words


def choose_word(list_words):
    chosen_word = random.choice(list_words)
    return(chosen_word)


def game_logic(answer):
    lifes = 9
    original_answer = answer
    show_answer = "_" * len(original_answer)
 
    while (lifes > 0):
        print(show_answer)
        user_answer = input('Enter a letter: ')
        if user_answer in answer:
            pass



def instructions():
    print('''
    Instructions:
    1. Count the number of lines that will appear, this will be the numbers of characters that the word has.
    2. When the system ask you for a letter enter one to see if the word contain it.
    3. If the letter is not in the word you will loose a life.
    4. You will have 9 lifes, wich means 9 attends to guesst the word    
    ''')


def run():
    erase_screen()
    welcome_print()
    answer = choose_word(open_data())


if __name__ == '__main__':
    run()
