from read_input import read_input

def count_splits(grid: list[list[str]]) -> int:
    beams = [c == 'S' for c in grid[0]]

    splits = 0
    for row in grid[1:]:
        new_beams = [c == 'S' for c in row]
        for i, b in enumerate(beams):
            if not b:
                continue
            if row[i] == '^':
                splits += 1
                if i - 1 in range(len(new_beams)):
                    new_beams[i - 1] = True
                if i + 1 in range(len(new_beams)):
                    new_beams[i + 1] = True
            else:
                new_beams[i] = True
        beams = new_beams

    return splits

test_splits = count_splits(read_input("input1"))
assert test_splits == 21, test_splits

print(count_splits(read_input()))

