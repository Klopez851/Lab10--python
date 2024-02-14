#######################################
# Author: Keidy Lopez
# Filename: problem #7.py
# Description: test program for draw_rectangle function
#######################################
from graphics import *

def main():
    w,h = 300,300
    win = GraphWin('Rectangle test program',w,h)

    # rectangle objects
    myRectangle1 = draw_rectangle(w/2,h/4,(w/4)*3,(h/4)*3, 'red',3)
    myRectangle1.draw(win)

    myRectangle1 = draw_rectangle(20,20,30,30, 'green', 1)
    myRectangle1.draw(win)

    myRectangle1 = draw_rectangle(270,40,290,80 ,'dark slate blue', 7)
    myRectangle1.draw(win)

    mp = win.getMouse()
    win.close()


# draws a rectangle with the specifed parameters and returns rectangle object
def draw_rectangle(top_left_x:int,top_left_y:int,bottom_right_x:int,bottom_right_y:int, color:str,border_thickness:int):
    myRectangle = Rectangle(Point(top_left_x, top_left_y),Point(bottom_right_x,bottom_right_y))
    myRectangle.setFill(color)
    myRectangle.setWidth(border_thickness)
    return myRectangle

if __name__ == "__main__":
    main()