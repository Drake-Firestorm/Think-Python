import math
import copy


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x=0, y=0):
        """
        Initialize a Point object.

        :param x: int
        :param y: int
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the point.

        :return: string
        """
        return "(%g, %g)" % (self.x, self.y)

    def __add__(self, other):
        """
        Returns the sum of two Point objects or a Point object and a tuple.

        :param other: Point object or tuple(x, y)
        :return: Point object
        """
        p = Point()
        if isinstance(other, Point):
            p.x = self.x + other.x
            p.y = self.y + other.y
        else:
            p.x = self.x + other[0]
            p.y = self.y + other[1]
        return p

    def __radd__(self, other):
        return self.__add__(other)


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """


def print_point(p):
    """Print point coordinates.

    :param p: Point object
    :return:
    """
    print("(%g, %g)" % (p.x, p.y))


def distance_between_points(p1, p2):
    """Returns distance between 2 points

    :param p1: Point object
    :param p2: Point object
    :return:
    """
    dist_sq_x = (p1.x - p2.x)**2
    dist_sq_y = (p1.y - p2.y)**2
    return math.sqrt(dist_sq_x + dist_sq_y)


def move_rectangle(rect, dx, dy):
    """ Moves the lower left corner of the rectangle by given x and y distance.

    :param rect: Rectangle object
    :param dx: distance to move x coordinate (can be negative)
    :param dy:distance to move y coordinate (can be negative)
    :return:
    """
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect


if __name__ == "__main__":
    point1 = Point()
    point2 = Point()
    point1.x = 3.0
    point1.y = 4.0
    point2.x = 0.0
    point2.y = 0.0
    # print(distance_between_points(point1, point2))
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    print_point(box.corner)

    p = Point(2.5)
    p2 = Point(1, 2)
    print(p + p2)
    p2 = (1, 3)
    print(p + p2)

    p = Point(3, 4)
    print(vars(p))
