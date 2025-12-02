from read_input import read_input

ranges = read_input()

def is_valid(n):
    s = str(n)
    for length in range(1, len(s) // 2 + 1):
        pattern = s[:length]
        repeat = len(s) // length
        if length * repeat == len(s) and pattern * repeat == s:
            return True
    return False

total = 0
for begin, end in ranges:
    for n in range(begin, end + 1):
        if is_valid(n):
            total += n
print(total)
