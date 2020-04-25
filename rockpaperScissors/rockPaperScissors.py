'''
Created on Apr 24, 2020

@author: ITAUser
'''
import random

keepPlaying = True

while(keepPlaying == True):
    print("This is rock rock, paper, scissors")
    print("First to 2. Press q to quit. type in lowercase letters")
    #rock is 1, paper is 2, scissors is 3
   
    scoreComp = 0
    scorePlayer = 0
   
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick rock, paper, or scissors")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("it's a draw")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("you lost")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("y")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("Wrong. pick rock, paper, or scissors.")
           
    if (scorePlayer == 2):
            print("you win")
         
           
    if (scoreComp == 2):
            print("I win")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)
