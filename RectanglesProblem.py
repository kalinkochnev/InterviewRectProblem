# imported for dealing with file input for the program
import os


class Rectangle:
    def __init__(self, x, y, length, height):
        self.top_left_pt = (x, y)
        self.top_right_pt = (x + length, y)
        self.bottom_right_pt = (x + length, y + height)
        self.bottom_left_pt = (x, y + height)
        self.rectx1, self.recty1 = self.top_left_pt
        self.rectx3, self.recty3 = self.bottom_right_pt
        self.contained_points = 0
        self.area = int(length) * int(height)

    @classmethod
    def from_dict(cls, dictionary):
        return Rectangle(dictionary['X1'], dictionary['Y1'], dictionary['LENGTH'], dictionary['HEIGHT'])

    @property
    def all_pts(self):
        points_dict = {
            'point1': self.top_left_pt,
            'point2': self.top_right_pt,
            'point3': self.bottom_right_pt,
            'point4': self.bottom_left_pt,
        }
        return points_dict

    def pt_in_rect(self, point):
        pointx, pointy = point
        if self.rectx1 < pointx < self.rectx3 and self.recty1 < pointy < self.recty3:
            return True
        return False

    # any point that is not within the area of the rectangle or the sides themselves
    def pt_outside_rect(self, point):
        pointx, pointy = point
        if (pointx < self.rectx1 or pointx > self.rectx3) or (pointy < self.recty1 or pointy > self.recty3):
            return True
        return False

    def pt_on_side(self, point):
        pointx, pointy = point
        # checks if on top or bottom side
        if (self.rectx1 <= pointx <= self.rectx3) and (pointy == self.recty1 or pointy == self.recty3):
            return True
        # checks if on left or right side
        elif (self.recty1 <= pointy <= self.recty3) and (pointx == self.rectx1 or pointx == self.rectx3):
            return True

    # checks if point is between x or y boundary of the squares points
    def is_pt_between_bound(self, axis, point):
        pointx, pointy = point
        if axis == 'x':
            if self.rectx1 < pointx < self.rectx3:
                return True
        elif axis == 'y':
            if self.recty1 < pointy < self.recty3:
                return True

        return False


def num_points_in_boundary(RectA, RectB):
    recta_points = RectA.all_pts
    rectb_points = RectB.all_pts
    recta_pts_inbound = 0
    rectb_pts_inbound = 0

    # iterate through rect points and counts the number that are in the boundary for each rect
    # TODO add documentation because this is confusing for what it does
    for point in recta_points.values():
        if RectB.is_pt_between_bound('x', point) or RectB.is_pt_between_bound('y', point):
            recta_pts_inbound += 1
    for point in rectb_points.values():
        if RectA.is_pt_between_bound('x', point) or RectA.is_pt_between_bound('y', point):
            rectb_pts_inbound += 1

    # returns number contained based on order of the rects in the parameters
    return_val = recta_pts_inbound, rectb_pts_inbound
    return recta_pts_inbound, rectb_pts_inbound


def num_contained_points(RectA, RectB):
    recta_points = RectA.all_pts
    rectb_points = RectB.all_pts
    recta_pts_contained = 0
    rectb_pts_contained = 0

    # iterate through rect points and count number that are contained for each rect
    for point in recta_points.values():
        if RectB.pt_in_rect(point):
            recta_pts_contained += 1
    for point in rectb_points.values():
        if RectA.pt_in_rect(point):
            rectb_pts_contained += 1

    # returns number contained based on order of the rects in the parameters
    return recta_pts_contained, rectb_pts_contained


def num_pts_on_sides(RectA, RectB):
    # iterate through rect points and count number that are on the sides of each rect
    recta_points = RectA.all_pts
    rectb_points = RectB.all_pts
    recta_pts_on_side = 0
    rectb_pts_on_side = 0

    # iterate through rect points and count number that are on the sides of each rect
    for point in recta_points.values():
        if RectB.pt_on_side(point):
            recta_pts_on_side += 1
    for point in rectb_points.values():
        if RectA.pt_on_side(point):
            rectb_pts_on_side += 1

    # returns number points on sides based on order of the rects in the parameters
    return recta_pts_on_side, rectb_pts_on_side


def num_pts_outside(RectA, RectB):
    recta_points = RectA.all_pts
    rectb_points = RectB.all_pts
    recta_pts_outside = 0
    rectb_pts_outside = 0

    # iterate through rect points and count number that are on the sides of each rect
    for point in recta_points.values():
        if RectB.pt_outside_rect(point):
            recta_pts_outside += 1
    for point in rectb_points.values():
        if RectA.pt_outside_rect(point):
            rectb_pts_outside += 1

    # returns number points outside based on order of the rects in the parameters
    return recta_pts_outside, rectb_pts_outside


def is_contained(RectA, RectB):
    contained_pts_val = num_contained_points(RectA, RectB)

    # If a rect has 4 pts and the other has 0, they're contained
    if contained_pts_val == (4, 0) or contained_pts_val == (0, 4):
        return True
    # If a rect has the same points, they contain one another
    elif RectA.all_pts == RectB.all_pts:
        return True
    return False


"""
def get_side_position(Rect, name):
    rect_pts = Rect.all_pts

    # rect[point_name][number], number is a position value in the tuple which is either the x or y value
    if name == 'top':
        y_value = rect_pts['point1'][1]
        return {'y': y_value}
    elif name == 'bottom':
        y_value = rect_pts['point3'][1]
        return {'y': y_value}
    elif name == 'right':
        x_value = rect_pts['point1'][0]
        return {'x': x_value}
    elif name == 'left':
        x_value = rect_pts['point3'][0]
        return {'x': x_value}

def get_intersecting_pts(RectA, RectB, type_intersect):
    RectA_x1, RectA_y1 = RectA.all_pts['point1']
    RectA_x3, RectA_y3 = RectA.all_pts['point3']
    RectB_x1, RectB_y1 = RectB.all_pts['point1']
    RectB_x3, RectB_y3 = RectB.all_pts['point3']
    intersecting_pts = []

    if type_intersect == (4, 4):
        intersecting_pts = [
            (RectA_x1, RectB_y1),
            (RectA_x3, RectB_y1),
            (RectA_x1, RectB_y3),
            (RectA_x3, RectB_y3),
        ]

    elif type_intersect == (1, 1):
        if RectA_y3 > RectB_y3:
            intersecting_pts = [
                (RectB_x3, RectA_y1),
                (RectA_x1, RectB_y3)
            ]
        elif RectB_y3 > RectA_y3:
            intersecting_pts = [
                (RectB_x1, RectA_y3),
                (RectA_x3, RectB_y1)
            ]
    elif type_intersect == (0, 2) or type_intersect == (2, 0):
        # Assigning y coordinate of intersection depending on which rect has the greater y value
        if RectB_y3 < RectA_y3:
            intersection_y_value = RectA_y1
            intersecting_pts = [
                (RectB_x1, intersection_y_value),
                (RectB_x3, intersection_y_value),
            ]
        else:
            intersection_y_value = RectA_y3
            intersecting_pts = [
                (RectA_x1, intersection_y_value),
                (RectA_x3, intersection_y_value),
            ]
    return intersecting_pts
"""


def is_intersecting(RectA, RectB):
    contained_pts_val = num_contained_points(RectA, RectB)
    points_in_bound_val = num_points_in_boundary(RectA, RectB)

    # if one point is contained in both squares, they're intersecting
    if contained_pts_val == (1, 1):
        return True
    # if two points are contained in one square but the other has 0, they're intersecting
    elif contained_pts_val == (0, 2) or contained_pts_val == (2, 0):
        return True
    # case where there are no contained points but the rectangles intersect
    elif points_in_bound_val == (4, 4):
        return True
    else:
        return None


def is_adjacent(RectA, RectB):
    points_on_sides = num_pts_on_sides(RectA, RectB)

    # if a rect has 2 points that have a common side and the other rect has 1, the're adjacent
    if points_on_sides == (1, 2) or points_on_sides == (2, 1):
        return True
    # if each rect has 2 points in common they are adjacent
    if points_on_sides == (2, 2):
        return True
    # if each rect has 1 point with a common side they are adjacent
    if points_on_sides == (1, 1):
        return True
    return False


def is_related(RectA, RectB):
    if num_pts_outside(RectA, RectB) == (4, 4):
        return False
    else:
        return True


def input_folder_reading():
    output_array = [{}, {}]
    if file.endswith('.txt'):

        with open(os.path.join(input_dir, file), 'r') as f:
            file_input = f.readlines()

            current_rect = 0
            for line in file_input:

                if "X1" in line and current_rect < 2:
                    temp_array = line.strip(" \n").split(",")
                    for item in temp_array:
                        temp_item = item.strip(' ').split('=')

                        output_array[current_rect][temp_item[0]] = temp_item[1]
                    current_rect += 1
    return output_array


# TODO create messages that classify the rectangles
def analyze_rects(RectA, RectB):
    if is_contained(RectA, RectB):
        return "A rectangle is contained"
    elif is_intersecting(RectA, RectB):
        return "A rectangle is intersecting"
    elif is_adjacent(RectA, RectB):
        return "The rectangles are adjacent"
    elif is_related(RectA, RectB) == False:
        return "The rectangles are not adjacent, intersecting or contained"


if __name__ == '__main__':
    input_dir = os.path.join(os.getcwd(), 'Input Folder')

    for file in os.listdir(input_dir):
        output_dict = input_folder_reading()
        # and file != "Example Input.txt"
        RectA = Rectangle.from_dict(output_dict[0])
        RectB = Rectangle.from_dict(output_dict[1])

        message = analyze_rects(RectA, RectB)
        print(f'Filename: {file} -- {message}')
