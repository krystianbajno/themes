#!/usr/bin/python
import tkinter
from tkinter import messagebox
import os
import time
import subprocess

#### GUI FUNCTIONS

def EXIT():
    exit()
def POWER():
    os.system("sudo systemctl poweroff &")
    exit()
def REBOOT():
    os.system("sudo systemctl reboot &")
    exit()
def SUSPEND():
    os.system("sudo systemctl suspend &")
    exit()
def UPDATE_CMD():
    os.system("sudo urxvt -e /bin/bash -c 'pacman -Syuu' &")
def UPDATE_QUICK():
    os.system("sudo urxvt -e /bin/bash -c 'pacman -Syuu --noconfirm' &")
    exit()
def UPDATE_SHUT():
    os.system("sudo urxvt -e /bin/bash -c 'pacman -Syuu --noconfirm && sudo systemctl poweroff' &")
    exit()
def UPDATE_RESTART():
    os.system("sudo urxvt -e /bin/bash -c 'pacman -Syuu --noconfirm && sudo systemctl reboot' &")
    exit()
def RES():
    os.system("i3-msg exit &")
    exit()
def RES_wm():
    os.system("i3-msg restart")
def RES_net():
    os.system("sudo urxvt -e /bin/bash -c 'exec /home/krystian/scripts/connection_restart.sh' & ") 
def RANDR():
    os.system("arandr &")
    exit()
def AUD():
    os.system("pavucontrol &")
    exit()
def WALLPAPER():
    os.system("nitrogen &")
    exit()
def SRV():
    os.system("sudo systemadm &")
    exit()
def pamac():
    os.system("sudo pamac-aur &")
    exit()
def fwbuilder():
    os.system("sudo fwbuilder &")
    exit()
# #### GUI SETTINGS
top = tkinter.Tk()
top.title("Shutdown")
top.configure(background='#073642')
top.geometry("330x100")
POWER = tkinter.Button(top, text = "POWER OFF", bg='#dc322f', fg='white', activebackground="#cC221F", command = POWER)
REBOOT = tkinter.Button(top, text ="REBOOT", bg='#b58900', fg='white', activebackground='#a57900', command = REBOOT)
SUSPEND = tkinter.Button(top, text = "SUSPEND", bg='#859900', fg='black', activebackground='#167Bc2', command = SUSPEND)
EXIT = tkinter.Button(top, text = "EXIT", command = EXIT)
user = str(os.environ.get('USER')) + ", GUID:" +  str(os.getuid())

####
UPDATE = tkinter.Menubutton(top, text = "UPDATE")
UPDATE.menu = tkinter.Menu(UPDATE, tearoff=0)
UPDATE["menu"] = UPDATE.menu
UPDATE.menu.add_command ( label = "Run pamac-aur packet manager", command = pamac)
UPDATE.menu.add_command ( label="Exit and update carefully with commandline", command = UPDATE_CMD) 
UPDATE.menu.add_command ( label="Quick update (Assume yes for all prompts)", command = UPDATE_QUICK)
UPDATE.menu.add_command ( label="Quick update and shutdown afterwards", command = UPDATE_SHUT)
UPDATE.menu.add_command ( label="Quick update and reboot afterwards", command = UPDATE_RESTART)
####
RESTART = tkinter.Menubutton(top, border=0, bg='#002B36', fg='white', text = "RESTART")
RESTART.menu = tkinter.Menu(RESTART, tearoff=0)
RESTART["menu"] = RESTART.menu
RESTART.menu.add_command (label="Restart " + str(user) + " X11 session", command = RES)
RESTART.menu.add_command ( label="Restart i3 window manager", command = RES_wm)
RESTART.menu.add_command ( label="Restart systemd-networkd", command = RES_net)
###
SETTINGS = tkinter.Menubutton(top, border=0, bg='#002B36', fg='white', text = "SETTINGS")
SETTINGS.menu = tkinter.Menu(SETTINGS, tearoff=0)
SETTINGS["menu"] = SETTINGS.menu
SETTINGS.menu.add_command (label="Services", command = SRV)
SETTINGS.menu.add_command (label="Firewall", command = fwbuilder)
SETTINGS.menu.add_command (label="Display", command = RANDR)
SETTINGS.menu.add_command ( label="Audio", command = AUD)
SETTINGS.menu.add_command (label="Wallpaper", command = WALLPAPER)
###
#### GUI INIT
tkinter.Label(top, bg='#002B36', fg='white', text="User: " +str(user)).place(x = 10, y = 80)
tkinter.Label(top, bg='#002B36', fg='white', text="By Krystian Bajno").place(x = 215, y = 80)
UPDATE.place(x = 30, y = 50)
SETTINGS.place(x = 215, y = 62, width=75, height=15)
POWER.place(x = 30, y = 10)
EXIT.place(x = 140, y = 50)
RESTART.place(x = 215, y = 45,  width=75, height=15)
SUSPEND.place(x = 130, y = 10)
REBOOT.place(x = 215, y = 10)

top.mainloop()
