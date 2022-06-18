import tkinter, os, pygame
from tkinter import filedialog
from tkinter import *
from pygame.locals import *

root_fd = os.path.dirname(__file__)
songs_fd = os.path.join(root_fd, "songs")
main_window = Tk()
main_window.title("NPW (Non-Portable Walkman)")
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
    file_selected = filedialog.askopenfilename(initialdir="./songs")
    play_song(file_selected)

select_song_btn = Button(main_window, text = "Select song...", command = select_song, relief = "solid", borderwidth = "1px")
play_song_btn = Button(main_window, text = "Play", command = play, relief = "solid", borderwidth = "1px", background = "#9f9")
pause_song_btn = Button(main_window, text = "Pause", command = pause, relief = "solid", borderwidth = "1px", background = "#f99")

select_song_btn.pack()
select_song_btn.place(x=-1, y=-1)
play_song_btn.pack()
play_song_btn.place(x=410, y=200)
pause_song_btn.pack()
pause_song_btn.place(x=340, y=200)
main_window.mainloop()