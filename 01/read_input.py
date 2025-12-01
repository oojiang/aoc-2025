from dial import Direction, Rotation

'''
@param filename - the file to read from.
@return a list of rotation tuples, where each tuple looks something like
        ('R', 67) or ('L', 42).
'''
def read_input(filename = "input") -> list[Rotation]:
    rotations = []
    with open(filename, 'r') as file:
        for line in file:
            direction = Direction(line[0])
            distance = int(line[1:].strip())
            rotations.append((direction, distance))

    return rotations
