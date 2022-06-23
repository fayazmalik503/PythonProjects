"""To bloack a website you need to changge the hostfile of that website
Do change it you need software authohorization  of your administration authorization
"""
import datetime
import time

'''open notepad -->open file -->open C drive --> open window file system 32 file --> open driver file --> etc --> now give all file to permission --> now open host file  '''
'''From above you will get the local host ID where you can copy local host ID with help of this you can block any website '''

"""WriteLocalHostID PasteWebsite""" #Delete http: this will now not open

'''Now how you can do with the python'''

import datetime as dt

end_time = dt.datetime(2022,6,25)
site_block = ["paste your website 1", "Paste your website 2"]
host_path = "File_host_path"
redirect = "125.0.0.1"

while True:
    if datetime.date.now()<end_time:
        print("website blocking")
        with open(host_path, "r+") as  host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " " + website+"\n")
                else:
                    pass

    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readline()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)

            host_file.truncate()
        time.sleep(5)

'''Now open you CMD with administer permission and run the file'''

'''Now  unbock you can comment the above  part'''  '''or'''   '''or open your file and notepad and  do the same'''
'''The above code is for particular time to block the website'''

