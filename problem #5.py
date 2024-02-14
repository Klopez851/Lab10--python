#######################################
# Author: Keidy Lopez
# Filename: problem #5.py
# Description: draws a traffic light on graphic window
#######################################
from graphics import *

def main():
    # width and height variables
    w,h=200,400

    # graphic window
    win = GraphWin('Traffic light', w,h)

    # main square of the traffic light
    square = Rectangle(Point(49,337),Point(151,35))
    square.draw(win)

    # list that hold Circle objects
    circles = []
    x=200    # variable for forloops
    y=400
    num = 5

    # forloop that creates circle objects and adds the to the Circle list
    for i in range(3):
        myCircle = Circle(Point(x/2,(y/7)*num),50)
        circles.append(myCircle)
        num -= 1.75

    # list that holds strings of color
    color = ['green', 'yellow', 'red']
    color_index = 0

    #forloop that draws Circle objects in circle list and colors them
    for circle in circles:
        circle.setFill(color[color_index])
        circle.draw(win)
        color_index += 1

    mp = win.getMouse()
    win.close()

if __name__ == "__main__":
    main()