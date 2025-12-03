from read_input import read_input

banks = read_input()

'''
Returns the max joltage of a bank (a single row of batteries).
'''
def max_joltage(bank: list[int]) -> int:
    max_left = 0
    result = 0
    for jolt in bank:
        result = max(result, 10 * max_left + jolt)
        max_left = max(max_left, jolt)
    return result

assert max_joltage([int(c) for c in '987654321111111']) == 98
assert max_joltage([int(c) for c in '811111111111119']) == 89
assert max_joltage([int(c) for c in '234234234234278']) == 78
assert max_joltage([int(c) for c in '818181911112111']) == 92

total = 0
for bank in banks:
    total += max_joltage(bank)
print(total)
