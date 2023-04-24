from math import sqrt

POINT_SIZE = 3

COLORS = {
    "POINT": "#ffffff",
    "CENTER": "#700b0b",
    "CIRCLE": "#14700b"
}


# Класс точки
class Point:
    points = []

    def __init__(self, x: int, y: int, canvas):
        self.x = x
        self.y = y

        self.id = Point.draw(self.x, self.y, canvas, COLORS["POINT"])
        Point.points.append(self)

    # Отрисовка точки.
    @staticmethod
    def draw(x: int, y: int, canvas, color: str = COLORS["POINT"]):
        return canvas.create_oval(x - POINT_SIZE, y - POINT_SIZE,
                                  x + POINT_SIZE, y + POINT_SIZE,
                                  fill=color)

    # Окрашивание всех точек в белый.
    @staticmethod
    def reset(canvas):
        for point in Point.points:
            Point.draw(point.x, point.y, canvas, COLORS["POINT"])


class Circle:
    exist = 0

    def __init__(self, c: Point, r: float):
        self.center = c
        self.radius = r

    # Отрисовка точки.
    @staticmethod
    def draw(center: Point, radius: float, canvas, color: str = COLORS["CIRCLE"]):
        Circle.reset(canvas)
        Circle.exist = canvas.create_oval(center.x - radius, center.y - radius,
                                          center.x + radius, center.y + radius,
                                          outline=color, width=1)

    @staticmethod
    def reset(canvas):
        if Circle.exist != 0:
            canvas.delete(Circle.exist)


def distance(point1: Point, point2: Point) -> float:
    return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def calculate(canvas):
    Point.reset(canvas)
    n = len(Point.points)

    radius = float("+inf")
    point = None
    for i in range(n):
        maxx = -1
        for j in range(n):
            if i == j: continue
            rad = distance(Point.points[i], Point.points[j])
            if rad > maxx:
                maxx = rad
        if maxx < radius:
            point = Point.points[i]
            radius = maxx

    return point, radius
