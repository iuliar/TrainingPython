"""Write a Python program to print messages on the screen as long as a condition is met.
"""
import getch as getch

message =("m1", "m2", "m3")

import keyboard
import random

while True:  # making a loop
    print(random.choice(message))
    if keyboard.is_pressed('space'):  # if key 'q' is pressed
        break  # finishing the loop
