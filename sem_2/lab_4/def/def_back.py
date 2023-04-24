from math import sqrt

POINT_SIZE = 3
eps = 1e-10

COLORS = {
    "POINT": "#212121",
    "VERTECS": "#700b0b",
    "LINE": "#191919"
}


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


def distance(point1: Point, point2: Point) -> float:
    return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def is_in(point: Point, A: Point, B: Point, C: Point, AB: float, AC: float, BC: float) -> bool:
    p_ABC = (AB + BC + AC) / 2  # полупериметр ABC
    S_ABC = sqrt(p_ABC * (p_ABC - AB) * (p_ABC - BC) * (p_ABC - AC))

    BO = distance(point, B)
    CO = distance(point, C)
    AO = distance(point, A)

    # ищем полупериметры ABO,ACO,BOC
    p_ABO = (AB + BO + AO) / 2
    p_ACO = (AC + CO + AO) / 2
    p_BOC = (CO + BO + BC) / 2

    # ищем площади ABO,ACO,BOC
    S_ABO = sqrt(p_ABO * (p_ABO - AB) * (p_ABO - BO) * (p_ABO - AO))
    S_ACO = sqrt(p_ACO * (p_ACO - AC) * (p_ACO - CO) * (p_ACO - AO))
    S_BOC = sqrt(p_BOC * (p_BOC - CO) * (p_BOC - BO) * (p_BOC - BC))

    # Доказываем нахождение точки O относительно треугольника ABC
    if (S_ABO + S_ACO + S_BOC) - S_ABC < eps:
        return True
    return False


def calculate(canvas):
    Point.reset(canvas)
    n = len(Point.points)
    verhines = []
    points_in = -1
    for i in range(n):
        for j in range(n):
            if i == j: continue
            ab = distance(Point.points[i], Point.points[j])
            for k in range(n):
                point_count = 0
                if k == i or k == j: continue
                ac = distance(Point.points[i], Point.points[k])
                bc = distance(Point.points[j], Point.points[k])
                for in_point in range(n):
                    if in_point == i or in_point == j or in_point == k: continue
                    if is_in(Point.points[in_point], Point.points[i], Point.points[j], Point.points[k], ab, ac, bc):
                        point_count += 1
                if point_count > points_in:
                    verhines = [Point.points[i], Point.points[j], Point.points[k]]
                    points_in = point_count
    return verhines
