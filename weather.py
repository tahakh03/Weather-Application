from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=27affb5776c8fdf26481741f0525563c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    description = description.capitalize()
    temp = int(json_data['main']['temp']-273.5)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|", "FEELS", "LIKE", temp, "°"))
    
    w.config(text=(wind, "km/h"))
    h.config(text=(humidity, "%"))
    d.config(text=description)
    p.config(text=(pressure, "kPa"))


#search box
search_image = PhotoImage(file="searchbox.png")
myImage = Label(image=search_image)
myImage.place(x=20, y=20)
textfield = tk.Entry(root, justify="left",width=24,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=47,y=40)
textfield.focus()

#search icon
search_icon = PhotoImage(file="searchicon.png")
search_icon = search_icon.subsample(9, 9)
myImageIcon=Button(image=search_icon, borderwidth=0, cursor="hand2", command=getWeather)
myImageIcon.place(x=420,y=31)

#logo

logo_image=PhotoImage(file="logo.png")
logo_image = logo_image.subsample(3, 3)
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#Bottom Box

frame_image = PhotoImage(file="display_box.png")
frame_my_image = Label(image=frame_image)
frame_my_image.pack(padx=5,pady=5,side=BOTTOM)


#label

label1 = Label(root, text="WIND", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label2.place(x=280,y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label3.place(x=440,y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica",15,'bold'), fg="white", bg="#1ab5ef")
label4.place(x=660,y=400)

t = Label(font=("arial", 70, "bold"), fg = "#ee666d")
t.place(x=400,y=160)

c = Label(font=("arial", 15, "bold"))
c.place(x=400,y=150)

w=Label(text="...", font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...", font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...", font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=440,y=430)

p=Label(text="...", font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=660,y=430)


root.mainloop()
