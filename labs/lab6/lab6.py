from graphics import *


def vignerecode(textinput, codeinput):
    textinput = textinput.upper()
    textinput = textinput.replace(" ", "")
    codeinput = codeinput.upper()
    encodedoutput = ""
    inputlength = len(textinput)
    for i in range(inputlength):
        messagevalue = ord(textinput[i]) - 65
        codevalue = ord(codeinput[i % len(codeinput)]) - 65
        encodedcharacter = ((messagevalue + codevalue) % 26) + 65
        encodedcharacter = chr(encodedcharacter)
        encodedoutput = encodedoutput + encodedcharacter
    print(encodedoutput)
    return encodedoutput


def main():
    width = 500
    height = 600
    win = GraphWin("Vigenere", width, height)
    text1point = Point(width - 400, height - 500)
    text1 = Text(text1point, "Text to Encode:")
    text1.draw(win)
    text2point = Point(width - 363, height - 400)
    text2 = Text(text2point, "Key:")
    text2.draw(win)
    text3point = Point(width / 2, height * 3 / 4)
    text3 = Text(text3point, "Click Anywhere to Encode")
    text3.draw(win)
    inputbox1 = Entry(Point((width - 250), (height - 500)), 20)
    inputbox1.draw(win)
    inputbox2 = Entry(Point((width - 250), (height - 400)), 20)
    inputbox2.draw(win)
    win.getMouse()
    textinput = inputbox1.getText()
    codeinput = inputbox2.getText()
    encodedoutput = vignerecode(textinput, codeinput)
    text3.undraw()
    text4point = Point(width / 2, height * 3 / 4)
    text4 = Text(text4point, encodedoutput)
    text4.draw(win)
    text5point = Point(width / 2, height * 4 / 5)
    text5 = Text(text5point, "Click Anywhere to Close")
    text5.draw(win)
    win.getMouse()
    win.close()


main()
