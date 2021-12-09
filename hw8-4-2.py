# Author: CMOB 12/8/2021

from random import randint


def rock_paper_scissors():
    
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)
       
        p_again = str.capitalize(input("Play again? Y or N  "))


        # Check if the user or the computer won.
        if player == computer:
            print("It's a tie!")
            return "tie"
            tie += 1
        elif player == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
                return "loss"
                loss += 1
            else:
                print("You win, rock crushes scissors!\n")
                return "win"
                win += 1
        elif player == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
                return "loss"
                loss += 1
            else:
                print("You win, paper covers rock!\n")
                return "win"
                win += 1
        elif player == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
                return "loss"
                loss += 1
            else:
                print("You win, scissors cuts paper!\n")
                return "win"
                win += 1



rock_paper_scissors()