import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyUSB0') # Defining serial port

ser = pyfirmata.util.Iterator(board) # Starting serial communication
ser.start()

analog_input0 = board.get_pin('a:0:i') # Defining potentiometer pins on Arduino
analog_input1 = board.get_pin('a:1:i')
analog_input2 = board.get_pin('a:2:i')
analog_input3 = board.get_pin('a:3:i')

while True:
    analog_value0 = analog_input0.read() # Converting to variables
    analog_value1 = analog_input1.read()
    analog_value2 = analog_input2.read()
    analog_value3 = analog_input3.read()

    if analog_value0 is not None:
        print("Pot 0= ",analog_value0) # Printing potentiometer values to shell
        print("Pot 1= ",analog_value1)
        print("Pot 2= ",analog_value2)
        print("Pot 3= ",analog_value3)

        time.sleep(0.5) # Delay in seconds

