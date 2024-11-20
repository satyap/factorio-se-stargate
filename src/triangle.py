from _decimal import Decimal

from src import point
from numpy import cross, dot, subtract


class Triangle(list):
    def __init__(self, left: point.Point, right: point.Point, top: point.Point, center: point.Point = None):
        super().__init__()
        self.left = left
        self.right = right
        self.top = top
        self.center = center
        for x in range(8):
            self.append([])

    def nearest(self, target: point.Point) -> (object, int, int):
        """Return a sub-triangle that the target vector passes through"""
        for row, i in enumerate(self):
            for col, j in enumerate(i):
                if target.passes_through(j):
                    return j, row, col + 7 - row
        raise RuntimeError("out of triangle")

    def build(self):
        """Build up a triangle of coordinates based on the corners"""
        left_side_coords = point.divide(self.top, self.left, 9)
        right_side_coords = point.divide(self.top, self.right, 9)
        for row in range(8):
            upper_coords = point.divide(left_side_coords[row], right_side_coords[row], row + 1)
            lower_coords = point.divide(left_side_coords[row + 1], right_side_coords[row + 1], row + 2)
            self[row] = self.calc_triangles(upper_coords, lower_coords)

    @staticmethod
    def calc_triangles(upper_coords, lower_coords):
        """
        Put together the corners of a row sub-triangles given by the coords of their "upper"
        and "lower" points. Each row starts with an upward triangle.
        """
        triangles = []
        for i, lower in enumerate(lower_coords):
            if i < len(lower_coords) - 1:
                if i > 0:
                    # downward triangle:
                    top = lower_coords[i]
                    right = upper_coords[i - 1]
                    left = upper_coords[i]
                    triangles.append(Triangle(left, right, top))
                # upward triangle:
                left = lower_coords[i]
                right = lower_coords[i + 1]
                top = upper_coords[i]
                triangles.append(Triangle(left, right, top))
        return triangles

    def _normal(self):
        """Find the normal vector: left - top and right - top, then cross product"""
        p1 = self.left - self.top
        p2 = self.right - self.top
        return cross(p1.vector(), p2.vector())

    def project(self, r: point.Point):
        """Project point r into the plane of the triangle"""
        # First get the vector from our triangle's center to the target
        r0 = self.center - r
        v3 = subtract(r0.vector(), r.vector())
        # Project it:
        d = dot(self.center.vector(), v3)
        m = [self.center.x * d, self.center.y * d, self.center.z * d]
        v3m = subtract(v3, m)
        p = subtract(r0.vector(), v3m)
        return point.Point(p[0], p[1], p[2], "projected_target")
