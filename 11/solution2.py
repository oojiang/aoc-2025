from read_input import read_input, Devices

'''
Counts the paths from start to end that must visit the devices in visit.
'''
def count_paths(devices: Devices, start: str, end: str, visit: list[str]):
    memo = {}

    def dfs(curr: str, todo: tuple[str, ...]):
        if curr == end:
            return 1 if len(todo) == 0 else 0
        if (curr, todo) in memo:
            return memo[(curr, todo)]

        if curr in visit:
            new_todo = tuple(device for device in todo if device != curr)
        else:
            new_todo = tuple(todo)

        count = 0
        for device in devices[curr]:
            count += dfs(device, new_todo)

        memo[(curr, todo)] = count
        return memo[(curr, todo)]

    return dfs(start, tuple(visit))

test_count = count_paths(read_input("input2"), 'svr', 'out', ['dac', 'fft'])
assert test_count == 2, test_count

print(count_paths(read_input(), 'svr', 'out', ['dac', 'fft']))
