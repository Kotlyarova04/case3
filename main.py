'''
Kotlyarova Polina
Rafaevich Vita
'''
import turtle as t
import math


def get_num_hexagons(num):
    return num


def get_color_choice(colour):
    return colour


def draw_hexagons(x, y, side_len, colour, pencolour):
    """
    Function for drawing a hexagons.
    :param x: first coordinate of the start of drawing hexagons
    :param y: second coordinate
    :param colour: hexagons fillcolor
    :return: None
    """
    t.goto(x, y)
    t.color(colour, pencolour)
    t.begin_fill()
    t.pd()
    for i in range(2):
        t.rt(30)
        t.forward(side_len)
        t.rt(60)
        t.forward(side_len)
        t.rt(60)
        t.forward(side_len)
        t.rt(30)
    t.end_fill()


print('''Допустимые цвета заливки:
красный
синий
зеленый
желтый
оранжевый
пурпурный
розовый
''')
colour = input("Пожалуйста, введите первый цвет: ")
colour1 = input("Пожалуйста, введите второй цвет: ")
number = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:"))

t.speed(100)
y1 = 500 / (2 * number)
x = (0.57735 * y1)
y = 500 / (2 * number)
side_len = 2 * x

for i in range(1, number + 1):
    t.pu()
    for j in range(1, number + 1):
        colour, colour1 = colour1, colour
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour)
        x += math.sqrt(3) * side_len
    x = (0.57735 * y1)
    y += 3 * side_len / 2
    if i % 2 != 0:
        x += math.sqrt(3) * side_len / 2
    else:
        colour, colour1 = colour1, colour
        x = (0.57735 * y1)

t.done()
