from read_input import read_input, Devices

'''
Counts paths from start to 'out', assuming no loops.
'''
def count_paths(start: str, devices: Devices) -> int:
    if start == 'out':
        return 1

    return sum(count_paths(device, devices) for device in devices[start])

test_count = count_paths('you', read_input('input1'))
assert test_count == 5, test_count

print(count_paths('you', read_input()))
