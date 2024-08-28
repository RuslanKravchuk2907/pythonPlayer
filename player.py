import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Music Player")
player.geometry("310x325")

var = tkinter.StringVar()
var.set("Select the song to play")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player, font="Helvetica 12 bold", width=30, bg="black", fg="white", selectmod=tkinter.SINGLE)

for item in songlist:
    playing.insert(0, item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    var.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player, font="Helvetica", textvariable=var).grid(row=0, columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Play", command=play, bg="green").grid(row=2, column=0)
pauseB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Play", command=play, bg="red").grid(row=2, column=0)
resumeB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Play", command=play, bg="blue").grid(row=2, column=0)

player.mainloope