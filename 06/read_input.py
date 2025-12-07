
def read_input(filename = "input") -> tuple[list[list[int]], list[str]]:
    rows = []
    with open(filename, 'r') as file:
        for line in file:
            rows.append(line.strip().split())

    operations = rows.pop()

    for i, row in enumerate(rows):
        rows[i] = [int(s) for s in row]

    return rows, operations
