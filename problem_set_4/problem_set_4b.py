
# PROBLEM SET 4

# Part B : Cipher Like Caesar

import string
import copy

WORDLIST_FILENAME = 'problem_set_4\words.txt'


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


def is_word(wordlist, word):
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
    return word in wordlist


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object
        """
        self.message_text = text
        self.valid_words = load_words()

    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        """
        copy_self_valid_words = copy.copy(self.valid_words)
        return copy_self_valid_words

    def build_shift_dict(self, shift):
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        """
        final_dictionary = {}
        dictionary_upper = {}
        dictionary_lower = {}
        upper_letters_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        upper_letters_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letters_1 = 'abcdefghijklmnopqrstuvwxyz'
        lower_letters_2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        if 0 <= shift < 26:
            for i in range(0, 26):
                dictionary_upper[upper_letters_1[i]] = upper_letters_2[i+shift]
                dictionary_lower[lower_letters_1[i]] = lower_letters_2[i+shift]

        final_dictionary = dict(dictionary_lower, **dictionary_upper)
        copy = final_dictionary.copy()
        return copy

    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        """
        dictionary_shift = self.build_shift_dict(shift)
        message = self.get_message_text()
        shift_message = ''
        special = " !:;,.?"

        for c in message:
            if c not in special:
                shift_letter_for_c = dictionary_shift.get(c)
                shift_message = shift_message + shift_letter_for_c
            else:
                shift_message = shift_message + c

        return shift_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message
        """

        super().__init__(text)
        self.shift = shift
        self.encrypton_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class
        """
        copy_self_encription_dict = copy.copy(self.encrypton_dict)
        return copy_self_encription_dict

    def get_message_text_encrypted(self) -> string:
        """
        Used to safely access self.message_text_encrypted outside of the class
        """
        return self.message_text_encrypted

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        """
        self.shift = shift
        self.build_shift_dict(shift)
        self.apply_shift(shift)


class CiphertextMessage(Message):

    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
        """
        super().__init__(text)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the \"best\" one. We will define \"best\" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.
        """
        palabras = load_words()

        for shift in range(0, 26):

            original_message = ''
            dic = self.build_shift_dict(shift)
            message = self.get_message_text()
            special = " !:;,.?"
            for c in message:
                if c not in special:
                    original_letter_for_c = dic.get(c)
                    original_message = original_message + original_letter_for_c
                else:
                    original_message = original_message + c

            test_original_message = original_message.split(" ")

            count = 0

            for s in test_original_message:
                if is_word(palabras, s) == False:
                    count += 0
                else:
                    count += 1

            if 0 < count <= len(test_original_message):
                test_original_message = ''.join(test_original_message)
                final_tuple = (shift, test_original_message)
                return final_tuple


if __name__ == '__main__':

    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
