import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 60)

while True:
    pixels.fill((204, 102, 0)) # Orange
    time.sleep(3)
    pixels.fill((0, 0, 255)) # Biru
    time.sleep(3)
    pixels.fill((0, 255, 0)) # Hijau
    time.sleep(3)
    pixels.fill((255, 255, 0)) # Kuning
    time.sleep(3)
    pixels.fill((153, 0, 153)) # Ungu
    time.sleep(3)
    pixels.fill((255, 0, 255)) # Pink
    time.sleep(3)
    pixels.fill((255, 0, 0)) # Merah
    time.sleep(3)
    pixels.fill((76, 153, 0)) # Hijau_Kukus
    time.sleep(3)
    pixels.fill((255, 255, 255)) # Putih
    time.sleep(3)


    pixels.fill((0, 0, 0))
    time.sleep(10)
