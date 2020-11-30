#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:15:14 2020

@author: a.kotatis
"""

import pyautogui, time
time.sleep(5)
f=open("beemovie.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")