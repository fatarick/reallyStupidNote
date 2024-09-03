import keyboard
import os


def save_file():
    name=input("Name for the file: ")
    with open(name + ".txt", "w") as f:
        f.write(text)

text=input()


keyboard.add_hotkey('ctrl+s', save_file)
keyboard.wait('esc')
