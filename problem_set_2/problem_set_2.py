# PROBLEM SET 2, THE HANGMAN GAME.

import random
import string

WORDS = 'problem_set_2\words.txt'


def is_word_guessed(letters_guessed, secret_word):
    """
    This function evaluates if inside a list of inputs provided for the usser <letters_guessed>
    was already guess the <secret_word>. The function returns True or False.
    """
    has_all = all([char in letters_guessed for char in secret_word])
    return has_all


def get_guessed_word(secret_word, letters_guessed):
    """
    This fuction returns a string, comprised of letters with underscores (_), and spaces that 
    represents which letters in secret_word have been guessed so far.
    """
    string = " "
    for c1 in secret_word:
        if c1 in letters_guessed:
            string += c1
        else:
            string += "_"

    return string


def get_available_letters(letters_guessed):
    """
    This function returns string (of letters), comprised of letters that represents which 
    letters have not yet been guessed.
    """
    available = 'abcdefghijklmnopqrstuvwxyz'
    string = " "
    for c in available:
        if c in letters_guessed:
            string += ""
        else:
            string += c
    return string


def input_available(letter_guessed):
    """
    This function validate if the input is a valid string of words
    Return False or True as appropriate.
    """
    available = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not letter_guessed in available:
        return False
    else:
        return True


def take_input():
    """
    This function take an input and return it.
    """
    letter = input('Please introduce a valid letter: ')
    return letter


def penalizes_a_word(letter_guessed, guesses):
    """
    This function penalizes a word if is not a valid input.
    Note: a invalid input are numbers, special characters or empty spaces.
    """

    warnings = 2

    while warnings != 0:
        if input_available(letter_guessed) == False:
            warnings -= 1
            print('Sorry, you lose a warning. Now you have:',
                  warnings, 'warnings left')
            letter_guessed = take_input()
        else:
            letter_guessed = letter_guessed.lower()
            break

    if warnings == 0:
        guesses -= 1

    return letter_guessed

# GAME INFRASTRUCTURE


def hangman():
    words = open(WORDS, 'r')
    line = words.readline()
    list_words = line.split()

    # Seleccionando la palabra random de la lista
    random_word = random.choice(list_words)

    # definiendo la palabra secreta
    secret_word = random_word
    guesses = len(secret_word) + 2

    print('Welcome to the game Hangman!')
    print('I am thinking for a word that is', len(secret_word), 'letters long')
    print('---------------------------------')
    print('You have', guesses, 'guesses left')
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    print('Total available letters: 26 ')
    print('---------------------------------')
    letters_guessed = []
    n_letters = 26

    while is_word_guessed(letters_guessed, secret_word) == False and guesses != 0:
        letter_guessed = input('please guess a letter:')
        new_letter_guessed = penalizes_a_word(letter_guessed, guesses)

        letters_guessed.append(new_letter_guessed)

        if new_letter_guessed in secret_word:
            print('Good guess: ')
            print(get_guessed_word(secret_word, letters_guessed))
            n_letters -= 1

        else:
            print('Oops!', new_letter_guessed, 'is not in my word: ')
            print(get_guessed_word(secret_word, letters_guessed))
            guesses -= 1
            n_letters -= 1

        print('---------------------------------')
        print('You have', guesses, 'guesses left')
        print(get_available_letters(letters_guessed))
        print('Total available letters:', n_letters)
        print('---------------------------------')

    number_unique_letters = len(set(secret_word))
    score = guesses * number_unique_letters
    print('GAME OVER')
    print('your total score is = ', score)
    print('The random word was: ', random_word)


hangman()
