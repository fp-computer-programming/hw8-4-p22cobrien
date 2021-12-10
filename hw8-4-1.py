# Author: CMOB 12/8/2021

from random import randint

def num_game():
    

    while True:
        player = input("Please enter a number between 0 & 50 ")
        computer = randint(0, 50)

        if player != "stop":
            if int(player) == computer:
                print("You guessed the number. The number was {0} and you geussed {1}".format(computer, player))
                break
            elif int(player) < computer:
                print("You guessed wrong. The answer is higher. Try again.")
            elif int(player) > computer:
                print("You guessed wrong. The number is lower. Try again.")
        elif player == "stop":
            print("The number was {0}".format(computer))
            break

num_game()
