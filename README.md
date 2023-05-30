
# MIT PROBLEM SET

This repository contains my solutions to the problem sets from the MIT course "Introduction to Computer Science and Programming in Python." Each problem is designed to test your problem-solving skills and Python programming proficiency.

Feel free to explore the folders and files corresponding to each assignment to find the solutions. Remember to understand the logic behind the solutions and try solving the problems on your own first.

## PROBLEM SET 1 

This problem set introduces you to using control flow in Python and formulating a computational solution to a problem. It will also give you the chance to explore bisection search.


### Part A: House Hunting 

The objective of this part is to determine the number of months it will take you to buy your dream house.

### How to use 
To use this program, you need to provide the following inputs:

1. annual_salary: Your annual salary as a floating-point number.
2. portion_saved: The portion of your salary to be saved each month as a decimal value (e.g., 0.1 for 10%).
3. total_cost: The total cost of your dream house as a floating-point number.
4. The program will calculate the number of months it will take to save for a down payment on the house, assuming an annual return on investments of 4% (monthly return of 0.04/12).

### File Structure

- `problem_set_1a.py`: The main Python script that contains the the part a implementation.

**Note**
Please note that this program assumes a constant monthly salary and does not consider factors like raises or changes in savings rate.


### Part B: Saving, with a raise 

The objective of this part is to determine the number of months it will take you to buy your dream house if your salary raises every six months.

### How to use 
To use this program, you need to provide the following inputs:

1. annual_salary: Your annual salary as a floating-point number.
2. portion_saved: The portion of your salary to be saved each month as a decimal value (e.g., 0.1 for 10%).
total_cost: The total cost of your dream house as a floating-point number.
3. semi_annual_raise: The raise in your salary every six months as a decimal value (e.g., 0.05 for 5%).
4. The program will calculate the number of months it will take to save for a down payment on the house, assuming an annual return on investments of 4% (monthly return of 0.04/12). It also considers the semi-annual raise in your salary.

### File Structure

- `problem_set_1b.py`: The main Python script that contains the the part b implementation.

**Note** 
Please note that this program assumes a constant monthly savings rate and does not consider factors like changes in savings rate or variations in investment returns over time.


### Part C: Finding the right amount to save away.

The objective of this part is to write a program to calculate the best savings rate, as a function of your starting salary. You should use bisection search to help you do this efficiently.

### How to use 

To use this program, you need to provide your starting salary as a floating-point number.

The program will calculate the best savings rate, as a function of your starting salary, that will allow you to save enough money for a down payment on a house within 36 months. It uses bisection search to efficiently find the savings rate that achieves a savings amount close to the down payment (within a tolerance of 100).

### File Structure

- `problem_set_1c.py`: The main Python script that contains the the part c implementation.

**Note**

Please note that this program assumes a constant monthly savings rate, semi-annual raises, and an annual return on investments of 4%. It also assumes a fixed total cost of the house. You can modify these assumptions according to your specific requirements.

### Project Design Responsibilities

- `problem_set_1a.py, problem_set_1b.py, problem_set_1c.py`: The main Python scripts that contains the the part a, b, c implementation.


## PROBLEM SET 2: THE HANGMAN GAME

This Hangman Game is a simple text-based implementation of the classic game. Players have to guess letters to uncover a hidden word within a limited number of guesses.

### How to Play

1. Run the Python script `problem_set_2.py` to start the game.
2. The program will select a random word from the word list and display the number of letters in the word as underscores.
3. Enter a letter as your guess and press Enter.
4. If the letter is correct and exists in the word, it will be revealed in its correct position(s).
5. If the letter is incorrect, you will lose a guess and the incorrect guess will be displayed.
6. Repeat steps 3-5 until you guess the entire word or run out of guesses.
7. The game ends when either all the letters in the word are guessed correctly or the number of guesses reaches zero.
8. After the game ends, your total score will be displayed. The score is calculated as the product of the number of guesses remaining and the number of unique letters in the word.
9. The random word that you were trying to guess will also be displayed.

### File Structure

- `problem_set_2.py`: The main Python script that contains the Hangman game implementation.
- `words.txt`: A text file containing a list of words that the game randomly selects from.

### Project Design Responsibilities

- `problem_set_2.py`: The main Python script that contains the Hangman game implementation.


## PROBLEM SET 3: Scrabble Game

This code implements a basic version of the Scrabble game. The game involves dealing a hand of letters to players, who then construct words using those letters. Each valid word earns the player points based on the length of the word and the letters used.

### How to Play

1. Run the Python script `problem_set_3.py` to start the game.
2. You will be prompted to enter the total number of hands you want to play.
3. For each hand:
   - A hand of random letters will be dealt to you.
   - You can view your current hand and its letters.
   - Optionally, you can choose to substitute one letter in your hand with a new letter.
   - Enter a word you want to create using the letters in your hand.
   - Repeat the previous two steps until you are finished or enter '!!'.
   - The code will check if the word is valid (exists in the provided word list) and if the letters used are available in your hand.
   - If the word is valid, the score for the word will be displayed.
   - Your hand will be updated based on the word played.
4. After all hands are played, the total score earned will be displayed.

### Files Structure

- `problem_set_3.py`: The main Python script that contains the scrabble game implementation.
- `words.txt`: A file containing a list of valid words used for checking the validity of words played.
- `test_ps3.py`: A file containing a test for the functions `get_word_score()`, `update_hand()`, `is_valid_word()`,`wildcard()` and `load_words()`.

### Test Implementation

To execute the test file `test_ps3.py`, please follow the steps below:

1. Ensure that you have downloaded the `test_ps3.py` file and placed it in the same directory as the entire `problem_set_3` file structure.
2. Import the necessary functions from the `problem_set_3.py` file that you intend to test. By default, the implementation imports everything from the problem set file.
3. Comment out the last lines containing the `play_game()` function inside the `problem_set_3.py` file.
4. Run the code inside the test file `test_ps3.py`.

Please note that these steps assume you have the required dependencies and a compatible Python environment set up. Make sure to fulfill any prerequisites or installation requirements before executing the test file.

### Project Design Responsibilities 

- `problem_set_3.py`: The main Python script that contains the scrabble game implementation.


## PROBLEM SET 4: String Permutations and Ciphers

### Part A: String Permutations 

This problem set focuses on generating permutations of a given string. The function uses a recursive approach to generate permutations by selecting a starting letter from the input string, generating permutations of the remaining letters, and inserting the starting letter at different positions within each permutation.

### How to Use

1. Open the file `problem_set_4a.py` in a Python environment.
2. Call the `get_permutations()` function, passing a string as the sequence parameter.
3. The function will return a list containing all the permutations of the input string.

### File Structure

`problem_set_4a.py`: The main Python script that contains the `get_permutations()` function.

**Note** 

The `get_permutations()` function has a time complexity of O(n!), where n is the length of the input string. Take this into consideration when using it with large strings, as the number of permutations grows exponentially with the length of the input.


## Part B: Cipher Like Caesar

A Caesar cipher is a simple method of encryption where each letter in the plaintext message is shifted a certain number of positions down the alphabet. This is an implementation of object-oriented programming.

### How to Use

1. Open the file `problem_set_4b.py` in a Python environment.
2. You will find the following classes:
    - Message: The base class that contains common attributes and method for encryption and decryption.
    - PlaintextMessage: A subclass of Message that represents a message in its original form (plaintext).
    - CiphertextMessage: A subclass of Message that represents an encrypted message (ciphertext).
3. Use the provided methods within the classes to perform the desired operations. 

### File Structure

- `problem_set_4b.py`: The main Python script that contains the implementation of classes `Message`, `PlaintextMessage`, and `CiphertextMessage`.
- `words.txt`: A text file containing a list of words.

**Note**

- Keep the files `words.txt` and `story.txt` in the same folder `problem_set_4b.py` for the solution to function correctly.

## Part C: Substitution Cipher Encryption and Decryption

This problem set focuses on implementing a substitution cipher encryption and decryption algorithm. The encryption algorithm creates a transpose dictionary based on a given permutation of vowels and applies it to a message, while the decryption algorithm attempts to decrypt the message by trying different permutations and checking the validity of the resulting words.

### How to Use

1. Open the file `problem_set_4.py` in a Python environment.
2. Import the `get_permutations()` functions from the `problem_set_4a.py` 
3. Run the script.
.
### File Structure

- `problem_set_4c.py`: The main Python script that contains the of classes `SubMessage` and `EncryptedSubtMessage` : Inherits from SubMessage and represents an encrypted message..
- `words.txt`: A text file containing a list of words.
`problem_set_4a.py`: The main Python script that contains the `get_permutations()` function.

**Note**
- The `load_words()` function may take a while to finish depending on the size of the word list.
- The `get_permutations()` function used in problem_set_4a.py has a time complexity of O(n!), where n is the length of the input string.

### Project Design Responsibilities 

- `problem_set_4a.py, problem_set_4b.py, problem_set_4c.py`: The main Python scripts that contains the the part a, b, c implementation.

## PROBLEM SET 5: RSS Feed Filter

This problem set involves creating an RSS feed filter using the provided code. The code is designed to fetch news items from RSS feeds, parse them, and apply filters based on triggers to retrieve specific stories. The filters include phrase triggers for title and description, as well as time triggers for filtering stories published before or after a specified time.

### How to Use

1. Ensure you have Python installed on your system.
2. Download or clone the code repository to your local machine.
3. Make sure you have the necessary dependencies installed. The code relies on the `feedparser`, `string`, `time`, `threading`, `datetime`, `pytz`, `mtTkinter`, and `project_util` libraries.
4. Open a terminal or command prompt and navigate to the directory containing the code files.
5. Run the `problem_set_5a.py` script using Python
6. The program will fetch news items from the Google Top Stories RSS feed and display them in a graphical interface.
7. You can modify the triggers by editing the `triggers.txt` file. Please refer to the problem set instructions for the trigger configuration syntax.

### File Structure

The file structure of the project is as follows:

`problem_set_5a.py`: The main script file that fetches, parses, and filters news items from the RSS feed.
- `project_util.py`: A utility module containing helper functions for translating HTML and other project-specific functions.
- `mtTkinter.py`: A modified version of the Tkinter library used for the graphical interface.
- `triggers.txt`: A configuration file where you can specify the triggers for filtering the news items. Please follow the specified syntax.
- `ps5_test.py`:  A file containing a test for the class and methods desing inside tne `problem_set_5a.py`. 

### Test Implementation

To execute the test file `ps5_test.py`, please follow the steps below:

1. Ensure that you have downloaded the `ps5_test.py` file and placed it in the same directory as the entire `problem_set_5a` file structure.
2. Import the necessary functions from the `problem_set_5a.py` file that you intend to test. By default, the implementation imports everything from the problem set file.
3. Run the code inside the test file `ps5_test.py`.

Please note that these steps assume you have the required dependencies and a compatible Python environment set up. Make sure to fulfill any prerequisites or installation requirements before executing the test file.

**Note**

Please ensure that you are using a Python version lower than 3.9.x to avoid compatibility issues with the `feedparser.py` provided by the MIT.

### Project Design Responsibilities 

- `problem_set_5a.py`: The script implementation until the problem 10.