import turtle
import Point1
import Circle
import polygon


def draw_rect(t, rect):
    """Draw a rectangle using using Turtle

    :param t: Turtle object
    :param rect: Rectangle object
    :return:
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.pd()
    t.setheading(0)
    for i in range(2):
        t.fd(rect.width)
        t.lt(90)
        t.fd(rect.height)
        t.lt(90)


def draw_circle(t, circle):
    """Draw a circle using using Turtle

    :param t: Turtle object
    :param circle: Circle object
    :return:
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.pd()
    polygon.circle(t, circle.radius)


if __name__ == "__main__":
    bob = turtle.Turtle()

    box = Point1.Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point1.Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle.Circle()
    circle.center = Point1.Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75

    draw_rect(bob, box)
    draw_circle(bob, circle)
    print(Circle.rect_in_circle(circle, box))
    print(Circle.rect_circle_overlap(circle, box))

    turtle.mainloop()
