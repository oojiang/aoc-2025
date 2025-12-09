from read_input import Coordinate, read_input

'''
Returns the area of the largest rectangle "defined" by any two points in
coordinates, where two points "define" the rectangle whose diagonal connects
the two points, and the rectangle must be parallel to the axes.
'''
def largest_rectangle(coordinates: list[Coordinate]) -> int:
    max_area = 0
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            max_area = max(max_area, area(coordinates[i], coordinates[j]))
    return max_area


def area(a: Coordinate, b: Coordinate) -> int:
    ax, ay = a
    bx, by = b

    xside = abs(ax - bx) + 1
    yside = abs(ay - by) + 1

    return xside * yside


test_area = largest_rectangle(read_input("input1"))
assert test_area == 50, test_area

print(largest_rectangle(read_input()))
