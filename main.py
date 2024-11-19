# Calculate the stargate input
import configparser

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
    start, dist = point.closest(target, candidates)
    print(f"start: {start.glyph} (distance: {dist}")


def all_symbols():
    top = point.parse(config["corners"]["top"], "a63")
    left = point.parse(config["corners"]["left"], "a61")
    right = point.parse(config["corners"]["right"], "a62")
    t = triangle.Triangle(left=left, right=right, top=top)
    t.build()
    for i in range(2, 9):
        t, y, x = t.nearest(target)
        print(f"symbol {i}: {y}, {x}")
        t.build()


if __name__ == "__main__":
    starting_point()
    all_symbols()
