import board
import neopixel
import time
import math
import sys


pixels = neopixel.NeoPixel(board.D18, 900)
pixels.auto_write = False




def vibeLighting(pixels):
  i=0
  while True:
      i = i+1
      if i > 139:
          i = 0
      for x in range(899):
          mod = (math.sin(((x+i+0.5)*math.pi)/70)+1)/2
          mod = max(0.05, mod)
          if mod < 0:
              mod = 0
          pixels[x] = (int(mod*120), 0, max(2,int(mod* 10)))
      pixels.show()




if __name__ == "__main__":
    r = sys.argv[1]
    if r == "vibe":
      vibeLighting(pixels)
    