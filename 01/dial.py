from enum import Enum

class Direction(str, Enum):
    R = "R"
    L = "L"

type Distance = int
type Rotation = tuple[Direction, Distance]

DIAL_SIZE = 100

'''
Rotates the dial
@param start - the number the dial is at currently
@param rotation - the Rotation instruction, e.g. (Direction.R, 67)
@return - the number the dial ends up at
'''
def rotate(start, rotation):
    direction, distance = rotation

    if direction == Direction.R:
        return (start + distance) % DIAL_SIZE
    else:
        return (start - distance) % DIAL_SIZE

'''
Counts the number of times the dial points at zero if it were to be rotated
    using `start` and `rotation`. Only counts when the dial changes to point
    at zero--e.g. if start is already zero, that initial zero isn't counted.

@param start - the number the dial is at currently
@param rotation - the Rotation instruction, e.g. (Direction.R, 67)
@return - the number the dial points at zero through the rotation.
'''
def num_times_at_zero(start, rotation):
    direction, distance = rotation

    if direction == Direction.R:
        return (start + distance) // DIAL_SIZE
    else:
        return ((DIAL_SIZE - start) % 100 + distance) // DIAL_SIZE
