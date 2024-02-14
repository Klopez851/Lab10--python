#######################################
# Author: Keidy Lopez
# Filename: problem #1.py
# Description: draws the flag of ireland in a graphic window
#######################################
from graphics import *

def main():
    # height and width variables
    w = 270
    h = 150

    # graphic window
    win = GraphWin('Flag of Ireland', w, h)

    # rectangle objects
    myRectangle1 = Rectangle(Point(0,0), Point(90,150))
    myRectangle2 = Rectangle(Point(90,0), Point(180,150))
    myRectangle3 = Rectangle(Point(180,0), Point(270,150))

    # rectangle object fill and outline
    myRectangle1.setFill('green')
    myRectangle2.setFill('white')
    myRectangle3.setFill('orange')

    myRectangle1.setOutline('green')
    myRectangle2.setOutline('white')
    myRectangle3.setOutline('orange')

    # drawing rectangles
    myRectangle1.draw(win)
    myRectangle2.draw(win)
    myRectangle3.draw(win)

    # modal method
    mp = win.getMouse()

if __name__=="__main__":
    main()