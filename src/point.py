from typing import List

from numpy import array

from src.vectors import vector_intersects_triangle, angle_between


class Point:
    """Point in 3D space. Or, a vector from (0,0,0) to this point."""

    def __init__(self, x: float, y: float, z: float, glyph: str = None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.glyph = glyph

    def d2(self, other):
        """Square of distance from another point."""
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def __str__(self) -> str:
        return f"{self.glyph}: ({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

    def angle(self, other):
        """Angle between this vector and another, in radians"""
        return angle_between(self.vector(), other.vector())

    def vector(self):
        """Convert to array so numpy can handle it"""
        return array([self.x, self.y, self.z])

    def passes_through(self, triangle):
        """Returns true if this point's vector passes through the triangle"""
        # Using Moller-Trumbore intersection algorithm:
        return vector_intersects_triangle(
            triangle.right.vector(),
            triangle.left.vector(),
            triangle.top.vector(),
            array([0, 0, 0]),
            self.vector(),
        )


def parse(s: str, glyph: str) -> Point:
    """
    Parse a string like (x,y,z) into a Point.
    """
    s = s.strip().replace(" ", "")
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1]
    x, y, z = s.split(",")
    return Point(x.strip(), y.strip(), z.strip(), glyph)


def closest(target: Point, candidates: List[Point]) -> (Point, float):
    """Return the coordinate that passes closest to the target vector"""
    nearest = None
    angle = None
    for candidate in candidates:
        if not nearest or angle > candidate.angle(target):
            nearest = candidate
            angle = nearest.angle(target)
    return nearest, angle


def segment(p1: Point, p2: Point, m: int, n: int) -> Point:
    """Return the point that segments p1->p2 in m:n parts"""
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
