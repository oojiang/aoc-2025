from read_input import read_input, Range

def total_fresh_size(ranges: list[Range]) -> int:
    ranges.sort()

    total = 0
    smallest_uncounted = 0 # All ids are nonnegative.
    for begin, end in ranges:
        true_begin = max(begin, smallest_uncounted)
        total += max(0, end - true_begin + 1)
        smallest_uncounted = max(smallest_uncounted, end + 1)

    return total

test_ranges, _ = read_input('input1')
test_size = total_fresh_size(test_ranges)
assert test_size == 14, test_size

ranges, _ = read_input()
print(total_fresh_size(ranges))
