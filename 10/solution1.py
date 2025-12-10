from read_input import Indicators, Button, Machine, read_input
from collections import deque

def fewest_presses(machine: Machine) -> int:
    goal, buttons = machine

    start = tuple(False for _ in goal)
    queue = deque([(start, 0)]) # each item is (indicators, count)
    seen = set()

    while queue:
        curr, count = queue.popleft()
        if curr in seen:
            continue
        seen.add(curr)

        if curr == goal:
            return count

        for button in buttons:
            queue.append((press(curr, button), count + 1))

    return -1

def press(ind: Indicators, button: Button) -> Indicators:
    return tuple(not ind[i] if i in button else ind[i]
        for i in range(len(ind)))

if __name__ == '__main__':
    test_count = 0
    for test_machine in read_input("input1"):
        test_count += fewest_presses(test_machine)
    assert test_count == 7, test_count

    count = 0
    for machine in read_input():
        count += fewest_presses(machine)
    print(count)
