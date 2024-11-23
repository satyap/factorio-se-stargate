# Calculate the stargate input
import configparser
from math import degrees

from src import triangle as triangle, point as point

config = configparser.ConfigParser()
config.read("starmap.ini")
config.read("stargate.ini")

foenestra = point.parse(config["stargate"]["foenestra"], "foenestra")
target = point.Point(-foenestra.x, -foenestra.y, -foenestra.z, "tgt")


def starting_point():
    """Return the first coordinate"""
    candidates = []
    for k, v in config["starmap"].items():
        candidates.append(point.parse(v, k))
    print(target)
    start, angle = point.closest(target, candidates)
    print(f"start: {start.glyph} (angle: {degrees(angle)} degrees)")


def load_triangle(stage):
    """Returns a triangle built up for the given stage"""
    top = point.parse(config[stage]["top"], "a63")
    left = point.parse(config[stage]["left"], "a61")
    right = point.parse(config[stage]["right"], "a62")
    print(f"left side length: {top.d2(left)}")
    print(f"right side length: {top.d2(right)}")
    print(f"bottom length: {left.d2(right)}")
    t = triangle.Triangle(left=left, right=right, top=top)
    if not target.passes_through(t):
        raise RuntimeError("target doesn't pass through triangle")
    return t


if __name__ == "__main__":
    starting_point()
    for stg in ("s2", "s3", "s4", "s5", "s6", "s7", "s8"):
        tr = load_triangle(stg)
        tr.build()
        print(f"{stg}-next: {tr.nearest(target)[1:3]}")
