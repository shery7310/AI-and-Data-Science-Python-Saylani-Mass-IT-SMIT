""" Write a program that takes a temperature in Celsius and checks
if it’s freezing, moderate, or hot. 
According to Appalachian State University Water freezes at 0°C
So tempratures below 0 are freezing
https://www.appstate.edu/~goodmanjm/rcoe/asuscienceed/six6energytransfer/temperature.html

Tempratures above 35 are hot
and tempratures between 20 and 35 can be considered moderate
whereas tempratures 5 and 20 can be considered chilly
"""

temprature = int(input("Enter Temprature in Celcius:\n"))
if temprature < 5:
    print("It's Freezing")
elif temprature > 5 and temprature <=20:
    print("It's Chilly")
elif temprature >= 20 and temprature <=35:
    print("It's moderate")
else:
    print("It's pretty hot")            