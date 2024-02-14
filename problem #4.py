#######################################
# Author: Keidy Lopez
# Filename: problem #4.py
# Description: draws 5 circles on a graphic window
#######################################
from graphics import *

def main():
    # graphs windoew
    win = GraphWin('Circles', 500,500)

    # fuction calls
    circle1 = draw_circle('black',350,350,6)
    circle1.draw(win)

    circle2 = draw_circle('dark slate blue', 450, 350, 18)
    circle2.draw(win)

    circle3 = draw_circle('red', 350, 150, 14)
    circle3.draw(win)

    circle4 = draw_circle('blue', 100, 4, 10)
    circle4.draw(win)

    circle5 = draw_circle('grey', 400, 400, 20)
    circle5.draw(win)

    mp = win.getMouse()


# draws a circle with the specifed parameters and returns circle object
def draw_circle (color:str, x:int,y:int,radius:int):
    myCircle = Circle(Point(x,y), radius)
    myCircle.setFill(color)
    return myCircle


if __name__ == "__main__":
    main()