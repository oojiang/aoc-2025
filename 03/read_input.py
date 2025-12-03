def read_input(filename = "input") -> list[list[int]]:
    banks = []
    with open(filename, 'r') as file:
        for line in file:
            batteries = [int(c) for c in line.strip()]
            banks.append(batteries)
    return banks
