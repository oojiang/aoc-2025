from read_input import read_input

'''
@param rows - 2D array of ints, representing operands
@param operations - the operations for each column
'''
def compute_grand_total(rows: list[list[int]], operations: list[str]):
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
        for row in rows:
            curr = func(curr, row[i])
        total += curr
    return total

rows, operations = read_input()
print(compute_grand_total(rows, operations))
