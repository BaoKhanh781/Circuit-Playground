import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
while True:
    pixels[0] = (255, 0, 0)
    # Pixel 1 green
    pixels[1] = (0, 255, 0)

    # Pixel 2 blue
    pixels[2] = (0, 0, 255)

    # Pixel 3 yellow (red + green)
    pixels[3] = (255, 255, 0)

    # Pixel 4 (red + blue)
    pixels[4] = (255, 0, 255)

    # Pixel 5 cyan (green + blue)
    pixels[5] = (0, 255, 255)

    # Pixel 6 white (red + green + blue)
    pixels[6] = (255, 255, 255)

    # Pixel 7 orange (more red, some green)
    pixels[7] = (255, 100, 0)

    # Pixel 8 pink
    pixels[8] = (255, 20, 147)

    # Pixel 9 light blue color
    pixels[9] = (0, 150, 255)

    time.sleep(0.5)
    pixels.fill((0, 0, 0))

    time.sleep(0.5)
