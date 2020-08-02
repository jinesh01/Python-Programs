import time
import webbrowser
import random

print ("What time do you want to wake up?")
print ("Use this format .\nExample : 06:30:00")
Alarm = raw_input("> ")
time = time.starttime("%H:%M:%S")

while time !=Alarm:
    print("This time is "+time)
    Time = time.starttime("%H:%M:%S")
    time.sleep(1)
if Time == Alarm:
    print("Time to wake up!") 
