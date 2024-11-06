from typing import List


class Point:
    """Point in 3D space"""

    def __init__(self, x: float, y: float, z: float, glyph: str = None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.glyph = glyph

    def d2(self, other):
        """Square of distance from another point."""
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

    def __str__(self) -> str:
        return f"{self.glyph}: [{self.x}, {self.y}, {self.z}]"


def parse(s: str, glyph: str) -> Point:
    """
    Parse a string like [x,y,z] into a Point.
    """
    s = s.strip().replace(" ", "")
    if not s.startswith("[") or not s.endswith("]"):
        raise RuntimeError("Format of point: [x,y,z]")
    s = s[1:-1]
    x, y, z = s.split(",")
    return Point(x, y, z, glyph)


def closest(target: Point, candidates: List[Point]) -> Point:
    nearest = None
    for candidate in candidates:
        if not nearest or nearest.d2(target) > candidate.d2(target):
            nearest = candidate
    return nearest
