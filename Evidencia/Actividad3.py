'''Continuar con una aplicación que implica una inteligencia con un grado de dificultad
 mayor conocida por la mayoría pero que requiere una actualización
  para manejar una funcionalidad adicional.'''

from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
#Position of ghosts and directions
ghosts = [
   [vector(-180, 160), vector(10, 0)],
   [vector(-180, -160), vector(0, 10)],
   [vector(100, 160), vector(0, -10)],
   [vector(100, -160), vector(-10, 0)],
]
#The tiles were changed
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
   "Draw square using path at (x, y)."
   path.up()
   path.goto(x, y)
   path.down()
   path.begin_fill()

   for count in range(4):
       path.forward(20)
       path.left(90)

   path.end_fill()

def offset(point):
   "Return offset of point in tiles."
   x = (floor(point.x, 20) + 200) / 20
   y = (180 - floor(point.y, 20)) / 20
   index = int(x + y * 20)
   return index

def valid(point):
   "Return True if point is valid in tiles."
   index = offset(point)

   if tiles[index] == 0:
       return False

   index = offset(point + 19)

   if tiles[index] == 0:
       return False

   return point.x % 20 == 0 or point.y % 20 == 0

def world():
   "Draw world using path."
   bgcolor('black')
   path.color('blue')

   for index in range(len(tiles)):
       tile = tiles[index]

       if tile > 0:
           x = (index % 20) * 20 - 200
           y = 180 - (index // 20) * 20
           square(x, y)
           # Drawing of points
           if tile == 1:
               path.up()
               path.goto(x + 10, y + 10)
               path.dot(2, 'white')

def move():
   "Move pacman and all ghosts."
   writer.undo()
   writer.write(state['score'])

   clear()

   if valid(pacman + aim):
       pacman.move(aim)

   index = offset(pacman)

   if tiles[index] == 1:
       tiles[index] = 2
       state['score'] += 1
       x = (index % 20) * 20 - 200
       y = 180 - (index // 20) * 20
       square(x, y)

   up()
   goto(pacman.x + 10, pacman.y + 10)
   dot(20, 'yellow')#continue movement
   previous_plan = vector(0,0)
   plan = vector(0,0)
   for point, course in ghosts:
       if valid(point + course):
           point.move(course)

        #The velocity of the ghosts was changed
       else:
           options = [
               vector(10, 0),
               vector(-10, 0),
               vector(0, 10),
               vector(0, -10),
           ]
           if previous_plan == plan:  # verifies if we dont move in de same direction again
               plan = choice(options)
           # change course of movement
           course.x = plan.x
           course.y = plan.y
           previous_plan = plan

       up()
       goto(point.x + 10, point.y + 10)
       dot(20, 'red')#draw ghost

   update()

   for point, course in ghosts:
       if abs(pacman - point) < 5:
           return

   # Make ghosts more intelligent
   for point, course in ghosts:
       # If difference between pacman and ghost is less than 45 we change direction of ghosts to chace pacman
       if abs(pacman - point) < 45:
           if point.x > pacman.x:  # If the x position of ghosts is more than pacman's we move -x
               if valid(vector(point.x - 5, point.y)):  # verifies if the movement is viable in -x
                   course.x = -5  # Change course
           elif point.x < pacman.x:
               if valid(vector(point.x + 5, point.y)):  # verifies if the movement is viable in +x
                   course.x = 5
           elif point.y > pacman.y:  # If the x position of ghosts is more than pacman's we move -y
               if valid(vector(point.x, point.y - 5)):  # verifies if the movement is viable in -y
                   course.y = -5
           elif point.y < pacman.y:
               if valid(vector(point.x, point.y + 5)):  # verifies if the movement is viable in +y
                   course.y = 5

   ontimer(move, 100)

def change(x, y):
   "Change pacman aim if valid."
   if valid(pacman + vector(x, y)):
       aim.x = x
       aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()

