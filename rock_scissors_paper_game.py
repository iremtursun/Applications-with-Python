#Collect all the components of your program to run it in a for loop
#Import the random library
import random

#Add the code to create a list containing the three actions of the game.
list=["rock","paper","scissors"]


#Add the code to set the scores of players to 0
score_player_one=0
score_player_two=0


#Add the code to ask the user how many rounds they want to play
rounds = int(input("How many rounds you want to play?"))
counter = 0
#Write a for loop and put the game inside
while True:
  #Add the code to select a random action for each player
  player_one = random.choice(list)
  player_two = random.choice(list)
  if counter < rounds:
    #Add the code to print the players choices
    if player_one != player_two:
      print("Player 1: ",player_one,"Player 2:",player_two)
      if player_one == "rock" and player_two == "paper":
        score_player_two += 1
        #print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
      elif player_one == "rock" and player_two == "scissors":
        score_player_one += 1
        #print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
      elif player_one == "scissors" and player_two == "paper":
        score_player_one += 1
        #print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
      elif player_one == "scissors" and player_two == "rock":
        score_player_two += 1
        #print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
      elif player_one == "paper" and player_two == "rock":
        score_player_one += 1
        #print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
      elif player_one == "paper" and player_two == "scissors":
        score_player_two += 1

    #Add the tie condition
    elif player_one == player_two:
      score_player_one += 0
      score_player_two += 0
      print("Tie! Both players chose the same action.")

    #Add the remaining condition
    else:
      print("This game can't play now.")

    #print the score
    print("Player 1's score: ",score_player_one, "Player 2's score: ", score_player_two)
    counter += 1

    if counter >= rounds:
      break

if score_player_two < score_player_one:
  print("WİNNER: PLAYER 1")
elif score_player_two > score_player_one:
  print("WİNNER: PLAYER 2")
elif score_player_two == score_player_one:
  print("Tie.")