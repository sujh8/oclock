
from cProfile import label
from calendar import month, weekday
from time import time
from tkinter import *
from tkinter import Tk, PhotoImage
from turtle import window_height, window_width
from numpy import true_divide
import pyglet 
from datetime import datetime
from pytz import HOUR
from sklearn.svm import l1_min_c
pyglet.font.add_file('digital-7.ttf')

bc = "#263957"
fc = "#f5f5f5"


window = Tk()
window.title("digital Clock")
window.geometry('440x150+50+50')
window.iconbitmap('calendar.ico')


window.resizable(width=False,height=False)
window.configure(bg=bc)
def clock():
    time = datetime.now()
    hour = time.strftime("%H : %M : %S")
    weekday =  time.strftime("%A")
    day = time.day
    month= time.strftime("%b")
    year = time.strftime("%Y")
    l1.configure(text=hour)
    l1.after(200, clock)
    l2.configure(text=weekday + " " + str(day) + "/" + str(month) + "/"+ str(year))

l1=Label(window, text ="12:49:05" ,font=('digital-7 80'),bg = bc , fg = fc)
l1.grid(row = 0 ,column =0 ,padx=5 ,sticky=NW )

l2=Label(window, text ="sunday  20/7/2022" ,font=('digital-7 20'),bg = bc ,fg = fc)
l2.grid(row = 1,column =0 ,padx=5 ,sticky=NW)
 
clock() 




window.mainloop()