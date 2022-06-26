# Digital Clock containing time in hour minutes seconds am/or PM along with date

from tkinter import *
import datetime
# *************************************************************************#
# Using method
# *************************************************************************#

# We can also do the same with using method.
def date_time():
    time = datetime.datetime.now()
# Let's define variables
    lab_h = time.strftime("%H")
    lab_m = time.strftime("%M")
    lab_s = time.strftime("%S")
    lab_d_n = time.strftime("%p")


# Changes in input text values at labels.

    lab_hr.config(text=lab_h)
    lab_min.config(text=lab_m)
    lab_sec.config(text=lab_s)
    lab_am.config(text=lab_d_n)

# To change data every time
    lab_sec.after(200, date_time)

def time_date():
    date = datetime.datetime.now()
    # For Date
    lab_d = date.strftime("%d")
    lab_m = date.strftime("%m")
    lab_y = date.strftime("%Y")
    lab_d_n = date.strftime("%a")
# Changes that will come from input in text= "00"
    lab_day.config(text=lab_d)
    lab_mon.config(text=lab_m)
    lab_year.config(text=lab_y)
    lab_day_name.config(text=lab_d_n)

#****************Interface*************************#
clock = Tk()
clock.title('*********Digital Clock*******')
clock.geometry("600x400")
clock.config(bg='orange')



#Title
lab_title = Label(clock, text='Digital Clock', font=('Time New Roman', 20, "bold"), bg='black', fg='orange')
lab_title.place(x='200', y='10', width="220", height="30")

# Hour
lab_hr = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_hr.place(x='80', y='80', width="80", height="50")
# min
lab_min = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_min.place(x='200', y='80', width="80", height="50")
# second
lab_sec = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_sec.place(x='320', y='80', width="80", height="50")
# am pm
lab_am = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='red')
lab_am.place(x='440', y='80', width="80", height="50")

# Fixed Blocks
lab_hour1 = Label(clock, text='Hour', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_hour1.place(x='100', y='160', width="40", height="20")

lab_min1 = Label(clock, text='Min', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_min1.place(x='220', y='160', width="40", height="20")

lab_sec1 = Label(clock, text='Sec', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_sec1.place(x='340', y='160', width="40", height="20")

lab_AMPM1 = Label(clock, text='AM/PM', font=('Time New Roman', 10, "bold"), bg='black', fg='red')
lab_AMPM1.place(x='450', y='160', width="60", height="20")

# Date
lab_day = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_day.place(x='80', y='240', width="80", height="50")

lab_mon = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_mon.place(x='200', y='240', width="80", height="50")

lab_year = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='black')
lab_year.place(x='320', y='240', width="80", height="50")

lab_day_name = Label(clock, text="00", font=('Time New Roman', 20, "bold"), bg='white', fg='red')
lab_day_name.place(x='440', y='240', width="80", height="50")

# Fixed Blocks for date
lab_day1 = Label(clock, text='Date', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_day1.place(x='100', y='320', width="40", height="20")

lab_mon1 = Label(clock, text='Month', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_mon1.place(x='220', y='320', width="40", height="20")

lab_year1 = Label(clock, text='Year', font=('Time New Roman', 10, "bold"), bg='black', fg='orange')
lab_year1.place(x='340', y='320', width="40", height="20")

lab_day1 = Label(clock, text='Day', font=('Time New Roman', 10, "bold"), bg='black', fg='red')
lab_day1.place(x='450', y='320', width="60", height="20")

date_time()
time_date()

clock.mainloop()