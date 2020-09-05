import board
import neopixel
import time
import math
import sys
import random

size = 900
pixels = neopixel.NeoPixel(board.D18, size)
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

def fill(pixels, brightness, color):
  pixels.brightness = brightness
  pixels.fill(color)
  pixels.show()

def bomb(pixels):
  fill(pixels, 1, (20, 105, 30))
  for x in range(size-2,-1,-1):
    pixels[x] = (255, random.randint(0,50), random.randint(0,25))
    pixels[x+1] = (0, 0, 0)
    pixels.show()
  for x in range(0, 5) :
    fill(pixels, 1, (20, 105, 30))
    pixels.show()
  



def fillFromOrigin(pixels, brightness, color, origin, sleep):
    left = origin
    right = origin
    
    while (left >= 0 or right < size):
      pixels[left] = color
      pixels[right] = color
      if left > 0:
        left = left - 1
      if right < size - 1:
        right = right + 1
      time.sleep(sleep)

      

if   __name__ == "__main__":
  r = sys.argv[1]
  r1 = 0
  if len(sys.argv) > 2:
    r1 = float(sys.argv[2])
  if   r == "vibe":
      vibeLighting(pixels)
  if   r == "dullWhite":
    fill(pixels, r1, (255, 255, 255))
  if r=="bomb":
    bomb(pixels)
  if r=="fill300":
    fillFromOrigin(pixels, r1, (255, 0, 0), 300, 1)