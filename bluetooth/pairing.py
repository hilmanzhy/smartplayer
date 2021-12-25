import RPi.GPIO as GPIO
import subprocess
import time

button = 4
flag = 0
count = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def code():
    subprocess.Popen(["sudo", "python", "/home/pi/player/testAutoPair.py"])
    time.sleep(10)
    subprocess.Popen(["sudo", "python", "/home/pi/player/BtAutoPair.py"])
    time.sleep(3)

def buttonpressed():
    global count
    global flag
#    code()
    if GPIO.input(button) == False and flag == 0:
       code()
       print("Pressed Button...")
       flag = 1
    if GPIO.input(button) == True and flag == 1:
       print("Unpressed Button...")
       flag = 0

while True:
   buttonpressed()
