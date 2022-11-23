from turtle import *
from math import exp


def draw_branch(branch_length, angle):
    if branch_length > 5:
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle)
        left(2 * angle)
        # unlock to "SEE" the recursion
        # pensize(int(branch_length / 10 / exp(-branch_length / 150)))
        draw_branch(branch_length - 15, angle)
        right(angle)
        backward(branch_length)
        # lock pensize and unlock it above to "SEE" the recursion
        pensize(int(branch_length / 10 / exp(-branch_length / 150)))


def draw_tree(trunk_length, angle):
    color("darkred")    #adding some color
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle)
    done()


draw_tree(100, 30)

