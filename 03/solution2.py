from read_input import read_input

banks = read_input()

'''
Returns the max joltage of a bank (a single row of batteries) if
we are allowed to turn on `num` batteries.
'''
def max_joltage(bank: list[int], num) -> int:
    battery_idxs = list(range(len(bank) - num, len(bank)))

    for i, right in enumerate(battery_idxs):
        left = battery_idxs[i - 1] if i - 1 in range(num) else -1

        curr = 0
        for idx in range(right, left, -1):
            if bank[idx] >= curr:
                curr = bank[idx]
                battery_idxs[i] = idx

    result = 0
    for idx in battery_idxs:
        result *= 10
        result += bank[idx]
    return result

assert max_joltage([int(c) for c in '987654321111111'], 12) == 987654321111, max_joltage([int(c) for c in '987654321111111'], 12)
assert max_joltage([int(c) for c in '811111111111119'], 12) == 811111111119
assert max_joltage([int(c) for c in '234234234234278'], 12) == 434234234278
assert max_joltage([int(c) for c in '818181911112111'], 12) == 888911112111

total = 0
for bank in banks:
    total += max_joltage(bank, 12)
print(total)
