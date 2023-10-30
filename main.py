'''
Kotlyarova Polina
Rafaevich Vita
'''
import turtle as t
import math


def get_num_hexagons():
    while True:
        num = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:"))
        if 4 <= num <= 20:
            return num
        print("Ошибка, оно должно быть от 4 до 20")



def get_color_choice():
    print('''Допустимые цвета заливки:
    красный
    синий
    зеленый
    желтый
    оранжевый
    пурпурный
    розовый
    ''')
    colors = ["red", "blue", "зеленый", "желтый", "оранжевый", "пурпурный", "розовый"]
    colour = input("Пожалуйста, введите первый цвет: ")
    colour1 = input("Пожалуйста, введите второй цвет: ")
    if colour in colors:
        return colour, colour1


def draw_hexagons(x, y, side_len, colour, pencolour):
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


colour_1, colour_2 = get_color_choice()
num_hexagons = get_num_hexagons()

y1 = 500 / (2 * num_hexagons)
x = (0.57735 * y1)
y = 500 / (2 * num_hexagons)
side_len = 2 * x

for i in range(1, num_hexagons + 1):
    t.pu()
    for j in range(1, num_hexagons + 1):
        colour_1, colour_2 = colour_2, colour_1
        t.pu()
        draw_hexagons(x, y, side_len, 'black', colour_1)
        x += math.sqrt(3) * side_len
    x = (0.57735 * y1)
    y += 3 * side_len / 2
    if i % 2 != 0:
        x += math.sqrt(3) * side_len / 2
    else:
        colour_1, colour_2 = colour_2, colour_1
        x = (0.57735 * y1)

t.done()
