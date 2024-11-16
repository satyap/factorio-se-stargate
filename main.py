# Calculate the stargate input
import configparser

import src.glyph as glyph
import src.point as point
import src.triangle as triangle

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
    return point.closest(target, candidates)


def build_triangle(stage):
    """Returns a triangle built up for the given stage"""
    top = point.parse(config[stage]["top"], "a63")
    left = point.parse(config[stage]["left"], "a61")
    right = point.parse(config[stage]["right"], "a62")
    return triangle.build(top, left, right)


def verify_coords():
    # print the distances between each point and its closest other point
    a = []
    for i, g in enumerate(glyph.LIST):
        a.append(point.parse(config["starmap"][g], g))
    for x in a:
        d_min = 2
        p2 = None
        for y in a:
            d = x.d2(y)
            if 1.0006219870614416e-26 < d < d_min:
                d_min = d
                p2 = y
        print(d_min, x, p2)


def verify_triangle(stage):
    top = point.parse(config[stage]["top"], "top")
    left = point.parse(config[stage]["left"], "left")
    right = point.parse(config[stage]["right"], "right")
    print(f"{stage}{left}")
    print(f"{stage}{right}")
    print(f"{stage}{top}")
    print(f"{stage} verification --v")
    print(top.d2(left))
    print(top.d2(right))
    print(left.d2(right))
    print(f"^-- verification of {stage}")


if __name__ == "__main__":
    # verify_coords()
    print(target)
    starting = starting_point()
    print(f"start: {starting}")
    for stg in ("s2", "s3", "s4", "s5", "s6", "s7", "s8"):
        verify_triangle(stg)
        t = build_triangle(stg)
        print(f"{stg}-next: {t.nearest(target)}")
