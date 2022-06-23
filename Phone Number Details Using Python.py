# Pip Install phone number or direct download

import  phonenumbers
from phonenumbers import timezone, geocoder, carrier

phone_no = input("Enter you Phone Number with +__ :")
phone = phonenumbers.parse(phone_no)
time = timezone.time_zones_for_number(phone)
carrier = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone_no)
print(phone)
print(time)
print(carrier)
print(reg)
