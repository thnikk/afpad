# Keypad libraries
import keypad
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard, find_device
from adafruit_hid.keycode import Keycode

# LED libraries
import neopixel
from rainbowio import colorwheel
pixels = neopixel.NeoPixel(board.D0, 8, brightness=1, auto_write=False)
logo = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=1, auto_write=False)

# Time (for LED timing)
import time

# Set pins for keys
pins = ( board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8 )
keys = keypad.Keys(pins, value_when_pressed=False, pull=True, interval=0.020)

# Map position  and keycodes
keymap = { 0:7, 1:6, 2:5, 3:2, 4:3, 5:4, 6:0, 7:1 }
keycodes = [ Keycode.Z, Keycode.X, Keycode.C, Keycode.A, Keycode.S, Keycode.D, Keycode.Q, Keycode.W ]

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Millis timer (float) for LEDs
ledMillis = 0
hue = 0

while True:

    # Update once every 20 milliseconds
    if (time.monotonic() - ledMillis) >= 0.020:
        ledMillis = time.monotonic() # Reset timer
        hue+=1 # Increment hue by 1
        pixels.fill(colorwheel(hue % 255)) # Get full RGB from hue value
        pixels.show() # Update LEDs
        logo[0] = (255,255,255) # Set logo color to white
        logo.show() # Update logo LED

    # Get new keypad events
    ev = keys.events.get()
    if ev is not None:
        # Get keycode for key
        key = keycodes[keymap[ev.key_number]]
        print(ev.key_number, ":", key)
        # Press or release on events
        if ev.pressed:
            kbd.press(key)
        else:
            kbd.release(key)
