# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from colorconfig import (
    DEFAULT_CORRECT_COLOR,
    DEFAULT_PRESENT_COLOR,
    DEFAULT_MISSING_COLOR,
    NEW_CORRECT_COLOR,
    NEW_PRESENT_COLOR,
    NEW_MISSING_COLOR,
    CURRENT_CORRECT_COLOR,
    CURRENT_PRESENT_COLOR,
    CURRENT_MISSING_COLOR,
)

UNKNOWN_COLOR = "#FFFFFF"       # Undetermined letters are white

def wordle():
    gw = WordleGWindow(DEFAULT_CORRECT_COLOR, DEFAULT_PRESENT_COLOR, DEFAULT_MISSING_COLOR)
    selected_word = random.choice(FIVE_LETTER_WORDS)
    selected_word = selected_word.lower()
    print("Randomly selected word:", selected_word) 

    def enter_action(s):
        current_row = gw.get_current_row()
        s = s.lower()

        if s == "":
            return
        
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
                    gw.set_square_color(gw.get_current_row(), col, gw.correct_color)
                gw.show_message("You've won! The word was: " + selected_word)
                replay_wordle(gw)

            else:
                for col in range(N_COLS):
                    guess_letter = s[col]
                    word_letter = selected_word[col]

                    if guess_letter == word_letter: 
                        correct_letter.append(col)
                    elif guess_letter in selected_word:
                        present_letter.append(col)
                    else:
                        missing_letter.append(col)

                for col in correct_letter:
                    gw.set_square_color(gw.get_current_row(), col, gw.correct_color)
                for col in present_letter:
                    gw.set_square_color(gw.get_current_row(), col, gw.present_color)
                for col in missing_letter:
                    gw.set_square_color(gw.get_current_row(), col, gw.missing_color)

                if gw.get_current_row() == 5:
                    gw.show_message("Game over")
                    replay_wordle(gw)

                else:
                    gw.show_message("Try Again")
                    gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not a valid word")

    gw.add_enter_listener(enter_action)

# def select_default_color_scheme():
#     global CORRECT_COLOR
#     global PRESENT_COLOR
#     global MISSING_COLOR
#     CORRECT_COLOR = "#66BB66"       # Light green for correct letters
#     PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
#     MISSING_COLOR = "#999999"       # Gray for letters that don't appear
#     print("Func", CORRECT_COLOR)



# def select_new_color_scheme():
#     global CORRECT_COLOR
#     global PRESENT_COLOR
#     global MISSING_COLOR
#     CORRECT_COLOR = "#3366FF"       # Alternate: Blue
#     PRESENT_COLOR = "#FF9900"       # Alternate: Orange
#     MISSING_COLOR = "#808080"       # Alternate: Medium gray
#     print("Func", CORRECT_COLOR)
           

if __name__ == "__main__":
    wordle()
