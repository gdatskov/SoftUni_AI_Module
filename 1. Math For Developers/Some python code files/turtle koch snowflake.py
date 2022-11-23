from turtle import *


def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            forward(a/3)
            left(t)
    else:
        forward(a)


# Test
koch(100, 0)
pensize(3)
koch(100, 1)