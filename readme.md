# Afpad Circuitpython
This is a basic firmware written for the Afpad using Circuitpython. I don't have the hardware and can't test the firmware, but it should work.

## Installation
Download the bootloader from [Adafruit](https://circuitpython.org/board/seeeduino_xiao_rp2040/) and copy it to the xiao by holding down the bootsel button (the one with the B next to it) while plugging it in. Copy the UF2 bootloader to the "RP_RP2" removable drive and it will flash the new bootloader and remount itself as a CircuitPython device.

Copy everything from this repository to the newly mounted CIRCUITPY device and it should update in real time.

## Features
It's got some rainbow leds keys.

## Resources
Adafruit documents all of their libraries in the [CircuitPython documentation](https://docs.circuitpython.org/en/latest/docs/index.html). Look up specific libraries for more detail.

- [Keypad library](https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html)
- [Keyboard library](https://docs.circuitpython.org/projects/hid/en/latest/api.html)
- [Keycodes](https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html)
- [Neopixel library](https://docs.circuitpython.org/projects/neopixel/en/latest/api.html?highlight=neopixel#neopixel-neopixel-strip-driver)

For more basic resources, check out a site like [w3schools](https://www.w3schools.com/python/default.asp) for their python tutorials. There are some differences between Python and CircuitPython, but most of the basic tutorials will carry over.
