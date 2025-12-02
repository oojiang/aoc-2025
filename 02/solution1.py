from read_input import read_input

ranges = read_input()

total = 0
for begin, end in ranges:
    for n in range(begin, end + 1):
        s = str(n)
        half = len(s) // 2
        if s[:half] == s[half:]:
            total += n
print(total)
