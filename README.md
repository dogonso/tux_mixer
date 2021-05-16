# tux_mixer
Control PulseAudio mixer with real potentiometers on Linux.

## Installation & Usage
1.  If pip is not installed try `sudo apt install pip3`. 
2. tux_mixer package is available on PyPI. Type `pip3 install tux_mixer` or 
`pip install tux_mixer`.
3. To start program type `tux_mixer` to terminal. 

## Hardware
1. Upload StandartFirmata (Examples>Firmata) to your Arduino.
2. Connect potentiometers starting from A0. A0 controls master volume.\
(There is no limit for number of potentiometers)
3. Define number of potentiometers from taskbar `Change Pot Number` (Default is 4)
4. Set `Change Delay`. It prevents high CPU usage. Optimal number is between 0.05 and 0.15.\
(Default is 0.1)
