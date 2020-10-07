from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
import os.path
import keyboard
import webbrowser
import re

versionNo = "v1.1"
wins = 0

def getWins():
    file = open("FallGuysWin.txt", "r")
    wins = file.readline()
    wins = re.sub("\D", "", wins)
    return wins


def initializeTextFiles():
    file = open("FallGuysWin.txt", "w+")
    initText = f"Total Wins: {wins}\n"\
               f"Wins Today: {fallGuysBot.wins}\n" \
               f"Streak: {fallGuysBot.streak}"
    file.write(initText)
    file.close()

def callback(url):
    webbrowser.open_new(url)

class FallGuysIsDopeTho():
    def __init__(self,TotalWins,Wins,Streak,Games):
        self.totalWins = TotalWins
        self.wins = Wins
        self.streak = Streak
        self.games = Games

    def addWin(self):
        self.wins += 1
        self.streak += 1
        self.totalWins += 1
        winsLabel.config(text=self.wins)
        streakLabel.config(text=self.streak)
        newScore = f"Total Wins: {self.totalWins}\n"\
                   f"Wins Today: {self.wins}\n" \
                   f"Streak: {self.streak}"
        file = open("FallGuysWin.txt", "w+")
        file.write(newScore)
        print(f"File has been written, new wins count is {self.wins}, new streak is {self.streak}, total wins is {self.totalWins}")
    def loseRound(self):
        self.streak = 0
        winsLabel.config(text=self.wins)
        streakLabel.config(text=self.streak)
        newScore = f"Total Wins: {self.totalWins}\n"\
                    f"Wins Today: {self.wins}\n" \
                    f"Streak: {self.streak}"
        file = open("FallGuysWin.txt", "w+")
        file.write(newScore)
        print(f"File has been written, new wins count is {self.wins}, new streak is {self.streak}, total wins is {self.totalWins}")
    def resetScore(self):
        self.wins = 0
        self.streak = 0
        winsLabel.config(text=self.wins)
        streakLabel.config(text=self.streak)
        newScore = f"Total Wins: {self.totalWins}\n"\
                   f"Wins Today: {self.wins}\n" \
                   f"Streak: {self.streak}"
        file = open("FallGuysWin.txt", "w+")
        file.write(newScore)
        print(f"Score Reset, file has been written, new wins count is {self.wins}, new streak is {self.streak}, total wins remains {self.totalWins}")

fallGuysBot = FallGuysIsDopeTho(wins, 0,0,0)

# Hokey Settings
hotkeyUp = "Ctrl+Shift+W"
hotkeyLose = "Ctrl+Shift+L"
hotkeyReset = "Ctrl+Shift+0"

keyboard.add_hotkey(hotkeyUp,fallGuysBot.addWin)
keyboard.add_hotkey(hotkeyLose,fallGuysBot.loseRound)
keyboard.add_hotkey(hotkeyReset,fallGuysBot.resetScore)


# Build UI
# Create Main Window
main = Tk()
main.title(f"ily<3 {versionNo}")
main.resizable(False,False)
#App Icon
mainIconAbs = os.path.abspath("img/AppIcon.png")
mainIcon = PhotoImage(file=mainIconAbs)
main.iconphoto(False,mainIcon)
#App Background
C = Canvas(main, bg="blue", height="101", width="220")
filename = PhotoImage(file = "img/FGBacker.png")
background_label = Label(main, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
# Create top menu
menuBar = Menu(main)
menuBar.add_command(label="🏆 Win 🏆", command=fallGuysBot.addWin)
menuBar.add_separator()
menuBar.add_command(label="😠 Lose 😠", command=fallGuysBot.loseRound)
menuBar.add_separator()
resetMenu = Menu(menuBar, tearoff=0)
resetMenu.add_command(label="Reset Counter", command=fallGuysBot.resetScore)
menuBar.add_cascade(label="Reset", menu=resetMenu)
#Display the menu
main.config(menu=menuBar)
# Font Styles
fontStyle = tkFont.Font(family="Montserrat Black", size=16)
headerFont = tkFont.Font(family="Montserrat", size=30)
# Streak Label
streakLabel = Label(main, text="0", font=fontStyle)
streakLabel.configure(background="#0178E6", foreground="White")
streakLabel.place(x=183,y=29)
# Wins Label
winsLabel = Label(main, text="0", font=fontStyle)
winsLabel.configure(background="#DF61F2", foreground="White")
winsLabel.place(x=183,y=67)
#Version Label
versionLabel = Label(main,text=("©BigSecret"))
versionLabel.configure(background='#DF61F2', foreground='white')
versionLabel.place(x=5,y=90,anchor="w")
versionLabel.bind("<Button-1>", lambda e: callback("https://www.twitch.tv/bigsecret"))


# Run app
if __name__ == '__main__':
    getWins()
    initializeTextFiles()
    main.mainloop()
