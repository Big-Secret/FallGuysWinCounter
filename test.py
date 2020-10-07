from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
import os.path
import keyboard
import webbrowser
import re

versionNo = "v1.1"

def getWins():
    file = open("FallGuysWin.txt", "r")
    wins = file.readline()
    wins = re.sub("\D", "", wins)
    wins = int(wins)
    print(wins)

getWins()