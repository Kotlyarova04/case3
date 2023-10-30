"""
Kotlyarova Polina
Rafaevich Vita
"""
import turtle as t
import math
from deep_translator import GoogleTranslator


def get_num_hexagons():
    while True:
        num = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд:"))
        if 4 <= num <= 20:
            return num
        print("Ошибка, оно должно быть от 4 до 20")


def get_color_choice():
    colors = ["красный", "синий", "зеленый", "желтый", "оранжевый", "пурпурный", "розовый"]
    while True:
        colour_1 = input("Пожалуйста, введите первый цвет (красный, синий, зеленый, желтый, оранжевый, пурпурный, "
                         "розовый): ")
        if colour_1.lower() in colors:
            break
        print("Пожалуйста, повторите попытку")
    while True:
        colour_2 = input("Пожалуйста, введите второй цвет (красный, синий, зеленый, желтый, оранжевый, пурпурный, "
                         "розовый): ")
        if colour_2.lower() in colors and colour_2.lower() != colour_1.lower():
            break
        print("Пожалуйста, повторите попытку. Возможно, введенный цвет уже был использован")
    return colour_1, colour_2


def translate(col):
    translated = GoogleTranslator(source='auto', target='en').translate(col)
    return translated


def draw_hexagons(x, y, side_len, colour):
    t.goto(x, y)
    t.fillcolor(colour)
    t.begin_fill()
    t.pd()
    for _ in range(2):
        t.rt(30)
        t.forward(side_len)
        t.rt(60)
        t.forward(side_len)
        t.rt(60)
        t.forward(side_len)
        t.rt(30)
    t.end_fill()


colour_1, colour_2 = get_color_choice()
colour_1, colour_2 = translate(colour_1), translate(colour_2)
num_hexagons = get_num_hexagons()

y1 = -500 / (2 * num_hexagons)
x = -(math.sqrt(3) * y1)/3
y = -500 / (2 * num_hexagons)
side_len = 2 * x

t.speed(200)
for i in range(1, num_hexagons + 1):
    t.pu()
    for j in range(1, num_hexagons + 1):
        colour_1, colour_2 = colour_2, colour_1
        t.pu()
        draw_hexagons(x, y, side_len, colour_1)
        x += math.sqrt(3) * side_len
    x = -(0.57735 * y1)
    y += 3 * side_len / 2
    if i % 2 != 0:
        x += math.sqrt(3) * side_len / 2
    else:
        colour_1, colour_2 = colour_2, colour_1
        x = -(0.57735 * y1)
t.done()
