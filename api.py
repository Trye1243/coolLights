from flask import Flask, json, request
from threading import Thread
import board
import neopixel
import time
import math
import sys
import random

kill = False
size = 900
pixels = neopixel.NeoPixel(board.D18, size)
pixels.auto_write = False


def vibeLighting(pixels):
    global kill
    i = 0
    while True:
        i = i + 1
        if i > 139:
            i = 0
        for x in range(899):
            mod = (math.sin(((x + i + 0.5) * math.pi) / 70) + 1) / 2
            mod = max(0.05, mod)
            if mod < 0:
                mod = 0
            pixels[x] = (int(mod * 120), 0, max(2, int(mod * 10)))
        pixels.show()
        if kill:
            break


def fill(pixels, brightness, color):
    global kill
    pixels.brightness = brightness
    pixels.fill(color)
    pixels.show()


def bomb(pixels):
    global kill
    fill(pixels, 1, (14, 2, 0))
    for x in range(size - 2, -1, -1):
        pixels[x] = (255, random.randint(0, 50), random.randint(0, 5))
        pixels[x + 1] = (0, 0, 0)
        pixels.show()
        if kill:
            break
    for x in range(0, 25):
        fill(pixels, 1, (255, random.randint(0, 80), 0))
        pixels.show()
        if kill:
            break


def fillFromOrigin(pixels, brightness, color, origin, sleep):
    global kill
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
        print(left, right)
        pixels.show()
        if kill:
            break




companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)



def lights(name):
    if (name=="off"):
        fill(pixels, (0, 0, 0), 0)
    elif (name=="vibe"):
        vibeLighting(pixels)
    elif (name=="bomb"):
        bomb(pixels)



t = Thread(target=lights, args=("none",))

@api.route('/lights', methods=['POST'])
def post_lights():
    global kill
    global t
    if t.is_alive():
        kill = True
        t.join()
        kill = False
    print(request.args.get("program"))
    t = Thread(target=lights, args=(request.args.get("program"),))
    t.start()
    return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run("130.215.126.81")