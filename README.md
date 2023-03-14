# FigPi
Minifigure sized RP2040 based development board.

This has not been tested.  I have ordered prototype boards, so if you use this repo, please be prepared to have things not work.

## Board Definition for CircuitPython
[Fig Pi Board Definition - Local](https://github.com/bwshockley/circuitpython/tree/bwshockley-figpi/ports/raspberrypi/boards/bwshockley_figpi)

TODO: Once this board definition is pulled into the Adafruit repo, change link to the Adafruit repo.

## Changelog
**v1.1**
* Attached USB_BOOT to GPIO20, Pin 31
* Moved C12 to make room for new signal.

**v1.5**
* Changed all JST connectors to 4-pin.
* Moved SWDIO and SWCLK to test pads.
* Added APA102-2020 LEDs to make a 3 x 3 matrix.

**v1.6**
* Minor cosmetic changes to accomidate 'Status' label.

**v1.7**
* Fixed potential manufacturing limitation with ground vias.

**v2.1**
* Significant layout change to fix errors, move to mostly 0402 size passives, DFM, and more.

**v2.2**
* Updated the stemma connectors (i2c).  Pins were swapped - fixed the order.

**v2.3**
* Minor updates to routing, cleanup of vias, additional DRC checks.  Added silkscreen details.
