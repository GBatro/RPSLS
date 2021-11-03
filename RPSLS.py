from random import choice
import tkinter.messagebox as popup

options = [ ("Rock", 1), 
            ("Paper", 2),
            ("Scissors", 3),
            ("Spock", 4),
            ("Lizard", 5) ]

class RPSLS:
  def winner(player1, player2):
    players = [player1[1], player2[1]]

    if player1[1] == player2[1]:
      return "n/a"
    elif abs(player1[1] - player2[1]) in (1,3):
      return options[max(players)-1][0]
    else:
      return options[min(players)-1][0]

  def runRPSLS(player1):
    player2 = choice(options)
    winningText = f"The winner was {RPSLS.winner(player1, player2)}! \n\nPlayer 1: {player1[0]} \nPlayer 2: {player2[0]}"
    popup.showinfo("Winner", winningText)