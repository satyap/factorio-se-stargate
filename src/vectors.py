# code from google AI
import numpy as np


def vector_intersects_triangle(v0, v1, v2, origin, direction):
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
    if is_point_inside_triangle(v0, v1, v2, intersection_point):
        return True
    else:
        return False


def is_point_inside_triangle(v0, v1, v2, point):
    """
    Checks if a point is inside a triangle using the barycentric coordinates method.

    Args:
        v0, v1, v2 (numpy.ndarray): Vertices of the triangle.
        point (numpy.ndarray): Point to check.

    Returns:
        bool: True if the point is inside the triangle, False otherwise.
    """

    # Compute the barycentric coordinates
    v1 = v1 - v0
    v2 = v2 - v0
    p = point - v0

    dot00 = np.dot(v1, v1)
    dot01 = np.dot(v1, v2)
    dot02 = np.dot(v1, p)
    dot11 = np.dot(v2, v2)
    dot12 = np.dot(v2, p)

    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    return (u >= 0) and (v >= 0) and (u + v < 1)
