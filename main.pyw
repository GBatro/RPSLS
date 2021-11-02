from tkinter import Button
from tkinter import Tk
from functools import partial
from RPSLS import options
from RPSLS import RPSLS

class main:
  root = Tk()
  root.title("RPSLS")
  root.minsize(100,130)
  root.geometry("200x130")

  runRPSLS = RPSLS.runRPSLS

  rockButton = Button(root, text="Rock", command=partial(runRPSLS,options[0]), bg="grey")
  paperButton = Button(root, text="Paper", command=partial(runRPSLS,options[1]), bg="white")
  scissorsButton = Button(root, text="Scissors", command=partial(runRPSLS,options[2]), bg="red")
  lizardButton = Button(root, text="Lizard", command=partial(runRPSLS,options[3]), bg="forestgreen")
  spockButton = Button(root, text="Spock", command=partial(runRPSLS,options[4]), bg="royalblue")

  rockButton.pack(side="top", fill="x")
  paperButton.pack(side="top", fill="x")
  scissorsButton.pack(side="top", fill="x")
  lizardButton.pack(side="top", fill="x")
  spockButton.pack(side="top", fill="x")

  root.mainloop()