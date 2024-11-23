import numpy as np
from numpy import ndarray, dot, arccos, clip, pi
from numpy.linalg import norm


def angle_between(v1: ndarray, v2: ndarray):
    c = dot(v1, v2) / norm(v1) / norm(v2)
    return arccos(clip(c, -1, 1))


def vector_intersects_triangle(v0, v1, v2, origin, direction):
    # code from google AI
    """
    Checks if a ray intersects a triangle.

    Args:
        v0, v1, v2 (numpy.ndarray): Vertices of the triangle.
        origin (numpy.ndarray): Origin of the ray.
        direction (numpy.ndarray): Direction of the ray.

    Returns:
        bool: True if the ray intersects the triangle, False otherwise.
    """

    # Compute the normal of the triangle
    normal = np.cross(v1 - v0, v2 - v0)

    # Check if the ray is parallel to the triangle
    if np.dot(normal, direction) == 0:
        return False

    # Compute the intersection point between the ray and the plane of the triangle
    t = np.dot(normal, v0 - origin) / np.dot(normal, direction)

    if t < 0:
        return False

    # Compute the intersection point
    intersection_point = origin + t * direction

    # Check if the intersection point is inside the triangle
    return is_point_inside_triangle(v0, v1, v2, intersection_point)


def is_point_inside_triangle(v1, v2, v3, v0):
    # Using "2PI is the sum of angles between vectors from corners to target":
    angle1 = angle_between(v1 - v0, v2 - v0)
    angle2 = angle_between(v2 - v0, v3 - v0)
    angle3 = angle_between(v3 - v0, v1 - v0)
    diff = abs(angle1 + angle2 + angle3 - 2 * pi)
    # the epsilon of 0.0001 may be imprecise, but it works for me.
    return diff < 0.0001
