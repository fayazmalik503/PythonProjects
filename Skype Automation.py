from skpy import Skype

slogin = Skype("fayaz_maliK@ymail.com", "Password")

contact = slogin.contacts

# You can print contacts details by using this below code.
for i in contact:
    print(i)


# Now how you can send message to someone.

contact = slogin.contacts["ID_of_the_user"]
contact.chat.sendMsg("Hello Mr. Jack. How are you")


# Now let's create a group Chat
group = slogin.chats.create("ID_1","ID_2","ID_3")


# How to send your picture or  any thing from local machine
import os.path
slogin = Skype("ID_user", "Password")

contact = slogin.contacts["ID_of_person"]
with open("Paste_file_Path", "rb") as f:
    contact.chat.sendFile(f,"skp.png", image = True)



