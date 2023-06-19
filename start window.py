from tkinter import *

start_window = Tk()
start_window.geometry("905x700")
start_window.title("HANGMAN")
start_window.config(bg='#FFFFFF')

def animals_theme():
    exec("import hangman_upgrade_1.py")
    
Animal = Button(text ="Animal Theme", command=animals_theme())
Animal.pack()


def theme1():
    exec("import hangman.py")


def fruits_theme():
    exec("import hangman_upgrade_2.py")
