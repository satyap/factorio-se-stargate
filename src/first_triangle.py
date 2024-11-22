from numpy import array
from numpy.linalg import norm

from src import point


def centroid(pts: list[point.Point], name) -> point.Point:
    v = array([
        sum([p.x for p in pts]) / len(pts),
        sum([p.y for p in pts]) / len(pts),
        sum([p.z for p in pts]) / len(pts),
    ])
    u = v / norm(v)
    return point.Point(
        x=u[0],
        y=u[1],
        z=u[2],
        glyph=name,
    )


class FirstTriangle:
    def __init__(self, starmap, corners):
        """
        Calculate triangle corners from the adjacent glyph positions.
        :param starmap:
        :param corners:
        """
        self.starmap = starmap
        self.corners = corners
        self.c_middle = self._point(corners["middle"])
        self.lefts = self._points("lefts")
        self.rights = self._points("rights")
        self.tops = self._points("tops")

    def _point(self, key):
        return point.parse(self.starmap[key], key)

    def top(self) -> point.Point:
        return centroid(self.tops, "top")

    def left(self) -> point.Point:
        return centroid(self.lefts, "left")

    def right(self) -> point.Point:
        return centroid(self.rights, "right")

    def _points(self, key):
        pts = [self._point(g.strip()) for g in self.corners[key].split(',') if g]
        pts.append(self.c_middle)
        return pts
