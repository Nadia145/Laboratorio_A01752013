'''Continuar con una aplicación que implica una inteligencia muy sencilla conocida por la 
mayoría pero que requiere una actualización para manejar una funcionalidad adicional.'''

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#List of color for food and snake
list_colors = ["black", "green", "yellow", "blue", "pink"]#lista sin color rojo
#Asign color randomly at the start of the game
color_snake = str(list_colors[randrange(0,4)])#Select snake color
list_colors.remove(color_snake)#Remove color of snake from list
color_food = str(list_colors[randrange(0,4)])#Select food color

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    #If snake head inside sneak end the game
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    #The food will appear randomnly in a short range
    if head == food:#If snake eat food extend snake
        print('Snake:', len(snake))
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #create body of snake
        square(body.x, body.y, 9, color_snake)
    #create food of snake
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()