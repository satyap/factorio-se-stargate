# Calculate the stargate input
import configparser

import point

config = configparser.ConfigParser()
config.read("starmap.ini")
config.read("stargate.ini")


def starting_point():
    foenestra = point.parse(config["stargate"]["foenestra"], "foenestra")
    reverse = point.Point(-foenestra.x, -foenestra.y, -foenestra.z)
    candidates = []
    for k, v in config["starmap"].items():
        candidates.append(point.parse(v, k))
    closest_point = point.closest(reverse, candidates)

    print(f"start: {closest_point}")


if __name__ == "__main__":
    starting_point()
