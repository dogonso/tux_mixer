import serial.tools.list_ports
from pulsectl import Pulse, PulseVolumeInfo
import pyfirmata
import time
import notify2
import os.path
import platform

ver_list = platform.python_version_tuple()

homedir = os.path.expanduser("~")
fulldir = homedir + '/.local/lib/python' + ver_list[0] + '.' + ver_list[1] + '/site-packages/tux_mixer/'

controlmsg = 0
waiter = 0
pairing = 0
connected = 0
msg = 0

pot_dir = fulldir + "pot.txt"
txt_num = open(pot_dir,"r")
config = txt_num.read()
input_num = int(config)
txt_num.close()

sleep_dir = fulldir + "sleep.txt"
timer = open(sleep_dir,"r")
delay_config = timer.read()
delay_num = float(delay_config)
timer.close()

input_list = []

def notification():
    notify2.init("Tux Mixer Notifier")
    noti = notify2.Notification('Tux Mixer', message= msg)
    noti.set_urgency(notify2.URGENCY_NORMAL)
    noti.set_timeout(notify2.EXPIRES_DEFAULT)
    noti.show()

def connection():
    board = pyfirmata.Arduino(ports[0].device)
    it = pyfirmata.util.Iterator(board)
    it.start()
    for num in range(input_num):
        pin = 'a:'+ str(num) + ':i'
        a_input = board.get_pin(pin)
        input_list.insert(num, a_input)
    
value_list = []

def volumectrl():
    value_list = []
    for num in range(input_num):
        a_value = input_list[num].read()
        value_list.insert(num, a_value)

    with Pulse('volume-increaser') as pulse:
        if value_list[0] is not None:
            for sink in pulse.sink_list():
                pulse.volume_set_all_chans(sink, round(value_list[0], 2))
                
    with Pulse('volume-example') as pulse:
        for tab in range(len(pulse.sink_input_list())):
            if tab+1 <= len(value_list):
                try:
                    sink_input = pulse.sink_input_list()[tab]
                    volume = sink_input.volume
                    volume.value_flat = round(value_list[tab+1], 2)
                    pulse.volume_set(sink_input, volume)
                except:
                    pass
    time.sleep(delay_num)

while True:    
    if connected == 0:
        ports = serial.tools.list_ports.comports()
        if len(ports) == 1:
            connected = 1
            msg = 'Board connected'
            notification()  
            continue
        if waiter == 0:
            msg = 'Waiting for connection'
            notification()
            waiter = 1
        time.sleep(1)

    if connected == 1:
        ports = serial.tools.list_ports.comports()
        if len(ports) == 0:
            connected = 0
            pairing = 0
            controlmsg = 0
            msg = 'Board disconnected'
            notification()
            continue
        if pairing == 0:
            time.sleep(1)
            try:
                connection()
            except:
                msg = 'Error: Can\'t access to board'
                notification()
                time.sleep(1)
                exit()
            pairing = 1
        if controlmsg == 0:
            msg = 'Volume control started'
            notification()
            controlmsg = 1
        volumectrl()
        time.sleep(delay_num)
