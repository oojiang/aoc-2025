import matplotlib.pyplot as plt
from read_input import read_input, Point

def visualize(p1: Point, p2: Point, filename = "input"):
    points = read_input(filename)
    points.append(points[0])
    x, y = zip(*points)
    plt.plot(x, y, marker='.')

    rect = rectangle_corners(p1, p2)
    rx, ry = zip(*rect)
    plt.plot(rx, ry, marker='.')

    plt.show()

def rectangle_corners(p1: Point, p2: Point):
    x1, y1 = p1
    x2, y2 = p2

    minX = min(x1, x2)
    maxX = max(x1, x2)
    minY = min(y1, y2)
    maxY = max(y1, y2)

    return [
        (minX, minY), (minX, maxY), (maxX, maxY), (maxX, minY), (minX, minY)
    ]
