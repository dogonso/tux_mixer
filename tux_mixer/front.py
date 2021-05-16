from pystray import MenuItem as item
import pystray
from PIL import Image
import time
import subprocess
from tkinter import simpledialog, messagebox
import tkinter
import os, sys
import os.path
import platform

def program():
    ver_list = platform.python_version_tuple()

    homedir = os.path.expanduser("~")
    fulldir = homedir + '/.local/lib/python' + ver_list[0] + '.' + ver_list[1] + '/site-packages/tux_mixer/'

    parent = tkinter.Tk() 
    parent.overrideredirect(1)
    parent.withdraw()

    control_dir = fulldir + "control.py"
    main = subprocess.Popen(["python3", control_dir])

    def sleep_time():
        timer = simpledialog.askfloat('Setup', 'Enter delay for volume control', minvalue=0.05, maxvalue=1.0, parent=parent)
        sleep_dir = fulldir + 'sleep.txt'
        timer_num = open(sleep_dir,"w")
        timer_num.write(str(timer))
        timer_num.close()
        main.terminate()
        messagebox.showwarning("Setup","Restart program with new settings")
        exit()
        
    def action():
        main.terminate()
        time.sleep(2)
        exit()

    def change_pot():
        pot_value = simpledialog.askinteger('Setup', 'Enter number of pots', minvalue=2, maxvalue=16, parent=parent)
        pot_dir = fulldir + "pot.txt"
        var_num = open(pot_dir,"w")
        var_num.write(str(pot_value))
        var_num.close()
        main.terminate()
        messagebox.showwarning("Setup","Restart program with new settings")
        exit()

    image_dir = fulldir + "tux_mixer_logo_mini.png"
    image = Image.open(image_dir)
    menu = (item('Change Pot Number', change_pot),  item('Change delay', sleep_time), item('Exit', action))
    icon = pystray.Icon("tuxmixer", image, "Tux Mixer", menu)

    icon.run()



