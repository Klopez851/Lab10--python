#######################################
# Author: Keidy Lopez
# Filename: problem #6.py
# Description: draws a target on a graphic window
#######################################
from graphics import *

def main():
 # width and height variables
    w = 500
    h = 500

# graphic window
    win = GraphWin('Target Practice',w,h)

# list that holds circle objects
    circles = []
    radius = 200

# forloop that creates circle objects and adds the to the circle list
    for i in range(7):
        myCircle = Circle(Point(w/2,h/2),radius)
        circles.append(myCircle)
        if i != 5:
            radius -= 30
        else:
            radius -= 35


# changes attributes of certain circles in circle list
    circles[5].setFill('white')
    circles[5].setOutline('white')
    circles[4].setFill('red')
    circles[4].setOutline('white')
    circles[4].setWidth(2)
    circles[3].setFill('black')

# for loop that draws circles
    for cir in circles:
        cir.draw(win)

# draws line of target
    myLine = Line(Point(w/2,5),Point(w/2,h-5))
    myLine1 = Line(Point(5, h/2), Point(w-5, h/2))
    myLine.draw(win)
    myLine1.draw(win)


    mp = win.getMouse()
    win.close()

if __name__ == "__main__":
    main()