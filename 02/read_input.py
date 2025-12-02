def read_input(filename = "input") -> list[tuple[int, int]]:
    ranges = []
    with open(filename, 'r') as file:
        line = file.read()
        for s in line.split(','):
            str_range = s.split('-')
            begin = int(str_range[0])
            end = int(str_range[1])
            ranges.append((begin, end))
    return ranges
