from ast import pattern
from cProfile import label
from cgitb import text
from email.mime import image
from email.policy import default
from fileinput import filename
from importlib.metadata import files
from logging import root
from msilib.schema import ListBox
from pickle import FRAME
from select import select
from tkinter import*
import tkinter as tk
import fnmatch
import os
from tkinter import font
import numpy
from pygame import mixer

raiz=tk.Tk()

raiz.resizable(True,True)

raiz.iconbitmap (r"C:\Users\Luis\Documents\Tareas\poo\Reproductor de musica\anime.ico")

raiz.title("McReproductor")

raiz.geometry("800x600")

raiz.config(bg="Blue")  


Rootpath = "C:\\Users\Luis\Documents\Musica"
pattern = "*.Mp3"

Anterior_img=tk.PhotoImage (file="anterior.gif")
Pausa_img=tk.PhotoImage (file="Pausa.gif")
Siguiente_img=tk.PhotoImage (file="Siguiente.gif")
Stop_img=tk.PhotoImage (file="Stop.gif")
Play_img=tk.PhotoImage (file="Play.gif")

def select():
    label.config(text=ListBox.get("anchor"))
    mixer.music.load(Rootpath)
    

Listbox=tk.Listbox(raiz,fg="black",bg="white", width=100, font=(14))
Listbox.pack(padx=15,pady=15)

label=tk.Label(raiz, text = "", bg="blue", fg="yellow", font=(18))
label.pack(pady=15)

top =tk.Label(raiz, bg="blue")
top.pack(padx=10,pady=5, anchor= "center")

BotonAnterior= tk.Button(raiz,text ="Anterior",image=Anterior_img, bg="green",borderwidth=10)
BotonAnterior.pack(pady=20, in_=top, side= "left")

BotonPausa= tk.Button(raiz,text = "Pausa",image=Pausa_img, bg="orange",borderwidth=10)
BotonPausa.pack(pady=20, in_=top,side= "left")

BotonPlay= tk.Button(raiz,text = "Play",image=Play_img, bg="yellow",borderwidth=10)
BotonPlay.pack(pady=20, in_=top,side= "left")

BotonSiguiente= tk.Button(raiz,text = "Siguiente",image=Siguiente_img, bg="red",borderwidth=10)
BotonSiguiente.pack(pady=20, in_=top,side= "left")

BotonStop= tk.Button(raiz,text = "Stop",image=Stop_img, bg="green",borderwidth=10)
BotonStop.pack(pady=20, in_=top,side= "left")

miFrame=Frame()
miFrame.pack()
miFrame.config(bg="black")
miFrame.config(width="600",height="300")
miFrame.pack(side="top")  

for root, dirs, files in os.walk(Rootpath):
    for filename in fnmatch.filter(files, pattern):
        Listbox.insert("end", filename)
        
raiz.mainloop()