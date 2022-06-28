# #Install Module first
#
# # importing the qrcode library
# import qrcode
# # generating a QR code using the make() function
# qr_img = qrcode.make("fayaz_malik@ymail.com.")
# # saving the image file
# qr_img.save("qr-img.jpg")

#*******************************************************************************************************#

# 1. Importing the modules
import qrcode
from tkinter import *
from tkinter import messagebox

"""4. Creating the function to generate QR code and save it
Finally, we create the function to generate the code that runs on clicking the button. In this,

1. First we create the QRCode object with the version/size that user gave as input in the size() entry

2. Then we add the text that we need to encode by getting from the entry ‘text’

3. Then we get the QR code and save it in the directory that user gave as input

4. After this, we show the pop up message to confirm the user that the image is saved"""


# Function to generate the QR code and save it
def generateCode():
    # Creating a QRCode object of the size specified by the user
    qr = qrcode.QRCode(version=size.get(),
                       box_size=10,
                       border=5)
    qr.add_data(text.get())  # Adding the data to be encoded to the QRCode object
    qr.make(fit=True)  # Making the entire QR Code space utilized
    img = qr.make_image()  # Generating the QR Code
    fileDirec = loc.get() + '\\' + name.get()  # Getting the directory where the file has to be save
    img.save(f'{fileDirec}.png')  # Saving the QR Code
    # Showing the pop up message on saving the file
    messagebox.showinfo("https://github.com/fayazmalik503 QR Code Generator", "QR Code is saved successfully!")

# 2. Creating the main window
# Next, we create the main window with title, size and color.
#Creating the window
#Creating the window
wn = Tk()
wn.title('https://github.com/fayazmalik503 QR Code Generator')
wn.geometry('700x700')
wn.config(bg='SteelBlue3')

# 3. Taking the inputs
# Now, we take the inputs from the user to create the QR Code.
'''1. Text/URL as Entry() named as ‘text’

2. Location to save the QR Code as Entry() named as ‘loc’

3. Name of the QR Code image when saved in the device as Entry() named as ‘name’

4. Size of the QR Code to be generated as Entry() named ‘size’. In this the user has 
to give the size in the range 1-40. 1 being the smallest size of 21×21.
'''
# Then we create a button when clicked generates the QR Code and saves it by executing the generateCode() function.
#Label for the window
headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="https://github.com/fayazmalik503, QR Code Application", bg='azure', font=('Times',10,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#Taking the input of the text or URL to get QR code
Frame1 = Frame(wn,bg="SteelBlue3")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1 = Label(Frame1,text="Enter the text/URL: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)
text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#Getting input of the location to save QR Code
Frame2 = Frame(wn,bg="SteelBlue3")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
label2 = Label(Frame2,text="Enter the location to save the QR Code: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)
loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#Getting input of the QR Code image name
Frame3 = Frame(wn,bg="SteelBlue3")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)
label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)
name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)
#Getting the input of the size of the QR Code
Frame4 = Frame(wn,bg="SteelBlue3")
Frame4.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)
label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)
size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)
#Button to generate and save the QR Code
button = Button(wn, text='Generate Code',font=('Courier',15,'normal'), command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)
#Runs the window till it is closed manually

wn.mainloop()



