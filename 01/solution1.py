from dial import Rotation, rotate
import read_input

'''
Assuming the dial starts at 50, counts the number of times the dial
ends up pointing at 0 by following `rotations`.
@param rotations - A list of rotations, such as ('R', 67)
@return - The number of times the dial ends pointing at 0
'''
def main(rotations: list[Rotation]) -> int:
    curr = 50
    count = 0
    for rotation in rotations:
        curr = rotate(curr, rotation)
        if curr == 0:
            count += 1
    return count

print(main(read_input.read_input()))
