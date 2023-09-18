# File: Wordle.py
#Hey there
#test test test 
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    gw = WordleGWindow()
    selected_word = random.choice(FIVE_LETTER_WORDS)
    selected_word = selected_word.lower()
    print("Randomly selected word:", selected_word) #Prints the five letter word in the console, not necessary for production but helping for testing.

    def enter_action(s):
        current_row = gw.get_current_row()
        s = s.lower()  # Convert the entered word to lowercase for case-insensitive comparison

        if s == "":
            # If the input string is empty or contains only whitespace, do nothing
            return
        #Gathers array of letters
        correct_letter = []
        present_letter = []
        missing_letter = []
        if s in FIVE_LETTER_WORDS:
            if s == selected_word:
                for col in range(N_COLS):
                    guess_letter = s[col]
                    word_letter = selected_word[col]

                    if guess_letter == word_letter: 
                        correct_letter.append(col)
                    for col in correct_letter:
                        gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                gw.show_message("You've won! The word was: " + selected_word)
            else:
            # Determine the colors for each square

                for col in range(N_COLS):
                    guess_letter = s[col]
                    word_letter = selected_word[col]

                    if guess_letter == word_letter: 
                        correct_letter.append(col)
                    elif guess_letter in selected_word:
                        present_letter.append(col)
                    else:
                        missing_letter.append(col)
                #loops through arrays to color letters
                for col in correct_letter:
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                for col in present_letter:
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                for col in missing_letter:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    
                if gw.get_current_row() == 5 :
                    gw.show_message("Game over")
                else: gw.show_message("Try Again")
            gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not a valid word")

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
