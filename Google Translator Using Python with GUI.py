from tkinter import *

# This will create comboBox
from tkinter import ttk

# Now we will create Translator we will import Google Translator
from googletrans import Translator, LANGUAGES

#***************************************************************************
# Now let's create functions
def change(text = "type", src = "English", dest= "Urdu"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 =trans.translate(text, src=src1, dest=dest1)
    return tran1.text
#***************************************************************************
# Let's Create function for get data
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END) # get from starting to end

    # Now we change masg so we call use change function
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END,textget)

root = Tk()
root.title('Translator')
root.geometry("800x500")
root.config(bg='orange')

lab_txt = Label(root, text="Translator", font=("Time New Romam", 30, "bold"), bg='orange' , fg='blue')
lab_txt.place(x=250, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Romam", 15, "bold"), bg='orange' , fg='black')
lab_txt.place(x=200, y=100, height=40, width=400)

sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=150, height=100, width=780)

# Now you will create COMBO BOX
list_text = list(LANGUAGES.values()) # Here you will give languages

comb_sor =  ttk.Combobox(frame, values=list_text)
comb_sor.place(x=10, y=250, height=20, width=100)
comb_sor.set("english")

#Button
button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=110, y=250, height=20, width=100)

comb_dest =  ttk.Combobox(frame, values=list_text)
comb_dest.place(x=210, y=250, height=20, width=100)
comb_dest.set("english")

# Desitination Label
lab_txt = Label(root, text="Destination Text", font=("Time New Romam", 15, "bold"), bg='orange', fg='black')
lab_txt.place(x=200, y=300, height=40, width=400)
# Destination Text Box
dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=350, height=100, width=780)


root.mainloop()