import socket
import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812W_STRIP

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

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

while True:
#   parser = argparse.ArgumentParser()
#   parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
#   args = parser.parse_args()
   print ('Got connection from', addr )
   data = c.recv(5)
#   time.sleep(1)
   a = data
   print(data)
   slider = str(a).split('-')
   if data == b'A-1':
      print("door lock On.....")
   if data == b'A-0':
      print("door lock Off....")
   if data == b'B-1':
      print("Bluetooth On....")
   if data == b'B-0':
      print("Bluetooth Off....")
   if data == b'C-1':
      print("Lamp AC On....")
   if data == b'C-0':
      print("Lamp AC Off....")
   if data == b'D-1':
#      pixels.fill((255, 255, 255))
      flag = 1
      print("Ledstrip On....")
   if data == b'D-0':
      flag = 0
#      pixels.fill((0, 0, 0))
      print("Ledstrip Off....")
   if flag == 1 and data == b'F-0':
#      pixels.fill((204, 102, 0)) # Orange
      print("Orange....")
   if flag == 1 and data == b'G-0':
#      pixels.fill((0, 0, 255)) # Biru
      print("Blue....")
   if flag == 1 and data == b'H-0':
#      pixels.fill((0, 255, 0)) # Hijau
      print("Green....")
   if flag == 1 and data == b'I-0':
#      pixels.fill((255, 255, 0)) # Kuning
      print("Yellow....")
   if flag == 1 and data == b'J-0':
#      pixels.fill((153, 0, 153)) # Ungu
      print("Purple....")
   if flag == 1 and data == b'K-0':
#      pixels.fill((255, 0, 255)) # Pink
      print("Pink....")
   if flag == 1 and data == b'L-0':
#      pixels.fill((255, 0, 0)) # Merah
      print("Red....")
   if flag == 1 and data == b'M-0':
#      pixels.fill((76, 153, 0)) # Hijau_Kukus
      print("Dark Green....")
   if flag == 1 and data == b'N-0':
#      pixels.fill((255, 255, 255)) # Putih
      print("White....")
   if slider[0] == "b'E":
      value = slider[1]
      print("Slider  > ",value[:-1])
      pwm = value[:-1]
      int(pwm)
      print(pwm)
      time.sleep(0.5)
      strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, pwm, LED_CHANNEL, LED_STRIP)
      strip.begin()
      colorWipe(strip, Color(255, 0, 0), 0)
