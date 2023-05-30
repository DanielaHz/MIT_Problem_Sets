# PROBLEM SET 3, THE SCRABBLE GAME.

import math
import string
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

WORDLIST_FILENAME = 'problem_set_3\words.txt'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end='')
    print()


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))
    hand['*'] = 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def dictionary_comprehension(new_hand):
    """
    This function is for compress a dictionary.
    this give the user a clear view of the available 
    letters and how many he have to still playing.
    """

    dictionary_to_compress = new_hand
    comprehension = {
        k: v for (k, v) in dictionary_to_compress.items() if v > 0}
    return comprehension


def is_word_in_word_list(word, hand, wordlist):
    """
    This function validates is the input word <word> is a real one.
    """
    word = word.lower()
    return word in wordlist


def are_word_letters_in_hand(word, hand, wordlist):
    """
    This fuction check if the input <word> was made it ONLY whit letters in <hand>.
    Note: if the user input is a word with any aditional letter he will lose all the 
    letter that match with the hand and off course he will lose the points even if the 
    word is real.
    """

    x = word.lower()
    y = hand.copy()
    for letter in x:
        if letter in y and y[letter] > 0:
            y[letter] -= 1
        else:
            return False
    return True


def is_valid_word(word, hand, wordlist):
    if is_word_in_word_list(word, hand, wordlist) and are_word_letters_in_hand(word, hand, wordlist) == True:
        return hand


def remove_words_from_hand(word, hand, wordlist):
    """
    This function remove the words that match with the dictionary <hand> and call the function
    dictionary_comprehension. Return the new dictionary.
    """
    for w in word:
        if w in hand.keys():
            hand[w] = hand[w] - 1
            hand = dictionary_comprehension(hand)
    return hand


def update_hand(word, hand, wordlist):
    """This fuction update the dictionary hand.
    """
    word = word.lower()
    validation = is_valid_word(word, hand, wordlist)
    if validation is not None:
        hand_copy = hand.copy()
        update = remove_words_from_hand(word, hand_copy, wordlist)
        return update
    return hand


def replace_vowel(word, hand, wordlist):
    word = word.lower()
    if '*' in word:
        wildcard_wordlist = []
        for char_vow in VOWELS:
            wildcard_word = word.replace('*', char_vow)
            wildcard_wordlist.append(wildcard_word)
        return wildcard_wordlist
    else:
        return [word]


def is_valid_word(word, hand, wordlist):
    word = word.lower()
    wildcard_words = replace_vowel(word, hand, wordlist)
    for wildcard_word in wildcard_words:
        if is_word_in_word_list(wildcard_word, hand, wordlist) and are_word_letters_in_hand(wildcard_word, hand, wordlist):
            return hand
    return False


def get_word_score(word, HAND_SIZE):
    """This function calculates the score of any word created for hand.
    The formula gives a higher score in function of the word lenght <n> and the letters used, remmeber that any word have a respective value"""
    total_first_comp = 0
    total_second_comp = 0
    long_word = len(word)
    for n in range(long_word):
        letter = word[n].lower()
        first_comp = SCRABBLE_LETTER_VALUES.get(letter)
        if first_comp is not None:
            total_first_comp += first_comp

    second_comp_1 = 7 * long_word
    second_comp_2 = (3 * (HAND_SIZE - long_word))
    total_second_comp = abs(second_comp_1 - second_comp_2)
    total = total_first_comp * total_second_comp
    return total


def game_over(word, total_general):
    """
    This function will stop the game when the user inputs the string <!!>. 
    """
    if word == '!!':
        print('Total score:', total_general, 'points.')
        print('Thanks for playing')
        exit()


def draw_letter():
    """
    Randomly selects and returns a letter from a pool of available letters.
    """
    letter_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return random.choice(letter_pool)


def substitute_hand(hand, letter):
    """
    This function substitutes a letter in the hand with a new letter.
    """
    substitute_hand = hand.copy()

    if letter in substitute_hand:
        remove_letter = substitute_hand.pop(letter)
        new_letter = draw_letter()
        substitute_hand[new_letter] = substitute_hand.get(new_letter, 0) + 1
    else:
        print("Letter not found in the hand.")

    return substitute_hand


def substitution_process(hand):
    """
    This function allows the user to change only one letter inside a current word.
    """
    print('Do you want to change any letter in your hand? Please enter 1 for Yes or 2 for No')

    while True:
        try:
            confirmation = int(input())
            if confirmation == 1:
                letter = input('Enter the letter you wish to change: ')
                substitution = substitute_hand(hand, letter)
                print("Modified hand: ", substitution)
                return substitution
            elif confirmation == 2:
                return hand
            else:
                print("Invalid input. Please enter either 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer (1 or 2).")


# GAME INFRASTRUCTURE


def play_game():
    print('!!!WELCOME TO THE SCRABBLE GAME!!!')
    print('The basic idea is to make a new word with the hand of letters we give you to play.')
    print('The longer the word is, much better. !!MORE POINTS FOR YOU!!')
    print('READY?. !!Lests get started!!')
    print('------------------------------------------------------------------------------------')
    wordlist = load_words()
    print('First, enter total number of hands: ')
    number_hands = int(input())
    print('------------------------------------------------------------------------------------')
    total_general = 0
    # NOTEE : The number_hands is how many times you want to play in a contining way with a new hand any time.

    while number_hands > 0:
        total_points = 0
        hand = deal_hand(HAND_SIZE)
        list_keys = hand.keys()
        llk = len(list_keys)

        while llk > 1:
            print('Current hand:', hand)
            print('Display current hand:')
            display_hand(hand)
            substitution_process(hand)
            print('Enter word, or "!!" to indicate that you are finished:')
            word = input('')
            game_over(word, total_general)
            is_valid_word(word, hand, wordlist)
            hand = update_hand(word, hand, wordlist)
            list_keys1 = hand.keys()
            llk = len(list_keys1)
            score = get_word_score(word, HAND_SIZE)
            print('the word', '*', word, '*' 'earned', score, 'points')
            print(
                '------------------------------------------------------------------------------------')
            total_points = total_points + score
            game_over(word, total_points)
        total_general = total_general + total_points
        number_hands -= 1

    print('Total score:', total_general, 'points.')
    print('Thanks for playing')


# if you want to run the test_ps3.py file, please make sure to comment the next function `play_game()``. Remember this is the function game
# and it executes the game infrastructure!!!!
play_game()
