import math
from _decimal import Decimal
from math import sqrt
from typing import List
import numpy

from src.vectors import vector_intersects_triangle


class Point:
    """Point in 3D space"""

    def __init__(self, x: Decimal, y: Decimal, z: Decimal, glyph: str = None):
        self.x = Decimal(x)
        self.y = Decimal(y)
        self.z = Decimal(z)
        self.glyph = glyph
        self.theta = self._theta()
        self.phi = self._phi()

    def d2(self, other):
        """Square of distance from another point."""
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def __str__(self) -> str:
        return f"{self.glyph}: ({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return self.__str__()

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def vector(self):
        """Convert to array so numpy can handle it"""
        return [self.x, self.y, self.z]

    def _theta(self):
        """Return spherical coordinate angle theta"""
        return math.atan2(self.y, self.x)

    def _phi(self):
        """Return spherical coordinate angle phi"""
        s = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return math.acos(self.z / Decimal(s))

    def passes_through(self, triangle):
        """Returns true if this point's vector passes through the triangle"""
        return vector_intersects_triangle(
            numpy.array(triangle.left.vector()),
            numpy.array(triangle.top.vector()),
            numpy.array(triangle.right.vector()),
            numpy.array([0, 0, 0]),
            numpy.array(self.vector()),
        )
        # min_theta = min(triangle.left.theta, triangle.right.theta, triangle.top.theta)
        # max_theta = max(triangle.left.theta, triangle.right.theta, triangle.top.theta)
        # min_phi = min(triangle.left.phi, triangle.right.phi, triangle.top.phi)
        # max_phi = max(triangle.left.phi, triangle.right.phi, triangle.top.phi)
        # theta_match = min_theta <= self.theta <= max_theta
        # phi_match = min_phi <= self.phi <= max_phi
        # return theta_match and phi_match


def parse(s: str, glyph: str) -> Point:
    """
    Parse a string like (x,y,z) into a Point.
    """
    s = s.strip().replace(" ", "")
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1]
    x, y, z = s.split(",")
    return Point(x.strip(), y.strip(), z.strip(), glyph)


def closest(target: Point, candidates: List[Point]) -> (Point, Decimal):
    nearest = None
    for candidate in candidates:
        if not nearest or nearest.d2(target) > candidate.d2(target):
            nearest = candidate
    return nearest, sqrt(nearest.d2(target))


def segment(p1: Point, p2: Point, m: int, n: int) -> Point:
    x = (n * p1.x + m * p2.x) / (m + n)
    y = (n * p1.y + m * p2.y) / (m + n)
    z = (n * p1.z + m * p2.z) / (m + n)
    return Point(x, y, z, None)


def divide(p1: Point, p2: Point, k: int) -> List[Point]:
    """
    Divide the line joining p1 and p2 into equal parts.
    Return the k points from p1 to p2, including p1 and p2.
    """
    points = []
    if k == 1:
        return [p1]
    for m in range(0, k):
        n = k - m - 1
        points.append(segment(p1, p2, m, n))
    return points
