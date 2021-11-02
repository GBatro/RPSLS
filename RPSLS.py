from random import choice
import tkinter.messagebox as popup

options = [ ("Rock", 1), 
              ("Paper", 2), 
              ("Scissors", 3), 
              ("Lizard", 4), 
              ("Spock", 5)]

class RPSLS:
  def winner(player1, player2):
    players = [player1, player2]

    if player1[1] == player2[1]:
      return "n/a"
    elif abs(player1[1] - player2[1]) in (1,3):
      return max(players)[0]
    else:
      return min(players)[0]

  def runRPSLS(player1):
    player2 = choice(options)
    winningText = f"The winner was {RPSLS.winner(player1, player2)}! \n\nPlayer 1: {player1[0]} \nPlayer 2: {player2[0]}"
    popup.showinfo("Winner", winningText)