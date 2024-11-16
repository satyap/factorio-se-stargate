from _decimal import Decimal
from math import sqrt

from src import point


class Triangle(list):
    def __init__(self):
        super().__init__()
        for x in range(8):
            self.append([])

    def nearest(self, target) -> (Decimal, Decimal, Decimal):
        min_d = 200
        out_x = None
        out_y = None
        p_next = None
        for y, i in enumerate(self):
            for x, j in enumerate(i):
                d = j.d2(target)
                if d < min_d:
                    min_d = d
                    out_x = x
                    out_y = y
                    p_next = j
        return out_y, out_x + 7 - out_y, sqrt(min_d), p_next  # glyphs are named with y-coord first :(


def build(top: point.Point, left: point.Point, right: point.Point) -> Triangle:
    """Build up a triangle of coordinates based on the corners"""
    t = Triangle()
    left_side = point.divide(top, left, 15)
    right_side = point.divide(top, right, 15)
    for row, _ in enumerate(t):
        i = row * 2
        t[row] = point.divide(left_side[i], right_side[i], i+1)
    return t
