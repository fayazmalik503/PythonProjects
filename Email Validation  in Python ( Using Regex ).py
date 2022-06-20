# Email Validation in Python
# Using RegEx

# 1 Condition a-z all small cases     fayazmalik@gmail.com
# 2 0-9
# . _ time 1
# @time 1
# . 2, 3

import re
email_condition = "^[a-z]+[\._]?[a - z 0-9]+[@]\w+[.]\w{2,3}$"
# ? Tell in RegEx work into 0 or 1.

user_email = input("Enter your Email : ")

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")

