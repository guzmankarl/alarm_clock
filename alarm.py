#Sample Python Project
#found on github


#Import libraries
import time 
import webbrowser
import random
import os

#Check if the user has the YT.txt file in the same alarm.py directory
if os.path.isfile("YT.txt") == False:
	print ("Error: YT was not found. Creating file...")
	flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
	filecreate = os.open("YT.txt", flags)
	with os.fdopen(fisierCreat, 'w') as fileCreated:
		fileCreated.write("https://www.youtube.com/watch?v=2Yl1ipGl2Is")

#Set the time 
print ("What time do you need to be up?")
print ("Use this form \nExample: 06:30")
Alarm = raw_input("> ")


#Set the Time variable
Time = time.strftime("%H:%M")


#open the text file with youtube links
with open("YT.txt") as f:
#urls are stored in the content variable
	content = f.readlines()


#When the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:

	print ("The time is ") + Time

#Redeclare Time
	Time = time.strftime("%H:%M")

#wait for delay
	time.sleep(5)

#If the time value is equal to alarm string, run the following

if Time == Alarm:

	print ("Time to wake up!")

#a random link is chose from variable content, which will be stored in random_video variable
	random_video = random.choice(content)

#use webbrowser library to open youtube video link
	webbrowser.open(random_video)
