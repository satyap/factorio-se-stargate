from _decimal import Decimal
from math import sqrt

from src import point
from numpy import cross, dot, subtract


class Triangle(list):
    def __init__(self, left: point.Point, right: point.Point, top: point.Point, center: point.Point):
        super().__init__()
        self.left = left
        self.right = right
        self.top = top
        self.center = center
        for x in range(8):
            self.append([])
        self._build()

    def nearest(self, target) -> (Decimal, Decimal, Decimal):
        """Return a sub-triangle that is closest to the projection of the target into the triangle's plane"""
        min_d = 200
        out_x = None
        out_y = None
        p_next = None
        projected_target = self.project(target)
        for y, i in enumerate(self):
            for x, j in enumerate(i):
                d = j.d2(projected_target)
                if d < min_d:
                    min_d = d
                    out_x = x
                    out_y = y
                    p_next = j
        return out_y, out_x + 7 - out_y, sqrt(min_d), p_next  # glyphs are named with y-coord first :(

    def _build(self):
        """Build up a triangle of coordinates based on the corners"""
        left_side_coords = point.divide(self.top, self.left, 9)
        right_side_coords = point.divide(self.top, self.right, 9)
        for row in range(8):
            upper_coords = point.divide(left_side_coords[row], right_side_coords[row], row + 1)
            lower_coords = point.divide(left_side_coords[row + 1], right_side_coords[row + 1], row + 2)
            self[row] = self.calc_triangles(upper_coords, lower_coords)
        print(self.center)
        print((self.left.x + self.right.x + self.top.x) / 3)

    @staticmethod
    def calc_triangles(upper_coords, lower_coords):
        """
        Calculate the centroid coordinates of a row sub-triangles given by the coords of their "upper"
        and "lower" points
        """
        centroids = []
        for i, lower in enumerate(lower_coords):
            # upward triangle:
            if i < len(lower_coords) - 1:
                centroids.append(point.centroid(lower, lower_coords[i + 1], upper_coords[i]))
                # and downward triangle:
                if i > 0:
                    centroids.append(point.centroid(lower, upper_coords[i - 1], upper_coords[i]))
        return centroids

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
