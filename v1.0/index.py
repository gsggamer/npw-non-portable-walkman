import tkinter
import os
import pygame
from tkinter import filedialog
from tkinter import *
from pygame.locals import *

root_fd = os.path.dirname(__file__)
songs_fd = os.path.join(root_fd, "songs")
main_window = Tk()
main_window.title("NPW (Non-Portable Walkman)")
icon = PhotoImage(file="v1.0/img/icon.png")
main_window.iconphoto(False, icon)
main_window.minsize(800, 600)


def play_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
    song_n = os.path.split(song)
    main_window.title(song_n[1])


def play():
    pygame.mixer.music.unpause()


def pause():
    pygame.mixer.music.pause()


def select_song():
    file_selected = filedialog.askopenfilename(initialdir=songs_fd)
    play_song(file_selected)


play_icon = PhotoImage(file="v1.0/img/play.png")
pause_icon = PhotoImage(file="v1.0/img/pause.png")
select_song_btn = Button(main_window, text="Select song...",
                         command=select_song, relief="solid", borderwidth="1px")

play_song_btn = Button(main_window, image=play_icon, command=play,
                       borderwidth=0)
pause_song_btn = Button(main_window, image=pause_icon, command=pause,
                        borderwidth=0)

select_song_btn.pack()
select_song_btn.place(x=-1, y=-1)
play_song_btn.pack()
play_song_btn.place(x=420, y=200)
pause_song_btn.pack()
pause_song_btn.place(x=330, y=200)
main_window.mainloop()
