from read_input import read_input2

def compute_grand_total2(operands: list[list[int]], operations: list[str]):
    IDENTITY = {
        '+': 0,
        '*': 1,
    }
    FUNC = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }

    total = 0
    for i, op in enumerate(operations):
        curr, func = IDENTITY[op], FUNC[op]
        for n in operands[i]:
            curr = func(curr, n)
        total += curr
    return total

rows, operations = read_input2()
print(compute_grand_total2(rows, operations))
