# xyz@xyz.om -------> follow this cocndition

email = input("Enter you email : ") #e.g. fayaz_malik@ymail.com
k, j, d = 0, 0, 0
if len(email) >= 6: # 1
    if email[0].isalpha(): # 02
        if ("@" in email) and (email.count("@") == 1): # 3
            if (email[-4]==".") ^ (email[-3]=="."): #4    ^ XOR Operator
                for i in email:
                    if i==i.isspace():  # 5
                        k = 1
                    elif i.isalpha():
                        if i ==i.upper():  #5  w --> W or W --> W
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1

                if k == 1 or j ==1 or d == 1:
                        print("wrong email 5")

            else:
                print("wrorng email 4")

        else:
            print("Wrong Input 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")
