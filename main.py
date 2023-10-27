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
    '''
    Function for drawing a hexagons.
    :param x: first coordinate of the start of drawing hexagons
    :param y: second coordinate of the start of drawing hexagons
    :param a: length of the side
    :param color: hexagons fillcolor
    :return: None
    '''
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

number = int(input())
side_len = int(input())
colour = input()
colour1 = input()
t.speed(100)
x = 0
y = 0
for i in range(number//2):
    colour, colour1 = colour1, colour
    t.pu()
    for i in range(number//2):
        colour, colour1 = colour1, colour
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour)
        y += 2 * math.sqrt(3) * side_len
    y = 0
    x += 2*math.sqrt(3) * side_len
x = 0
y = 0
for i in range(number-number//2):
    t.pu()
    x += math.sqrt(3) * side_len
    for i in range(number-number//2):
        colour, colour1 = colour1, colour
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour)
        y += 2 * math.sqrt(3) * side_len
    colour, colour1 = colour1, colour
    y = 0
    x += math.sqrt(3) * side_len
x = 0
y = 0
for i in range(number-number//2):
    colour, colour1 = colour1, colour
    t.pu()
    x += math.sqrt(3) * side_len/2
    y += math.sqrt(3) * side_len
    for i in range(number-number//2):
        colour, colour1 = colour1, colour
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour)
        y += 2*math.sqrt(3) * side_len
    y = 0
    x += 3*math.sqrt(3) * side_len/2
x = 0
y = 0
for i in range(number-number//2):
    t.pu()
    x += 3*math.sqrt(3) * side_len/2
    y += math.sqrt(3) * side_len
    for i in range(number-number//2):
        colour, colour1 = colour1, colour
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour)
        y += 2*math.sqrt(3) * side_len
    colour, colour1 = colour1, colour
    y = 0
    x += math.sqrt(3) * side_len/2


t.done()