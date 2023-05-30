
# PROBLEM SET 4

# Part C: Substitution Cipher

import string
from problem_set_4a import get_permutations
import copy
import random

WORDLIST_FILENAME = 'problem_set_4\words.txt'
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


def load_words(file_name=WORDLIST_FILENAME):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words()

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        copy_self_valid_words = copy.copy(self.valid_words)
        return copy_self_valid_words

    def build_transpose_dict(self, vowels_permutation):
        '''
    vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to an
    uppercase and lowercase letter, respectively. Vowels are shuffled
    according to vowels_permutation. The first letter in vowels_permutation
    corresponds to a, the second to e, and so on in the order a, e, i, o, u.
    The consonants remain the same. The dictionary should have 52
    keys of all the uppercase letters and all the lowercase letters.

    Example: When input "eaiuo":
    Mapping is a->e, e->a, i->i, o->u, u->o
    and "Hello World!" maps to "Hallu Wurld!"

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
        vowels_permutation = get_permutations(VOWELS_LOWER)
        permutation = random.choice(vowels_permutation)

        transpose_dictionary = {}

        for d in VOWELS_LOWER:
            c = VOWELS_LOWER.index(d)
            lower = permutation.lower()
            transpose_dictionary.update({d: lower[c]})

        for e in VOWELS_UPPER:
            j = VOWELS_UPPER.index(e)
            upper = permutation.upper()
            transpose_dictionary.update({e: upper[j]})

        for i in CONSONANTS_LOWER:
            transpose_dictionary.update({i: i})

        for i in CONSONANTS_UPPER:
            transpose_dictionary.update({i: i})

        return transpose_dictionary

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''
        vowels_permutation = get_permutations(VOWELS_LOWER)
        transpose_dict = self.build_transpose_dict(vowels_permutation)
        message = self.get_message_text()
        shift_message = ''
        special = " !:;,.?"

        for c in message:
            if c not in special:
                shift_letter_for_c = transpose_dict.get(c)
                shift_message = shift_message + shift_letter_for_c
            else:
                shift_message = shift_message + c

        return shift_message


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    

        Hint: use your function from Part 4A
        '''
        permutations = get_permutations(VOWELS_LOWER)

        for shift in permutations:

            original_message = ''
            dic = self.build_transpose_dict(shift)
            encrypt_message = self.get_message_text()
            special = " !:;,.?"
            for c in encrypt_message:
                if c not in special:
                    original_letter_for_c = dic.get(c)
                    original_message = original_message + original_letter_for_c
                else:
                    original_message = original_message + c

            test_original_message = original_message.split(" ")
            palabras = load_words()
            count = 0

            for s in test_original_message:
                if is_word(palabras, s) == False:
                    count += 0
                else:
                    count += 1

            x = len(test_original_message)
            y = x / 2

            if y < count <= x:
                test_original_message = ' '.join(test_original_message)
                print('The decrypt messages is: ', test_original_message)
                print(
                    'The number of valid words created with the permutation are:', count)
                print('The permutation is: ', shift)


if __name__ == '__main__':
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(),
          "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    enc_message.decrypt_message()
