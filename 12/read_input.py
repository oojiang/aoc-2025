import re

type PresentShape = list[list[bool]]
type Dimensions = tuple[int, int]
type Count = int
type Tree = tuple[Dimensions, list[Count]]

def read_input(filename = "input") -> tuple[list[Tree], list[PresentShape]]:
    shapes = []
    trees = []
    with open(filename, 'r') as file:
        for i in range(6):
            file.readline() # skip the index
            present = [
                [c == '#' for c in file.readline().strip()],
                [c == '#' for c in file.readline().strip()],
                [c == '#' for c in file.readline().strip()],
            ]
            shapes.append(present)
            file.readline() # skip the newline

        for line in file:
            trees.append(tree(line))
    return (shapes, trees)

def tree(s) -> Tree:
    data = s.split()
    dim = dimensions(data[0])
    counts = [int(n) for n in data[1:]]
    return (dim, counts)

def dimensions(s) -> Dimensions:
    pattern = r"(\d+)x(\d+):"
    return tuple(int(n) for n in re.match(pattern, s).groups())
