import turtle
import random


class Polygon:
    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = color
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = get_new_color()
        self.border_size = random.randint(1, 10)

    def reposition(self):
        turtle.penup()
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

    def reduction(self):
        self.size *= self.reduction_ratio

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


sides = int(input('Which art do you want to generate? Enter a number between 1 to 8, inclusive: '))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
color = get_new_color()
reduction_ratio = 0.618
polygon_1 = Polygon(sides-1, color)
polygon = Polygon(sides, color)
polygon1 = Polygon(sides+1, color)
polygon2 = Polygon(sides+2, color)
polygon3 = Polygon(3, color)
polygon4 = Polygon(4, color)
polygon5 = Polygon(5, color)
if sides <= 3:
    for i in range(10):
        polygon2.draw_polygon()
        polygon2.reposition()
        polygon2.reposition()
        polygon2.reposition()
        polygon2.reduction()
elif sides == 4:
    for i in range(10):
        polygon1.draw_polygon()
        polygon1.reposition()
        polygon1.reduction()
        polygon.draw_polygon()
        polygon.reposition()
        polygon.reduction()
        polygon_1.draw_polygon()
        polygon_1.reposition()
        polygon_1.reduction()

# elif sides == 5:
#     # for j in range(20):
#         for k in range(4):
#             polygon3.draw_polygon()
#             polygon3.reduction()
#             polygon3.draw_polygon()
#

            
# hold the window; close it by clicking the window close 'x' mark
turtle.done()