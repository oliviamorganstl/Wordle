# File: Wordle.py
#Hey there
#test test test 
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):

        s = s.lower()  # Convert the entered word to lowercase for case-insensitive comparison
        
        if s in FIVE_LETTER_WORDS:
            gw.show_message("Congratulations! You guessed a valid word: " + s)
            if s == selected_word.lower():
                gw.show_message("You've won! The word was: " + selected_word)

        else:
            gw.show_message("Not in word list")

    def select_random_word(word_list): #Brings in the 5 letter words as a parameter then picks one.
        random_word = random.choice(word_list)
        return random_word


    selected_word = select_random_word(FIVE_LETTER_WORDS)
    print("Randomly selected word:", selected_word) #Prints the five letter word in the console, not necessary for production but helping for testing.


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    for i in range(len(selected_word)): #i is the column number
        letter = selected_word[i]
        gw.set_square_letter(0, i, letter) #we are assuming row 0 in the parameter

# Startup code

if __name__ == "__main__":
    wordle()
