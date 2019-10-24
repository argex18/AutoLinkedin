import pyautogui as gui
from os import getcwd

def __test():
    print(getcwd() + "\\shares\\test.jpg")
    print(gui.position())
    gui.click(271, 529)
    gui.typewrite(getcwd() + "\\shares\\test.jpg")
    gui.typewrite(["enter"])

if __name__ == "__main__":
    __test()