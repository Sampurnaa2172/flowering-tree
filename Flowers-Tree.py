# -*- coding: utf-8 -*-
"""
@author: Sampurnaa
"""
import random
from math import sqrt
from turtle import *

CHECK = False
BRANCH_LENGTH = 60
FAN = 12
class FloweringTree:
    def __init__(self):
        self.petal_count = 0
        self.petal_left_border = 0
        self.petal_right_border = 0
        self.turtle = Turtle()
        self.frame = Screen()
        if CHECK:
            self.frame.tracer(0, 0)
        else:
            self.frame.tracer(3, 0)
        self.frame.bgcolor('grey')
        self.turtle.speed(10)
        self.turtle.up()

    def tree(self, branch_len):
        if branch_len > 3:
            if 8 <= branch_len <= 12:
                if random.randint(0, 2) == 0:
                    self.turtle.color('snow')
                else:
                    self.turtle.color('red')
                self.turtle.pensize(branch_len / 3)
            elif branch_len < 8:
                self.petal_count += 1
                cur_x = self.turtle.pos()[0]
                if cur_x < 0:
                    self.petal_left_border = min(self.petal_left_border, cur_x)
                else:
                    self.petal_right_border = max(self.petal_right_border, cur_x)
                if random.randint(0, 1) == 0:
                    self.turtle.color('purple')
                else:
                    self.turtle.color('pink')
                self.turtle.pensize(branch_len / 2)
            else:
                self.turtle.color('black')
                self.turtle.pensize(branch_len / 10)

            #branch/leaf
            self.turtle.down()
            self.turtle.forward(branch_len)
            self.turtle.up()

            random_angle = 3 + 2 * FAN * random.random()
            random_length = FAN * random.random()

            self.turtle.right(random_angle)
            self.tree(branch_len - random_length)
            self.turtle.left(2 * random_angle)
            self.tree(branch_len - random_length)
            self.turtle.right(random_angle)

            
            self.turtle.up()
            self.turtle.backward(branch_len)

    def petal_field(self, count, left_border=-100, right_border=100):
        middle = (right_border + left_border) / 2
        frame_width = (right_border - left_border) / 3
        depth = int(sqrt(frame_width))
        _start_pos = self.turtle.pos()
        start_pos = (middle, _start_pos[1] + depth / 2 - BRANCH_LENGTH / 10)
        self.turtle.goto(start_pos)

        for _ in range(count):
            random_width = frame_width - 2 * frame_width * random.random()
            random_depth = depth - 2 * depth * random.random()
            self.turtle.forward(random_depth)
            self.turtle.left(90)
            self.turtle.forward(random_width)
            self.turtle.down()
            if random.randint(0, 1) == 0:
                self.turtle.color("snow")
            else:
                self.turtle.color("pink")
            rand_size = random.random()
            self.turtle.pensize(2.5 * rand_size)
            self.turtle.circle(rand_size)
            self.turtle.up()
            self.turtle.right(90)
            self.turtle.goto(start_pos)
        # Repaint the covered branch
        self.turtle.goto(_start_pos)
        self.turtle.color('black')
        self.turtle.pensize(BRANCH_LENGTH // 10)
        self.turtle.down()
        self.turtle.forward(BRANCH_LENGTH)
        self.turtle.up()
    def signature(self):
        start_pos = self.turtle.pos()
        self.turtle.color('black')
        self.turtle.goto(start_pos)

    def draw(self):
        try:
            self.turtle.left(90)
            self.turtle.backward(250)
            self.tree(BRANCH_LENGTH)
            self.petal_count = self.petal_count // (int(sqrt(2 * FAN)))
            self.petal_field(self.petal_count, self.petal_left_border, self.petal_right_border)
            self.turtle.backward(100)
            self.signature()
            self.turtle.color('wheat')
            self.turtle.down()
            self.turtle.forward(20)
            self.frame.exitonclick()
        except KeyboardInterrupt:
            print('Keyboard Interrupt.')


if __name__ == '__main__':
    flowering_tree = FloweringTree()
    flowering_tree.draw()
