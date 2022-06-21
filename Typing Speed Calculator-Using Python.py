from time import *
import random as r

# Finding Mistake
# Here we will check the result of test1 and testinput

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except :
            error = error + 1
    return error

#Speed and time
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':

    while True:
        ck = input("ready to test : yes / no :")
        if ck == "yes":
            test = ["A paragraphs is a self-contained unit of the discourse in writing",
            "Writing is an art", "Writing is sharing of idea"]

            test1 = r.choice(test)
            print("*********Typing speed calculator*******")
            print(test1)
            print()
            print()

            time_1 = time()
            testinput = input("Enter :")   # input give by default string
            time_2 = time()

            print('Speed :', speed_time(time_1, time_2, testinput), " w/se ")
            print("Error : ", mistake(test, testinput))

        elif ck == 'no':
            print('Thank-you')
            break

        else:
            print("wrong input")