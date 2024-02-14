#######################################
# Author: Keidy Lopez
# Filename: problem #3.py
# Description: scaled tictactoe grid
#######################################
from graphics import *

def main():
    # width and height variable
    w = int(input('please enter width of graphic window: '))
    h = int(input('please enter height of graphic window: '))

    # graphic window
    win = GraphWin('tic-tac-toe grid', w, h)

    # line objects
    line1 = Line(Point(w/3,0), Point(w/3,h))
    line2 = Line(Point((w/3)*2,0), Point((w/3)*2,h))
    line3 = Line(Point(0,h/3), Point(w,h/3))
    line4 = Line(Point(0,(h/3)*2), Point(w,(h/3)*2))

    # line methods
    line1.setFill('dark slate blue')
    line2.setFill('dark slate blue')
    line3.setFill('dark slate blue')
    line4.setFill('dark slate blue')

    line1.setWidth((w*.03))
    line2.setWidth((w*.03))
    line3.setWidth((w*.03))
    line4.setWidth((w*.03))

    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)

    # modal method
    mp = win.getMouse()

if __name__ == "__main__":
    main()