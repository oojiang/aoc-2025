from dial import Rotation, rotate, num_times_at_zero
import read_input

'''
Assuming the dial starts at 50, counts the number of times the dial
points at zero at any pont by following `rotations`.
@param rotations - A list of rotations, such as ('R', 67)
@return - The number of times the dial points at 0
'''
def main(rotations: list[Rotation]) -> int:
    curr = 50
    count = 0
    for rotation in rotations:
        count += num_times_at_zero(curr, rotation)
        curr = rotate(curr, rotation)
    return count

print(main(read_input.read_input()))
