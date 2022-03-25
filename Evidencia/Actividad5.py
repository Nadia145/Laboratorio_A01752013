from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(["U0001F600"]) * 2
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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))


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