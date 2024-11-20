from unittest import TestCase

import src.triangle as triangle
from src import point


class TestTriangle(TestCase):
    def test_build(self):
        t = triangle.Triangle(
            left=point.Point(0, 0, 0, "left"),
            right=point.Point(16, 0, 0, "right"),
            top=point.Point(8, 16, 0, "top"),
        )
        t.build()

        top_tr = t[0][0]
        self.assertEqual(top_tr.left, point.Point(7, 14, 0))
        self.assertEqual(top_tr.right, point.Point(9, 14, 0))
        self.assertEqual(top_tr.top, point.Point(8, 16, 0))

        # 2nd row, left (upward)
        self.assertEqual(t[1][0].left, point.Point(6, 12, 0))
        self.assertEqual(t[1][0].right, point.Point(8, 12, 0))
        self.assertEqual(t[1][0].top, point.Point(7, 14, 0))

        # 2nd row middle (down-pointing)
        self.assertEqual(t[1][1].left, point.Point(9, 14, 0))
        self.assertEqual(t[1][1].right, point.Point(7, 14, 0))
        self.assertEqual(t[1][1].top, point.Point(8, 12, 0))

        # 2nd row, right (upward)
        self.assertEqual(t[1][2].left, point.Point(8, 12, 0))
        self.assertEqual(t[1][2].right, point.Point(10, 12, 0))
        self.assertEqual(t[1][2].top, point.Point(9, 14, 0))


