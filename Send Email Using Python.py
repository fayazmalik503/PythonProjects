import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('fayaz_malik@ymail.com','Password')
subject = "test python"
body = "I love python"
massage = "subject:{}\n\n{}".format(subject,body)"
listadd = ['frist_email.com',
           'second_email.com',
           'third_email.com']
ob.sendmail('fayaz_malik@ymail.com', listadd, massage)
print("Message sent")
ob.quit()
# Now you can check this online.
