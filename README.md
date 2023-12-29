# Guess_It_game_Hangman
This repository contains the simple python guessing game mixed with hangman.

1- The name of the game is Guess It! 

2- In every turn, two dices are rolled and display numbers. 

3- User must guess the sum of these two numbers, whether it lies in “a”, “b” or “c”. 

    “a” contains 1 to 6 numbers, “b” contains number 7 and “c” contains numbers 8 to 12. 

4- Our main purpose is to save the hangman. 

5- Hangman has 3 lives. 

6- There are three bricks belove the hangman, if the user guesses correctly, the hangman will be saved, and points increased. 

7- If the user guesses wrong, one brick will be removed from below the hangman, I show that 1 life is taken. 

8- If the user guesses wrong consecutively three times, the hangman will die. 

9- Then again the computer will ask the user if he wants to play again and displays the total points otherwise 

10- for running this game:
```bash
pip install pyfiglet
python Guess_it_Project.py


