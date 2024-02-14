#######################################
# Author: Keidy Lopez
# Filename: problem #2.py
# Description: draws a house on a graphic window
#######################################
from graphics import *

def main():
    # height and with variable
    w= 400
    h= 400

    # graphic window
    win = GraphWin('House', w,h)

    # rectangle object and methods
    mySquare = Rectangle(Point(100,200), Point(300,400))
    mySquare.setFill('dark slate blue')
    mySquare.draw(win)

    # rectangle object and methods
    door = Rectangle(Point(175,300),Point(230,400))
    door.setFill('floral white')
    door.draw(win)

    # circle object and methods
    doorKnob = Circle(Point(220,355),5)
    doorKnob.setFill('navy')
    doorKnob.draw(win)

    # polygon object and methods
    roof = Polygon(Point(190,100), Point(50,200), Point(340,200))
    roof.setFill('black')
    roof.draw(win)

    mp = win.getMouse()

    print(mp)


if __name__ == "__main__":
    main()