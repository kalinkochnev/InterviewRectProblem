import unittest
import RectanglesProblem as RP


class TestRectanglesProblem(unittest.TestCase):
    def setUp(self):
        self.standard_rect = RP.Rectangle(0, 0, 50, 50)

    def test_get_points(self):
        rect1 = RP.Rectangle(10, 25, 30, 100)
        rect2 = RP.Rectangle(25, 25, 200, 100)

        correct_output = dict(point1=(10, 25), point2=(40, 25), point3=(40, 125), point4=(10, 125))
        self.assertDictEqual(correct_output, rect1.all_pts)

        correct_output = dict(point1=(25, 25), point2=(225, 25), point3=(225, 125), point4=(25, 125))
        self.assertDictEqual(correct_output, rect2.all_pts)

    # tests when point is within the sides of the rect
    def test_point_in_rect_case1(self):
        points_in_rect = [(25, 22), (0.1, 0.1), (49.9, 49.9), (0.1, 49.9), (49.9, 0.1)]

        for point in points_in_rect:
            with self.subTest(point=point):
                self.assertTrue(self.standard_rect.pt_in_rect(point))

    # tests when point is not within the rect
    def test_point_in_rect_case2(self):
        points_not_in_rect = [(175, 60), (75, 50), (250, 10), (30, 0), (50, 40), (48, 50), (0, 30)]

        for point in points_not_in_rect:
            with self.subTest(point=point):
                self.assertFalse(self.standard_rect.pt_in_rect(point))

    # tests when points are on the side of the rect
    def test_point_on_side_case1(self):
        points_on_side = [(30, 0), (25, 0), (48, 50), (0, 30), (50, 50), (50, 0), (0, 50)]

        # case 1: points are on sides of standard_rect
        for point in points_on_side:
            with self.subTest(point=point):
                self.assertTrue(self.standard_rect.pt_on_side(point))

    # tests when points are not on the side of the rect
    def test_point_on_side_case2(self):
        points_not_on_side = [(25, 22), (0.1, 0.1), (49.9, 49.9), (0.1, 49.9), (49.9, 0.1)]

        # case 2: if not on side, its false
        for point in points_not_on_side:
            with self.subTest(point=point):
                self.assertFalse(self.standard_rect.pt_on_side(point))

    # tests when points are outside of the rectangle
    def test_point_out_of_rect_case1(self):
        points_not_in_rect = [(175, 60), (75, 50), (250, 10), (300, 52), (25, 100), (25, -100)]

        for point in points_not_in_rect:
            with self.subTest(point=point):
                self.assertTrue(self.standard_rect.pt_outside_rect(point))

    # tests when the points are inside of the rectangle
    def test_point_out_of_rect_case2(self):
        points_in_rect = [(25, 22), (0.1, 0.1), (49.9, 49.9), (0.1, 49.9), (49.9, 0.1), (50, 50), (30, 0), (0, 30),
                          (50, 40), (48, 50)]

        for point in points_in_rect:
            with self.subTest(point=point):
                self.assertFalse(self.standard_rect.pt_outside_rect(point))

    # TODO create test for number of points contained in one another
    def test_num_points_contained(self):
        pass

    """
        def test_num_points_in_boundary(self):
            pass
    
    
        def test_num_contained_points(self):
            pass
    
    
        def test_num_pts_on_sides(self):
            pass
    
    
        def test_num_pts_outside(self):
            pass
    """

    # tests when 2 points of rect1 are present in standard_rect
    def test_rect_intersection_case1(self):
        rect1 = RP.Rectangle(10, 25, 30, 100)

        # case 1: 2 points of rect1 present in standard_rect
        self.assertTrue(RP.is_intersecting(rect1, self.standard_rect))

    # tests when 1 point of rect2 is present in standard_rect
    def test_rect_intersection_case2(self):
        rect2 = RP.Rectangle(25, 25, 200, 125)

        self.assertTrue(RP.is_intersecting(rect2, self.standard_rect))

    # tests when all points of rect3 are outside of rect4 but still intersects
    def test_rect_intersection_case3(self):
        rect3 = RP.Rectangle(40, 0, 40, 100)
        rect4 = RP.Rectangle(0, 30, 100, 30)

        self.assertTrue(RP.is_intersecting(rect3, rect4))

    """
    DOES NOT WORK!
    def test_get_intersecting_pts(self):
        rect1 = RP.Rectangle(10, 25, 30, 100)
        rect2 = RP.Rectangle(25, 25, 200, 125)
        rect4 = RP.Rectangle(0, 30, 100, 30)
        rect3 = RP.Rectangle(40, 0, 40, 100)

        correct_values = [(10, 50), (40, 50)]
        self.assertListEqual(RP.get_intersecting_pts(self.standard_rect, rect1, (2, 0)), correct_values)
        self.assertListEqual(RP.get_intersecting_pts(rect1, self.standard_rect, (2, 0)), correct_values)

        correct_values = [(50, 25), (25, 50)]
        self.assertListEqual(RP.get_intersecting_pts(rect2, self.standard_rect, (1, 1)), correct_values)
        self.assertListEqual(RP.get_intersecting_pts(self.standard_rect, rect2, (1, 1)), correct_values)

        correct_values = [(40, 30), (80, 30), (40, 60), (80, 60)]
        self.assertListEqual(RP.get_intersecting_pts(rect4, rect3, (4, 4)), correct_values)
    """

    # tests when 4 points of rect6 contained in rect5
    def test_rect_contained_case1(self):
        rect5 = RP.Rectangle(0, 0, 200, 100)
        rect6 = RP.Rectangle(25, 40, 150, 50)

        self.assertTrue(RP.is_contained(rect5, rect6))

    # tests when rectangle contains itself
    def test_rect_contained_case2(self):
        rect6 = RP.Rectangle(25, 40, 150, 50)

        # case 3: rect6 contains itself
        self.assertTrue(RP.is_contained(rect6, rect6))

    # tests when smaller rect (rect7) is adjacent to standard_rect vertically
    def test_rect_adjacent_case1(self):
        rect7 = RP.Rectangle(50, 25, 50, 25)

        self.assertTrue(RP.is_adjacent(rect7, self.standard_rect))

    # tests when standard_rect is adjacent to rect8 with the same side length vertically
    def test_rect_adjacent_case2(self):
        rect8 = RP.Rectangle(50, 0, 50, 50)

        self.assertTrue(RP.is_adjacent(self.standard_rect, rect8))

    # tests when rect10 is adjacent to rect9 with the same side length horizontally
    def test_rect_adjacent_case3(self):
        rect9 = RP.Rectangle(0, 0, 100, 25)
        rect10 = RP.Rectangle(0, 25, 100, 25)

        self.assertTrue(RP.is_adjacent(rect10, rect9))

    # tests when smaller rect (rect11) is adjacent to rect9 horizontally
    def test_rect_adjacent_case4(self):
        rect11 = RP.Rectangle(0, 25, 50, 25)
        rect9 = RP.Rectangle(0, 0, 100, 25)

        self.assertTrue(RP.is_adjacent(rect11, rect9))

    """Rectangles do not intersect, are not contained and are not adjacent to each other. These are all essentially 
    the same test cases but just have small variations in the event shared x or y coordinates somehow affect it """
    def test_is_related(self):
        rect12 = RP.Rectangle(50, 60, 50, 100)
        rect13 = RP.Rectangle(60, 50, 50, 100)
        rect14 = RP.Rectangle(300, 300, 10, 10)

        # case 1: rect12 shares a common first point x coordinate with standard_rect
        self.assertFalse(RP.is_related(rect12, self.standard_rect))

        # case 2: rect13 shares a common first point y coordinate with standard_rect
        self.assertFalse(RP.is_related(rect13, self.standard_rect))

        # case 3: rect14 has no relation to standard_rect
        self.assertFalse(RP.is_related(self.standard_rect, rect14))