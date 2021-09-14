import Point1
import copy


class Circle:
    """Represents a Circle.

    attributes: center, radius"""


def point_in_circle(circle, point):
    """Checks if the point is in circle.

    :param circle: Circle object
    :param point: Point object
    :return:
    """
    dist_from_center = Point1.distance_between_points(circle.center, point)
    return dist_from_center <= circle.radius


def rect_in_circle(circle, rect):
    """Checks if the rectangle is fully inside the circle.

    :param circle: Circle object
    :param rect: Rectangle object
    :return:
    """
    new_rect = copy.deepcopy(rect)

    if not point_in_circle(circle, new_rect.corner):
        return False

    new_rect.corner.x += new_rect.width
    if not point_in_circle(circle, new_rect.corner):
        return False

    new_rect.corner.y += new_rect.height
    if not point_in_circle(circle, new_rect.corner):
        return False

    new_rect.corner.x -= new_rect.width
    if not point_in_circle(circle, new_rect.corner):
        return False

    return True


def rect_circle_overlap(circle, rect):
    """Checks if any corner of the rectangle is in the circle.

    :param circle: Circle object
    :param rect: Rectangle object
    :return:
    """
    new_rect = copy.deepcopy(rect)

    if point_in_circle(circle, new_rect.corner):
        return True

    new_rect.corner.x += new_rect.width
    if point_in_circle(circle, new_rect.corner):
        return True

    new_rect.corner.y += new_rect.height
    if point_in_circle(circle, new_rect.corner):
        return True

    new_rect.corner.x -= new_rect.width
    if not point_in_circle(circle, new_rect.corner):
        return True

    return False


if __name__ == "__main__":
    circle = Circle()
    circle.center = Point1.Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75
    # Point1.print_point(circle.center)         # 1.

    point1 = Point1.Point()
    point1.x = 225.0
    point1.y = 100.0
    # print(point_in_circle(circle, point1))    # 2.

    box = Point1.Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point1.Point()
    box.corner.x = 50.0
    box.corner.y = 50.0
    print(rect_in_circle(circle, box))        # 3.
    print(rect_circle_overlap(circle, box))   # 4.
