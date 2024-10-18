import datetime
from playsound import playsound
alarmhour = int(input("Enter Hour: "))
alarmmin = int(input("Enter Minute: "))
alarm = input("AM/PM: ")
if alarm == "PM":
    alarmhour += 12
while True:
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
       print("Playing Alarm Sound...")  
       playsound("alarm.mp3")
       break

