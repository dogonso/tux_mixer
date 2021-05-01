# tux_mixer
Control PulseAudio mixer with real potentiometers on Linux. 

## Hardware

- Using Arduino Nano/Uno as microcontroller board. 
- Potentiometers are connected to analog pins (default 4 potentiometers). 
- Powering potentiometers from 5V output on Arduino.

![circuit](https://user-images.githubusercontent.com/73137174/116781057-28ff6600-aa89-11eb-83bc-b4e419049c47.png)

## Software

- Python [pulsectl](https://github.com/mk-fg/python-pulse-control) and [pyFirmata](https://github.com/tino/pyFirmata) are used for this project. 
- Required packages can be installed by `pip install -r requirements.txt`

- Upload firmata protocol to Arduino. `Arduino IDE > File > Examples > Firmata > StandartFirmata`

## Modification

More potentiometers can be added to control more applications :

- Define new analog pins at start of code. Example: `analog_input4 = board.get_pin('a:4:i')` 
- Convert new input to variable under `while` loop. Example: `analog_value4 = analog_input4.read()`

- Control PulseAudio with new value. Example:
```
if analog_value4 is not None:

    with Pulse('volume-example') as pulse:

        if len(pulse.sink_input_list()) > 2: Number 2 on list controlling 3rd sound activity (x+1 equation). This line prevents IndexError. 

            sink_input = pulse.sink_input_list()[2] # Same as the number in the top row

            volume = sink_input.volume

            volume.value_flat = round(analog_value4, 2)

            pulse.volume_set(sink_input, volume)
```
> `board = pyfirmata.Arduino('/dev/ttyUSB0')` This address can change depending which port Arduino is connected.












