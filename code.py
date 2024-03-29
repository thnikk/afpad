# Keypad libraries
import keypad
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard, find_device
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Time (for LED timing)
import time

# LED libraries
import neopixel
from rainbowio import colorwheel
# Initialize neopixels
pixels = neopixel.NeoPixel(board.D0, 8, brightness=1, auto_write=False)
# Initialize built-in neopixel
logo = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=1, auto_write=False)

# Set pins for keys
pins = ( board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8 )
keys = keypad.Keys(pins, value_when_pressed=False, pull=True, interval=0.020)

# Map position  and keycodes
keymap = [ 1, 0, 2, 3, 4, 7, 6, 5 ]
keycodes = [ [Keycode.LEFT_CONTROL, Keycode.C], [Keycode.LEFT_CONTROL, Keycode.V], [Keycode.LEFT_ARROW], [Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT], [Keycode.RIGHT_ARROW], [Keycode.FIVE], [Keycode.LEFT_GUI, Keycode.LEFT_SHIFT, Keycode.S], [Keycode.SEVEN] ]
"""
Physical keymap
[ 0, 1, X ]
[ 2, 3, 4 ]
[ 5, 6, 7 ]
(X is where the xiao and LED are)
"""

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Millis timer (float) for LEDs
ledMillis = 0
hue = 0

count = 0
countMillis = 0

idleMillis = time.monotonic()

while True:

    # Update once every 20 milliseconds
    if (time.monotonic() - ledMillis) >= 0.020:
        ledMillis = time.monotonic() # Reset timer
        hue+=1 # Increment hue by 1
        pixels.fill(colorwheel(hue % 255)) # Get full RGB from hue value
        logo[0] = (colorwheel(hue % 255)) # Set logo color to white
        pixels.show() # Update LEDs
        logo.show() # Update logo LED
    
    # Uncomment for LED timeout
    # if (time.monotonic() - idleMillis) >= 30:
        # pixels.brightness = 0
        # logo.brightness = 0
    # else:
        # pixels.brightness = 1
        # logo.brightness = 1

    # Uncomment to see loop speed over serial
    # count+=1
    # if (time.monotonic() - countMillis) > 1:
        # countMillis = time.monotonic()
        # print(count)
        # count = 0

    # Get new keypad events
    ev = keys.events.get()
    # If there's a new event
    if ev is not None:
        # Reset idle timer
        idleMillis = time.monotonic()
        # And the pressed key matches the number
        if keymap.index(ev.key_number) is 8:
            # Do a thing on release
            if not ev.pressed:
                layout.write('This types a string')
        
        elif keymap.index(ev.key_number) is 9:
            # Do a thing on release
            if not ev.pressed:
                layout.write('This also types a string')

        else:
            # Press or release
            if ev.pressed:
                # Iterate through keys and press/release all sub-keys for a given key
                for key in keycodes[keymap.index(ev.key_number)]:
                    print("Pressing", keymap[ev.key_number])
                    kbd.press(key)
            else:
                for key in keycodes[keymap.index(ev.key_number)]:
                    print("Releasing", keymap[ev.key_number])
                    kbd.release(key)
