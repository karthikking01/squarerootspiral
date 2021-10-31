import turtle, math
import itertools
from random import randint, randrange
def func():
    global ty
    t.color("black")
    t.write('Now click on this screen and quit', font=style, align='center')
    ty = 1
turtle.onkeypress(func, key='space')
screen = turtle.Screen()
screen.listen()
home = (0, 0)
input("PLEASE CONSIDER THIS WINDOW TOO! \n Not a virus no need to worry!\n Hit enter")
inp = input("The spiral should end at: √")
print("You may hit \"SPACE\" on the turtle window then click on graphics window to close the program")
print("Now you may \"Minimize\" this window")
t = turtle.Turtle()
t.ht()
turtle.colormode(255)
t.speed(100)
listcor = [] 
listang = []
colorlist = [(127, 0, 255), "indigo", "blue", "green", "yellow", "orange", "red"]
listpoly = []
l1 = []
l2 = []
ty = 0
t.fd(50)
t.lt(90)
t.fd(50)
listcor.append(t.pos())
t.home()
listang.append(t.towards(100,100))
style = ('Courier', 15, 'italic')
t.write('To stop animation click space and wait', font=style, align='center')
for (i,a,b) in zip(range(0,int(inp)), listcor, listang):
    t.goto(a)
    b += 90
    t.lt(b)
    t.fd(50)
    listcor.append(t.pos())
    x = t.pos()
    t.home()
    listang.append(t.towards(x))
listcor.insert(0, (50,0))
for i in listcor:
    try:
        l1.append(i)
        l2.append(listcor[int(listcor.index(i))+1])
    except IndexError:
        break
l1.pop()
#coloring
while ty == 0:
    for (a,b) in zip(l1, l2):
        if ty == 0:
            t.goto(home)
            t.color(colorlist[0])
            colorlist.insert(0, colorlist.pop())
            t.begin_fill()
            t.color()
            t.goto(a)
            t.goto(b)
            t.goto(home)
            t.end_fill()
        else:
            break
turtle.exitonclick()