import customtkinter
import time
import math
import pygame
from PIL import Image,ImageTk
from threading import *
from tkinter import *

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")
root=customtkinter.CTk() 

root.title('music player')
root.geometry("500x700")

pygame.mixer.init()

song_list=['music/_Aabaad_Barbaad__Abhishek_B,_Aditya_K,_Rajkummar_R,_Sanya_M,_Fatima_S__Arijit,_Pritam,Sandeep(256k).mp3',"music/Lehanga_Mashup__-_Punjabi__Gurashish_Singh_ft._Kuhu_Gracia_I_Tanveer_Singh_Kohli__(256k).mp3","music/Raabta__Kuch_to_hai_tujhse_raabta(256k).mp3"]
n=0
photo=ImageTk.PhotoImage(file='img/music1.png')
img1=Label(root,image=photo,anchor=customtkinter.CENTER).place(x=50,y=40)

def progress():
    a=pygame.mixer.Sound(f'{song_list[n]}')
    song_len=a.get_length()*3
    for i in range(0,math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos()/10000000)

def thread():
    t1=Thread(target=progress)
    t1.start()

def play_music():
    thread()
    global n
    current_song=n
    if n>2:
        n=0
    song_name=song_list[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover=(song_name,n)
    print('PLAY')
    n +=1

def skip_forward():
    play_music()

def skip_back():
    global n
    n-=2
    play_music()

def volume(value):
    pygame.mixer.music.set_volume(value)

label=customtkinter.CTkLabel(master=root,text="music_player")
label.place(relx=0.5,rely=0.6,anchor=customtkinter.CENTER)

button=customtkinter.CTkButton(master=root,text="play",command=play_music)
button.place(relx=0.5,rely=0.7,anchor=customtkinter.CENTER)

skip=customtkinter.CTkButton(master=root,text="  >  ",command=skip_forward,width=2)
skip.place(relx=0.7,rely=0.7,anchor=customtkinter.CENTER)

skip_b=customtkinter.CTkButton(master=root,text="  <  ",command=skip_back,width=2)
skip_b.place(relx=0.3,rely=0.7,anchor=customtkinter.CENTER)

slider = customtkinter.CTkSlider(master=root,width=160,height=16,border_width=5.5,command=volume)
slider.place(relx=0.5,rely=0.78,anchor=customtkinter.CENTER)

progressbar=customtkinter.CTkProgressBar(master=root,width=260,height=10,border_width=2,progress_color="lightgreen")
progressbar.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

root.mainloop()


