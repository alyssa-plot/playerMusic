import tkinter as tk
import tkinter
from tkinter import *
from tkinter import filedialog
import os
import fnmatch
import pygame

master = tk.Tk()
master.title("Playermusic")
master.geometry("400x500")

pygame.init()

chemin_playlist = "musique/"
patern ="*.mp3"

songs = []
current_song = ""
paused = False
volume = 0.5
def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load("musique/" + playlist.get(playlist.curselection()))
        pygame.mixer.music.play()

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def stop_music():
    pygame.mixer.music.stop()

def add_music():
    global songs
    files = filedialog.askopenfilenames()
    for file in files:
        if file.endswith('.mp3'):
            songs.append(file)
            playlist.insert(END, file)

def delete_music():
    global songs
    selected_indices = playlist.curselection()

    for i in reversed(selected_indices):
        playlist.delete(i)
        songs.pop(i)

def set_volume(val):
    volume = float(val)/100
    pygame.mixer.music.set_volume(volume)

playlist = tkinter.Listbox(master, width=36, font=('Arial', 14))
playlist.grid(columnspan=7, row=1)

#affichage des photos sur les boutons
btn_play = PhotoImage(file="image/play.png")
btn_pause = PhotoImage(file="image/pause.png")
btn_loop = PhotoImage(file="image/loop.png")
btn_stop = PhotoImage(file="image/stop.png")
btn_add = PhotoImage(file="image/add.png")
btn_delete = PhotoImage(file="image/deleted.png")

#Affichage des boutons pour démarrer la musique, la stopper, loop, etc...
btnplay = Button(master,text="play", image=btn_play,width=60,height=80,font=('Arial', 10), command = play_music)
btnplay.grid(column=3, row=6)
btnpause = Button(master,text="pause",image=btn_pause,width=60,height=80, font=('Arial', 10), command= pause_music)
btnpause.grid(column=4 , row=6)
btnloop = Button(master,text="loop",image=btn_loop,width=60,height=80, font=('Arial',10))
btnloop.grid(column=0 , row=6)
btnsstop = Button(master,text="stop", image=btn_stop,width=60,height=80, font=('Arial',10), command = stop_music)
btnsstop.grid(column=5 , row=6)
btnadd = Button(master, text="add a music",image=btn_add,width=60,height=80, font=('Arial',10), command = add_music)
btnadd.grid(column=2 , row=6)
delete_ = Button(master, text="Delete", image=btn_delete,width=60,height=80, font=('Arial',10), command = delete_music)
delete_.grid(columnspan=7 , row=8)

volume_scale = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volume_scale.grid(columnspan=8)

#chemin pour la playlist
for root, dirs,files in os.walk(chemin_playlist):
    for filename in fnmatch.filter(files,patern):
        playlist.insert('end', filename)

def on_closing():
    pygame.mixer.quit()
    master.destroy()

master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()