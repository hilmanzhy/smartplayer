import socket
import time
import board
import neopixel
import RPi.GPIO as GPIO
import subprocess

#GPIO.setmode(GPIO.BOARD)

doorlock = 20
lamp = 21

GPIO.setup(doorlock, GPIO.OUT)
GPIO.setup(lamp, GPIO.OUT)

pixels = neopixel.NeoPixel(board.D18, 60)
pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB

s = socket.socket()
print ("Socket successfully created")
port = 12345
s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(5)
c, addr = s.accept()
print ("socket is listening")
slider = 0
flag = 0
R = 0
G = 0
B = 0

def ble_on():
    subprocess.Popen(["sudo", "python", "/home/pi/player/bluetooth/testAutoPair.py"])
    time.sleep(5)
    subprocess.Popen(["sudo", "python", "/home/pi/player/bluetooth/BtAutoPair.py"])
    time.sleep(3)

while True:
   print ('Got connection from', addr )
   data = c.recv(5)
   a = data
   print(data)
   slider = str(a).split('-')
   if data == b'A-1':
      GPIO.output(20, GPIO.HIGH)
      print("door lock On.....")
   elif data == b'A-0':
      GPIO.output(20, GPIO.LOW)
      print("door lock Off....")
   elif data == b'B-1':
      ble_on()
      print("Bluetooth On....")
   elif data == b'B-0':
      print("Bluetooth Off....")
   elif data == b'C-1':
      GPIO.output(21, GPIO.HIGH)
      print("Lamp AC On....")
   elif data == b'C-0':
      GPIO.output(21, GPIO.LOW)
      print("Lamp AC Off....")
   elif data == b'D-1':
      pixels.fill((255, 255, 255))
      pixels.show()
      flag = 1
      print("Ledstrip On....")
   elif data == b'D-0':
      flag = 0
      pixels.fill((0, 0, 0))
      pixels.show()
      print("Ledstrip Off....")
   elif flag == 1 and data == b'F-0':
      R = 204
      G = 102
      B = 0
      pixels.fill((R, G, B)) # Orange
      pixels.show()
      print("Orange....")
   elif flag == 1 and data == b'G-0':
      R = 0
      G = 0
      B = 255
      pixels.fill((R, G, B)) # Biru
      pixels.show()
      print("Blue....")
   elif flag == 1 and data == b'H-0':
      R = 0
      G = 255
      B = 0
      pixels.fill((R, G, B)) # Hijau
      pixels.show()
      print("Green....")
   elif flag == 1 and data == b'I-0':
      R = 255
      G = 255
      B = 0
      pixels.fill((R, G, B)) # Kuning
      pixels.show()
      print("Yellow....")
   elif flag == 1 and data == b'J-0':
      R = 153
      G = 0
      B = 153
      pixels.fill((R, G, B)) # Ungu
      pixels.show()
      print("Purple....")
   elif flag == 1 and data == b'K-0':
      R = 255
      G = 0
      B = 255
      pixels.fill((R, G, B)) # Pink
      pixels.show()
      print("Pink....")
   elif flag == 1 and data == b'L-0':
      R = 255
      G = 0
      B = 0
      pixels.fill((R, G, B)) # Merah
      pixels.show()
      print("Red....")
   elif flag == 1 and data == b'M-0':
      R = 76
      G = 153
      B = 0
      pixels.fill((R, G, B)) # Hijau_Kukus
      pixels.show()
      print("Dark Green....")
   elif flag == 1 and data == b'N-0':
      R = 255
      G = 255
      B = 255
      pixels.fill((R, G, B)) # Putih
      pixels.show()
      print("White....")
   elif slider[0] == "b'E":
      value = slider[1]
#      print("Slider  > ",value[:-1])
      pwm = float(value[:-1]) / 100.0
      pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=pwm, auto_write=False, pixel_order=ORDER)
      print(R, G, B, pwm)
      pixels.fill((R, G, B))
      pixels.show()

