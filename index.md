
<img src="https://user-images.githubusercontent.com/73137174/118411474-6ffe7580-b69d-11eb-9297-b39b77e71446.png" width="250" height="250">

## Installation & Usage
1.  If pip is not installed try `sudo apt install pip`. 
2.  Install Tkinter from terminal. `sudo apt install python3-tk`
3. tux_mixer package is available on PyPI. Type `pip install tux_mixer`.
4. To start program type `tux_mixer` to terminal. 

## Hardware
1. Upload StandartFirmata (Examples>Firmata) to your Arduino.
2. Connect potentiometers starting from A0. A0 controls master volume.\
(There is no limit for number of potentiometers)
3. Define number of potentiometers from taskbar `Change Pot Number` (Default is 4)
4. Set `Change Delay`. It prevents high CPU usage. Optimal number is between 0.05 and 0.15.\
(Default is 0.1)
