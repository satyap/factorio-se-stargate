from unittest import TestCase

import src.point as point


class TestPoint(TestCase):
    def test_divide(self):
        p1 = point.Point(0, 5, 0, "p1")
        p2 = point.Point(100, 0, 5, "p2")

        p3 = point.Point(50, 2.5, 2.5, "p3")

        p4 = point.Point(20, 4, 1, "p4")
        p5 = point.Point(40, 3, 2, "p5")
        p6 = point.Point(60, 2, 3, "p6")
        p7 = point.Point(80, 1, 4, "p7")
        self.assertEqual(
            point.divide(p1, p2, 2),
            [p1, p2],
        )
        self.assertEqual(
            point.divide(p1, p2, 3),
            [p1, p3, p2],
        )
        self.assertEqual(
            point.divide(p1, p2, 6),
            [p1, p4, p5, p6, p7, p2],
        )
