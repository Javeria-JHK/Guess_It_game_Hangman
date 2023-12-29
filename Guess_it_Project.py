import random
import pyfiglet
name = input("What is your name? ")
title = pyfiglet.figlet_format("GUESS  IT", font="bubble")
print("Hello, " + name, "Time to play")
print(title)
print("Help and save Hangman")
print(" ")
points = 0
# ranges are given
a = (1, 2, 3, 4, 5, 6)
b = (7,7)
c = (8, 9, 10, 11, 12)

print("Your points = ", points)
print(" ")
print("""a = (1, 2, 3, 4, 5, 6)                                                                                       
b = (7)                                                                                                            
c = (8, 9, 10, 11, 12)""")
response = 1
print(" ")
while points < 50:
    used_lives = 0
    if response == 1:
        print("Lets start!")
        response = 0

        while used_lives < 3:
            if used_lives == 1:
                print(""" 
                      |-------|
                      |       |
                      |       O
                      |      \|/
                      |       |
                      |      | |
                      |       #
                      |       #
                      |      
                                  """)
            elif used_lives == 2:
                print(""" 
                      |-------|
                      |       |
                      |       O
                      |      \|/
                      |       |
                      |      | |
                      |       #
                      |      
                      |      
                                  """)

            else:
                print(""" 
                      |-------|
                      |       |
                      |       O
                      |      \|/
                      |       |
                      |      | |
                      |       #
                      |       #
                      |       #
                                  """)

            number_dice1 = random.randint(1, 6)
            number_dice2 = random.randint(1, 6)
            SUM = number_dice1 + number_dice2
            used_lives += 1
            choosed_range = eval(input("Guess the sum of two dice number "
                                       "and choose the option in which your guess lies:- 'a<7,b=7 and c>7': ").lower())

            if SUM in choosed_range:
                print("You WON!")
                print("Great!!! you saved the Hangman")
                print("10 points increased")
                points = points + 10
                print("your points = ", points)
                print("You want to Play Again?")
                response = int(input("If yes enter 1 , if No enter 0: "))
                break
            else:
                points = points - 5
                if used_lives == 3:
                    continue
                else:
                  print("Try AGAIN! next time")
        else:
            print("you Loose!")
            print(""" 
                  |-------|
                  |       |
                  |       O
                  |      \|/
                  |       |
                  |      | |
                  |       
                  |       
                  |       
                              """)
            print("sorry! Hangman Died")
            print("your points = ", points)
            print("You want to Play Again?")
            response = int(input("If yes enter 1 , if No enter 0: "))
    else:
        print(f"Total points: {points}")
        print("Thanks!")
        exit()