from read_input import read_input

'''
Mutates grid so that the accessable rolls are removed, and
returns the number of removed rolls.
'''
def remove_accessable_rolls(grid: list[list[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    def has_paper(r, c):
        if r not in range(ROWS) or c not in range(COLS):
            return False
        return grid[r][c] != '.'

    def is_accessible(r, c):
        if grid[r][c] == '.':
            return False
        total = 0
        count = 0
        for r_ in range(r - 1, r + 2):
            for c_ in range(c - 1, c + 2):
                count += 1
                if (r_, c_) != (r, c):
                    total += has_paper(r_, c_)
        return total < 4

    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if is_accessible(r, c):
                grid[r][c] = '.'
                count += 1

    return count

'''
Continually mutates grid until ALL accessable rolls are removed,
and returns the number of removed rolls.
'''
def count_removable_rolls(grid: list[list[str]]) -> int:
    count = 0
    while removed := remove_accessable_rolls(grid):
        count += removed

    return count

test_count = count_removable_rolls(read_input("input1"))
assert test_count == 43, test_count

grid = read_input()
print(count_removable_rolls(grid))
