type Point = tuple[float, float]

def read_input(filename = "input") -> list[Point]:
    points = []
    with open(filename, 'r') as file:
        for line in file:
            p = tuple(int(s) for s in line.split(','))
            points.append(p)
    return points
