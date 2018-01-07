#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# SOURCE: https://github.com/boppreh/keyboard/blob/master/examples/10_second_macro.py


import keyboard
import time

keyboard.start_recording()
time.sleep(10)
events = keyboard.stop_recording()
keyboard.replay(events)
