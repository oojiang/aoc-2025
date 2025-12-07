def read_input(filename = "input") -> tuple[list[list[int]], list[str]]:
    rows = []
    with open(filename, 'r') as file:
        for line in file:
            rows.append(line.strip().split())

    operations = rows.pop()

    for i, row in enumerate(rows):
        rows[i] = [int(s) for s in row]

    return rows, operations

def read_input2(filename = "input") -> tuple[list[list[int]], list[str]]:
    operands = []
    operations = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        op_line = lines.pop()

        cursor = -1
        while True:
            cursor += 1
            if op_line[cursor] == '\n':
                break
            elif op_line[cursor] in '+*':
                operands.append([])
                operations.append(op_line[cursor])

            curr = 0
            for line in lines:
                if line[cursor] == ' ':
                    continue
                curr *= 10
                curr += int(line[cursor])
            if curr != 0:
                operands[-1].append(curr)

    return operands, operations
