# Need GUI module tinker
from tkinter import *
import speedtest # Import the file "pip install speedtest-cli" otherwise speedtest module will be not usable.

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + "Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("    Checking Internet Speed")
sp.geometry("410x500")
sp.config(bg = "pink")

lab = Label(sp, text = "  Internet Speed Test", font = ("Time New Roman", 20, "bold"), bg = "pink" , fg = "blue")
lab.place(x = 65 , y = 40)

# Download Speed
lab = Label(sp, text = "Downloading Speed", font = ("Time New Roman", 20, "bold"), fg = "black")
lab.place(x = 65 , y = 100, height= 50, width=290)
lab_down = Label(sp, text = "00", font = ("Time New Roman", 20, "bold"), fg = "black")
lab_down.place(x = 65 , y = 160, height= 50, width=290)
# Uploading Speed
lab = Label(sp, text = "Uploading Speed", font = ("Time New Roman", 20, "bold"), fg = "black")
lab.place(x= 65, y =220, height=50, width=290)
lab_up = Label(sp, text="00", font = ("Time New Roman", 20, "bold"), fg = "black")
lab_up.place(x=65, y=280, height= 50, width=290)

button = Button(sp, text="Check Speed", font=("Time New Roman", 15, "bold"), relief=RAISED, bg="red", command=speedcheck)
button.place(x = 85 , y = 340, height= 40, width=250)

sp.mainloop()
