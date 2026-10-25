```
HANGMAN GAME (PYTHON)

1. ABOUT THE PROJECT
--------------------
A simple text-based Hangman game that runs in the console.
The computer selects a secret word and the player tries to
guess it one letter at a time before running out of lives.

This project was created as part of a Python programming
internship task.

2. FEATURES
-----------
- Random word selection from a list of 5 predefined words
- Player gets 6 wrong guesses (lives)
- Shows the word as underscores, revealing correct letters
- Shows all letters guessed so far
- Input validation (single letters only)
- Repeated or invalid guesses do not cost a life
- Win / lose message revealing the secret word

3. REQUIREMENTS
---------------
- Python 3.6 or higher (uses f-strings)
- No external libraries needed (only the built-in "random")

4. HOW TO RUN
-------------
1. Save the file as hangman.py
2. Open a terminal / command prompt in that folder
3. Run:

python hangman.py

(On some systems use: python3 hangman.py)

5. HOW TO PLAY
--------------
1. The game shows the word as underscores, e.g. _ _ _ _ _ _
2. Type one letter and press Enter.
3. If the letter is in the word, it is revealed.
4. If not, you lose one life (6 lives in total).
5. You win by revealing every letter of the word.
6. You lose when all 6 lives are used up.

6. SAMPLE OUTPUT
----------------
=== Welcome to Hangman ===

Word: _ _ _ _ _ _
Guessed:
Guess a letter: p
Correct!

Word: p _ _ _ _ _
Guessed: p
Guess a letter: z
Wrong! Lives left: 5

7. WORD LIST
------------
python, internship, program, keyboard, developer

(To add more words, edit the "words" list at the top of
hangman.py.)

8. CONCEPTS USED
----------------
- random module (random.choice)
- while loop with while-else
- if / elif / else conditions
- strings and string methods (lower, isalpha)
- lists (guessed_letters)
- input validation
- all() with a generator expression
- f-strings for formatted output

9. FILE STRUCTURE
-----------------
hangman/
|-- hangman.py  (main game code)
|-- README.txt  (this file)

10. POSSIBLE IMPROVEMENTS
-------------------------
- Add ASCII hangman drawing for each wrong guess
- Load words from an external file
- Add difficulty levels
- Add a "play again" option
- Add a hint feature
=====================================================

Thank you for playing Hangman!
=====================================================