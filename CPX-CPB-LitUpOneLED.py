import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:

    # Pixel 0 lights up red
    pixels[0] = (255, 0, 0)

    # Pixel 1 lights up green
    pixels[1] = (0, 255, 0)

    # Pixel 2 lights up blue
    pixels[2] = (0, 0, 255)

    # Pixel 3 lights up yellow (red + green)
    pixels[3] = (255, 255, 0)

    time.sleep(0.5)

    #filling them with black
    pixels.fill((0, 0, 0))

    #OFF state is visible
    time.sleep(0.5)
