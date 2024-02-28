from tkinter import *
from tkinter import ttk
import requests

def data_get():

    city = city_name.get()

    data = requests.get("ADD API"+city+"&appid=ea60abfebe2223dbb").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("SHREE'S WEATHER APP")
win.config(background="coral")
win.geometry("530x530")

name_label = Label(win,text="SHREE'S WEATHER APP",
                   font=("Tme New Roman",25," bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="SHREE'S WEATHER APP",values = list_name,
                   font=("Tme New Roman",25," bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather Climate",
                   font=("Tme New Roman",12,))
w_label.place(x=25,y=260,height=50,width=140)

w_label1 = Label(win,text="",
                   font=("Tme New Roman",12,))
w_label1.place(x=250,y=260,height=50,width=140)


wb_label = Label(win,text="Weather Description",
                   font=("Tme New Roman",11,))
wb_label.place(x=25,y=330,height=50,width=140)

wb_label1 = Label(win,text="",
                   font=("Tme New Roman",11,))
wb_label1.place(x=250,y=330,height=50,width=140)



temp_label = Label(win,text="Temperature",
                   font=("Tme New Roman",12,))
temp_label.place(x=25,y=400,height=50,width=140)

temp_label1 = Label(win,text="",
                   font=("Tme New Roman",12,))
temp_label1.place(x=250,y=400,height=50,width=140)

per_label = Label(win,text="Pressure",
                   font=("Tme New Roman",11,))
per_label.place(x=25,y=470,height=50,width=140)

per_label1 = Label(win,text="",
                   font=("Tme New Roman",11,))
per_label1.place(x=250,y=470,height=50,width=140)

done_button = Button(win, text="DONE",
                         font=("Tme New Roman", 25, " bold"),command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
