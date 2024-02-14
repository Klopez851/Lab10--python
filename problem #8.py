#######################################
# Author: Keidy Lopez
# Filename: problem #8.py
# Description: scaled rectangle on a graphic window
#######################################
from graphics import *
import random

def main():
    # width and height variable and graphic window
    w,h= 300,300
    win = GraphWin('SCALED RECTANGLE', w, h)

    # random color choices
    color_list = ['green','blue','dark slate blue', 'yellow','red','purple','brown', 'pink','white','black','khaki','light blue']

    # ractangle object and methods
    myRectangle1 = Rectangle(Point((w/2)-25,(h/2)-25),Point((w/2)+25,(h/2)+25))
    myRectangle1.setFill(random.choice(color_list))
    myRectangle1.draw(win)

    mp = win.getMouse()
    win.close()

if __name__ == "__main__":
    main()