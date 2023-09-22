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

    def evaluate_word(testInput, word):
        tempWORD = []
        tempINPUT = []
        tempINDEX = []
        outputMap = {}

        #Creates Map for first pass
        for i in range(5):
            outputMap[i] = "_"


        wordMap = {}
        inputMap = {}

        for i in range(5):
            show = [word[i], testInput[i]]
            if word[i] == testInput[i]:
                outputMap[i] = "G"
            else:
                tempINPUT.append(testInput[i])
                tempINDEX.append(i)
                tempWORD.append(word[i])

        for i in range(len(tempWORD)):
            if tempWORD[i] in wordMap:
                wordMap[tempWORD[i]] += 1
            else:
                wordMap[tempWORD[i]] = 1

        for i in range(len(tempINPUT)):
            if tempINPUT[i] in inputMap:
                inputMap[tempINPUT[i]] += 1
            else:
                inputMap[tempINPUT[i]] = 1

        for i in range(len(tempINDEX)):
            if tempINPUT[i] in tempWORD and wordMap[tempINPUT[i]] > 0:
                outputMap[tempINDEX[i]] = 'Y'
                wordMap[tempINPUT[i]] -= 1
            
        output = ""
        for i in range(5):
            output += outputMap[i]

        return output

    def enter_action(s):
        current_row = gw.get_current_row()
        s = s.lower()

        if s == "":
            return
        
        if s in FIVE_LETTER_WORDS:
            result = evaluate_word(s, selected_word)

            for col in range(N_COLS):
                if result[col] == "G":
                    gw.set_square_color(current_row, col, gw.correct_color)
                elif result[col] == "Y":
                    gw.set_square_color(current_row, col, gw.present_color)
                else:
                    gw.set_square_color(current_row, col, gw.missing_color)

            if result == "GGGGG":
                gw.show_message("Congratulations! You've won! The word was: " + selected_word)
            elif current_row == 5:
                gw.show_message("Game over. The word was: " + selected_word)
            else:
                gw.show_message("Try Again")
                gw.set_current_row(current_row + 1)
        else:
            gw.show_message("Not a valid word")

    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()
