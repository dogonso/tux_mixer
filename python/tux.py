from pulsectl import Pulse, PulseVolumeInfo # Importing libraries
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyUSB0') # Defining serial port to software (May be different depending on port)

ser = pyfirmata.util.Iterator(board) # Starting serial communication with Arduino
ser.start()

analog_input0 = board.get_pin('a:0:i') # Defining analog pins (Potentiometers)
analog_input1 = board.get_pin('a:1:i')
analog_input2 = board.get_pin('a:2:i')
analog_input3 = board.get_pin('a:3:i')

while True:
    analog_value0 = analog_input0.read() # Converting analog inputs to variables
    analog_value1 = analog_input1.read()
    analog_value2 = analog_input2.read()
    analog_value3 = analog_input3.read()

    if analog_value2 is not None: # Preventing crash caused by non-integer variables at start

        with Pulse('volume-example') as pulse:

            if len(pulse.sink_input_list()) > 0: # Preventing IndexError when there is no sound activity 

                sink_input = pulse.sink_input_list()[0] # Controlling first sound activity on list

                volume = sink_input.volume

                volume.value_flat = round(analog_value2, 2) # Rounding analog input to have more stable values

                pulse.volume_set(sink_input, volume) 

    if analog_value1 is not None:

        with Pulse('volume-example') as pulse:

            if len(pulse.sink_input_list()) > 1:

                sink_input = pulse.sink_input_list()[1] # Controlling second sound activity on list

                volume = sink_input.volume

                volume.value_flat = round(analog_value1, 2)

                pulse.volume_set(sink_input, volume) # Applying changes on volume

    if analog_value3 is not None:

        with Pulse('volume-increaser') as pulse:
            for sink in pulse.sink_list():

                pulse.volume_set_all_chans(sink, round(analog_value3, 2)) # Controlling master sound

    time.sleep(0.05) # Delay to prevent high CPU usage    

            
            

