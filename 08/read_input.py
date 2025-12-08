type Coordinate = tuple[int, int, int]

def read_input(filename = "input") -> list[Coordinate]:
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            coor = tuple(int(s) for s in line.split(','))
            coordinates.append(coor)
    return coordinates
