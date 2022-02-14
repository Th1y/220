from graphics import *
from time import *

win = GraphWin("HSVD", 1000, 800)
win.setBackground("grey")


def heart():
    c1 = Circle(Point(450, 400), 100)
    c1.draw(win)
    c1.setFill("red")
    c2 = Circle(Point(550, 400), 100)
    c2.draw(win)
    c2.setFill("red")
    t = Polygon(Point(350, 410), Point(500, 700), Point(650, 410))
    t.setFill("red")
    t.draw(win)


def vdtext():
    hsvdtext = Text(Point(500, 250), "Happy Saint Valentine's Day")
    hsvdtext.setSize(20)
    hsvdtext.setTextColor("Black")
    hsvdtext.draw(win)
    text2 = Text(Point(500, 275), "Don't Forget the Saint")
    text2.setSize(15)
    text2.setTextColor("White")
    text2.draw(win)
    closetext = Text(Point(500, 750), "CLICK TO CLOSE")
    closetext.setSize(20)
    closetext.setTextColor("Black")
    closetext.draw(win)


def arrow():
    cupid = Line(Point(900, 685), Point(1050, 750))
    cupid.setArrow("first")
    cupid.draw(win)
    return cupid


def movearrow(cupid):
    for i in range(20):
        cupid.move(-50, -25)
        sleep(0.15)


def main():
    vdtext()
    cupid = arrow()
    heart()
    movearrow(cupid)
    win.getMouse()
    win.close()


main()
