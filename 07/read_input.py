def read_input(filename = "input") -> list[list[str]]:
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid
