import sys
import random
from rich import print

"""
looks for all the words in certain file
"""
def read_all_words():
    if len(sys.argv) > 1:
        try:
            if 4 < int(sys.argv[1]) < 9:
                try:
                    with open(f'{sys.argv[1]}.txt', 'r') as file:
                        all_words = file.read().split()
                except FileNotFoundError:
                    raise FileNotFoundError(f'No file found for the given number: {sys.argv[1]}')
            else:
                raise ValueError('Number should be between 5 and 8, inclusive')
            
        except ValueError as e:
            print(f'Error: {e}')
            return None
    else:
        print('Error: No argument detected')
        return None
    return all_words

"""
selects single random word
"""
def select_random_word(all_words):

    word = random.choice(all_words)
    print(word)
    
    return word


"""
prompts the user for input
"""
def get_guess(word):
    guess = input("Guess: ").lower()
    if len(word) != len(guess):
        print("Letter count doesn't match.")
        return get_guess(word)
    return guess


"""
iterates over word and checks for correct/wrong letters
"""
def check_guess(guess, word):
    # string for color-coding the word user enters
    # example: RRGYRY (R - red, G - green, Y - yellow)
    colorized_guess = ""

    # loops through both letters and indices in word
    for position, letter in enumerate(guess):
        if guess[position] == word[position]:
            colorized_guess+="G"
        else:
            if letter in word:
                colorized_guess+="Y"
            else:
                colorized_guess+="R"

    return colorized_guess 


"""
prints out the word in correct colors
"""
def color_word(colorized_guess, guess):
    colors = {
        "G": "green",
        "Y": "yellow",
        "R": "red"
    }
    printable_guess = ''

    for position, letter in enumerate(colorized_guess):
        printable_guess += '[' + colors[letter] + ']'+ guess[position]+'[/' + colors[letter] + ']'

    return printable_guess
"""
main logic
"""
def main():
    try:
        print("[yellow]Searches for word list...[/yellow]")
        all_words = read_all_words()
        print("[yellow]Choosing word[/yellow]")
        word = select_random_word(all_words)
    except Exception as e:
        print("Error:", e)

    print("[green]This is WORDLE[/green]")

    # for counting user inputs
    guesses = 0 

    guess = ''

    print(f"[blue]Please give us your guess. {len(word)} letter word: [/blue]")
    # repeats prompting until user guess the word or no more available guesses
    while guess != word: 
        guess = ""

        # gets guess
        guess = get_guess(word)

        # next guess
        guesses += 1 

        colorized_guess = check_guess(guess, word)
        
        # prints colorized word
        print(color_word(colorized_guess, guess))

        if guesses > 5:
            print("No luck today!")
            break
    else:
        # VICTORY!
        print("You guessed the word!")

if __name__ == "__main__":
    main()
