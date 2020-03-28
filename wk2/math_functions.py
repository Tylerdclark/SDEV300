#  math_functions.py
"""defines 4 math functions (sin, cos, sqrt, log10) that take start and stop and increment values as arguments"""
from math import sin, cos, pi, sqrt, log10


def sin_output(start, stop, increment):
    """"""
    print('input / sin output')
    while stop >= start:
        x_value = start
        y_value = sin(start)
        print(f'{x_value:.2f}  {y_value:.2f}')
        start = x_value + increment


def cos_output(start, stop, increment):
    print('input / cos output')
    while stop >= start:
        x_value = start
        y_value = cos(start)
        print(f'{start:.2f}  {y_value:.2f}')
        start = x_value + increment


def sqrt_output(start, stop, increment):
    print('input / sqrt output')
    while stop >= start:
        x_value = start
        y_value = sqrt(start)
        print(f'{start:.2f}  {y_value:.2f}')
        start = x_value + increment


def log10_output(start, stop, increment):
    print('input / log10 output')
    while stop >= start:
        if start == 0:
            print('0 undefined')
            start += increment
        else:
            x_value = start
            y_value = log10(start)
            print(f'{start:.2f}  {y_value:.2f}')
            start = x_value + increment


# sin_output(-2 * pi, 2 * pi, pi / 64)
# cos_output(-2 * pi, 2 * pi, pi / 64)
log10_output(0, 200, 0.5)
# file_writer = open("math_output2.txt", "w")
# for i in range(10):
#     file_writer.write("This is line %d\r\n" % (i + 1))
# file_writer.close()
