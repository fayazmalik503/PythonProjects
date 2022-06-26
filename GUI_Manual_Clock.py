#Digital Clock containing time in hour minutes seconds am/or PM along with date

from tkinter import *
import datetime
#*************************************************************************#
# Object Creating
dateAndTime =  datetime.datetime.now()

# Using Class object calling different function seperately.
# For Time
lab_hour = dateAndTime.strftime("%H")
lab_min = dateAndTime.strftime("%M")
lab_sec = dateAndTime.strftime("%S")
lab_day_nig = dateAndTime.strftime("%p")

# For Date
lab_day = dateAndTime.strftime("%d")
lab_mon = dateAndTime.strftime("%m")
lab_year = dateAndTime.strftime("%Y")
lab_day_name = dateAndTime.strftime("%a")

#*************************************************************************#
'''
# We can also do the same with usin method.
    def date_time():
    time = datetime.datetime.now()
    
    lab_hour = dateAndTime.strftime("%H")
    lab_min = dateAndTime.strftime("%M")
    lab_sec = dateAndTime.strftime("%S")
    lab_day_nig = dateAndTime.strftime("%p")
    
    # For Date
    lab_day = dateAndTime.strftime("%d")
    lab_mon = dateAndTime.strftime("%m")
    lab_year = dateAndTime.strftime("%Y")
    lab_day_name = dateAndTime.strftime("%a")
# Changes in input text values at labels.
    lab_hour.config(text=lab_hour)
    lab_min.config(text=lab_min
    lab_sec.config(text=lab_sec)
    lab_day_nig.config(text=lab_day_nig)
# To change data every time
    lab_hour.after(200,dateAndTime)
    
'''

clock = Tk()
clock.title('*********Digital Clock*******')
clock.geometry("600x400")
clock.config(bg= 'black')

# Title
lab_title = Label(clock, text='Digital Clock', font=('Time New Roman', 20, "bold"), bg='black', fg='white')
lab_title.place(x='200',  y='10', width="220", height="30")

# Hour
lab_hour = Label(clock, text=lab_hour, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_hour.place(x='80',  y='80', width="80", height="50")

lab_min = Label(clock, text=lab_min, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_min.place(x='200',  y='80', width="80", height="50")

lab_sec = Label(clock, text= lab_sec, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_sec.place(x='320',  y='80', width="80", height="50")

lab_day_nig = Label(clock, text=lab_day_nig, font=('Time New Roman', 20, "bold"), bg='white', fg='red')
lab_day_nig.place(x='440',  y='80', width="80", height="50")

# Fixed Blocks
lab_hour1 = Label(clock, text='Hour', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_hour1.place(x='100',  y='160', width="40", height="20")

lab_min1 = Label(clock, text='Min', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_min1.place(x='220',  y='160', width="40", height="20")

lab_sec1 = Label(clock, text='Sec', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_sec1.place(x='340',  y='160', width="40", height="20")

lab_AMPM1 = Label(clock, text='AM/PM', font=('Time New Roman', 10, "bold"), bg='black', fg='red')
lab_AMPM1.place(x='450',  y='160', width="60", height="20")

# Date
lab_day = Label(clock, text=lab_day, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_day.place(x='80',  y='240', width="80", height="50")

lab_mon = Label(clock, text=lab_mon, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_mon.place(x='200',  y='240', width="80", height="50")

lab_year = Label(clock, text=lab_year, font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_year.place(x='320',  y='240', width="80", height="50")

lab_day_name = Label(clock, text=lab_day_name, font=('Time New Roman', 20, "bold"), bg='white', fg='red')
lab_day_name.place(x='440',  y='240', width="80", height="50")

# Fixed Blocks for date
lab_day1 = Label(clock, text='Date', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_day1.place(x='100',  y='320', width="40", height="20")

lab_mon1 = Label(clock, text='Month', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_mon1.place(x='220',  y='320', width="40", height="20")

lab_year1 = Label(clock, text='Year', font=('Time New Roman', 10, "bold"), bg='black', fg='white')
lab_year1.place(x='340',  y='320', width="40", height="20")

lab_day1 = Label(clock, text='Day', font=('Time New Roman', 10, "bold"), bg='black', fg='red')
lab_day1.place(x='450',  y='320', width="60", height="20")
clock.mainloop()