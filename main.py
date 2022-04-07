from tkinter import *
import random
from tkinter import messagebox

colors = ['Red', 'Blue', 'Green', 'Black', 'Pink',  'Orange', 'Yellow', 'Purple', 'White', 'Brown']

score: int = 0
timeleft: int = 60

def startGame(event):
  if timeleft == 60:
    countdown()
  nextcolor()

def countdown():
  global timeleft
  if timeleft == 0:
    messagebox.showinfo('Time Left: ', 'Time is over and Your score is ' + str(score))
  if timeleft > 0:
    timeleft -= 1
    timeLabel.config(text='Time Left: ' + str(timeleft))
    timeLabel.after(1000, countdown)


def nextcolor():
  global score, timeleft

  if timeleft > 0:
    e.focus_set()
    if e.get().lower() == colors[1].lower():
      score += 1

    e.delete(0,END)
    random.shuffle(colors)

    label.config(fg = str(colors[1]), text = str(colors[0]))
    scoreLabel.config(text = 'Score: ' + str(score))


root = Tk()
root.title('Color Game')
root.geometry('375x200')
root.resizable(0,0)

instruction = Label(root, text='Введите цвет слова, and not the word text', font=('Arial', 12))
instruction.pack()

scoreLabel = Label(root, text='Press Enter to start', font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = Label(root, text = 'Time Left: ' + str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

label = Label(root, font=('Helvetica', 60))
label.pack()

e = Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()