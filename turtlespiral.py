import turtle, time
import itertools
from random import randint, randrange
def func():
    global ty
    style = style = ('Courier', 15, 'bold')
    t.color("yellow")
    t.write('Now click on this screen and quit', font=style, align='center')
    ty = 1
turtle.onkeypress(func, key='space')
screen = turtle.Screen()
screen.listen()
home = (0, 0)
inp = int(turtle.textinput("Enter the ending value", "The spiral shall end at √:"))
fdval = int(turtle.textinput("Enter the scale", "How big the spiral should be in %(10-small, 100-big)"))
t = turtle.Turtle()
t.ht()
style = ('Courier', 15, 'bold')
t.write('To stop animation click space and wait', font=style, align='center')
turtle.colormode(255)
time.sleep(2)
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