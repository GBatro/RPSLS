from random import choice 
from tkinter import *
import tkinter.messagebox
from functools import partial

root = Tk()

options = [("Rock", 1), ("Paper", 2), ("Scissors", 3), ("Lizard", 4), ("Spock", 5)]

def winner(player1, player2):

  players = [player1, player2]

  if player1[1] == player2[1]:
    return "n/a"
  elif abs(player1[1] - player2[1]) in (1,3):
    return max(players)[0]
  else:
    return min(players)[0]

def runRPSLS(decision):
  player2 = choice(options)
  player1 = decision
  winningText = f"The winner was {winner(player1, player2)}! \n\nPlayer 1: {player1[0]} \nPlayer 2: {player2[0]}"
  tkinter.messagebox.showinfo("Winner", winningText)

rockButton = Button(root, text="Rock", command=partial(runRPSLS,options[0]), bg="grey", width=50)
paperButton = Button(root, text="Paper", command=partial(runRPSLS,options[1]), bg="white", width=50)
scissorsButton = Button(root, text="Scissors", command=partial(runRPSLS,options[2]), bg="red", width=50)
lizardButton = Button(root, text="Lizard", command=partial(runRPSLS,options[3]), bg="forestgreen", width=50)
spockButton = Button(root, text="Spock", command=partial(runRPSLS,options[4]), bg="royalblue", width=50)

rockButton.pack(side="top")
paperButton.pack(side="top")
scissorsButton.pack(side="top")
lizardButton.pack(side="top")
spockButton.pack(side="top")

root.mainloop()