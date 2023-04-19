import time
import board
import digitalio
import neopixel
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
    RED,
)

pixel_pin = board.NEOPIXEL
led_back = digitalio.DigitalInOut(board.LED)
led_back.direction = digitalio.Direction.OUTPUT
button_1 = digitalio.DigitalInOut(board.BUTTON)
button_1.switch_to_input(pull=digitalio.Pull.DOWN)

# The number of NeoPixels
num_pixels = 9

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

pulse = Pulse(pixels, speed=.01, color=TEAL, period=0.75)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def heart_pulse(wait, pixint):
    pixels[0] = (pixint, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels[2] = (pixint, 0, 0)
    pixels[3] = (pixint, 0, 0)
    pixels[4] = (pixint, 0, 0)
    pixels[5] = (pixint, 0, 0)
    pixels[6] = (0, 0, 0)
    pixels[7] = (pixint, 0, 0)
    pixels[8] = (0, 0, 0)
    pixels.show()
    time.sleep(wait)

animations = AnimationSequence(pulse)


while True:
    led_back.value = button_1.value
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    #animations.animate()
