from read_input import Point, read_input
from solution1 import area

type Segment = tuple[Point, Point]

'''
Returns the area of the largest rectangle which fits in the boundary.
Also returns the two points that define the largest rectangle.
'''
def largest_green_rectangle(points: list[Point]) -> tuple[int, tuple[Point, Point]]:
    boundary: list[Segment] = []
    for i, p2 in enumerate(points):
        p1 = points[i - 1]
        boundary.append((p1, p2))

    max_area = 0
    best = ((-1, -1), (-1, -1))
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            rect = rectangle_segments(points[i], points[j])
            if not any_intersect(rect, boundary):
                curr_area = area(points[i], points[j])
                if curr_area > max_area:
                    max_area = curr_area
                    best = (points[i], points[j])
        print(f"{i}/{len(points)}")
    return max_area, best

'''
Returns the four segments representing the sides of the rectangle defined
by point1 and point2.

Slightly nudges the rectangle inwards.
'''
def rectangle_segments(point1: Point, point2: Point) -> list[Segment]:
    x1, y1 = point1
    x2, y2 = point2

    minX = min(x1, x2) + 0.01
    maxX = max(x1, x2) - 0.01
    minY = min(y1, y2) + 0.01
    maxY = max(y1, y2) - 0.01

    segments = []
    for x in (minX, maxX):
        segments.append(((x, minY), (x, maxY)))
    for y in (minY, maxY):
        segments.append(((minX, y), (maxX, y)))
    return segments

'''
Checks if any segments in group1 intersect any segments in group2.
'''
def any_intersect(group1: list[Segment], group2: list[Segment]) -> bool:
    for seg1 in group1:
        for seg2 in group2:
            if intersects(seg1, seg2):
                return True
    return False

'''
Checks if two segments intersect.
'''
def intersects(segment1: Segment, segment2: Segment) -> int:
    (x1a, y1a), (x1b, y1b) = segment1
    (x2a, y2a), (x2b, y2b) = segment2
    x1min, x1max = sorted([x1a, x1b])
    y1min, y1max = sorted([y1a, y1b])
    x2min, x2max = sorted([x2a, x2b])
    y2min, y2max = sorted([y2a, y2b])

    # If two segments intersect, then the beginning of the intersection
    # will be the max of their mins. The end of the intersection will be
    # the min of their maxes. Thus, if the beginning is after the end, then
    # they do not intersect.
    return (max(x1min, x2min) <= min(x1max, x2max) and
            max(y1min, y2min) <= min(y1max, y2max))


if __name__ == '__main__':
    test_area, test_best = largest_green_rectangle(read_input("input1"))
    assert test_area == 24, (test_area, test_best)

    print(largest_green_rectangle(read_input()))
