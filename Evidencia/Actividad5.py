'''Continuar con un juego que desarrolla la memoria para cambiar su
 funcionalidad, haciéndolo más interesante para el jugador.'''
 
from random import *
from tkinter import CENTER, LEFT, RIGHT
from turtle import *
from xml.etree.ElementTree import tostring
from freegames import path

car = path('car.gif')
list_em = [u'\ud83d\udd00',u'\ud83d\udd01',u'\ud83d\udd02',u'\ud83d\udd03',u'\ud83d\udd04',u'\ud83d\udd05',u'\ud83d\udd06',u'\ud83d\udd07',u'\ud83d\udd08'
           ,u'\ud83d\udd09',u'\ud83d\udd10',u'\ud83d\udd11',u'\ud83d\udd12',u'\ud83d\udd13',u'\ud83d\udd14',u'\ud83d\udd15',u'\ud83d\udd16',u'\ud83d\udd17'
           ,u'\ud83d\udd18',u'\ud83d\udd19',u'\ud83d\udd20',u'\ud83d\udd21',u'\ud83d\udd22',u'\ud83d\udd23',u'\ud83d\udd24',u'\ud83d\udd25',u'\ud83d\udd26'
           ,u'\ud83d\udd27',u'\ud83d\udd28',u'\ud83d\udd29',u'\ud83d\udd30',u'\ud83d\udd31']

tiles = list(list_em) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0 #variable for storing number of taps
square_count = 0 #variable for checking discovered squares

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global square_count
    global tap_count
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        #add 1 to tap count when tap interaction and print it
        tap_count += 1 
        print("Tap count :", tap_count)

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        #add 2 to count when 2 squares are revealed
        square_count += 2

    if square_count == 64:#If square count is 32 all squares have been discoverd
        print("Todos los cuadros estan destapados!!")


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    global square_count

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']


    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 5, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))  
        #if tiles[mark] < 10:
            #goto(x + 15, y)
            #color('black')
            #write(tiles[mark], font=('Arial', 30, 'normal'))  
        #else:    
            #goto(x + 4, y)
            #color('black')
            #write(tiles[mark], font=('Arial', 30, 'normal'))  
            


    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()