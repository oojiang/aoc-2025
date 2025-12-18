from linalg import Vector, Matrix, solve, gaussian_elimination
from read_input import Machine, read_input
import time

'''
Day 10 part 2, except redone without any libraries like numpy or scipy.
'''

def fewest_presses(machine: Machine, debug=False) -> int:
    _, buttons, goal = machine

    maximums = [
        min(goal[i] for i in button)
        for button in buttons
    ]

    A = [
        [1 if i in button else 0 for button in buttons]
        for i in range(len(goal))
    ]

    A, b, is_free = gaussian_elimination(A, goal)
    if debug:
        print(f"# of free variables: {sum(is_free)}")

    for i in range(len(is_free)):
        if not is_free[i]:
            maximums[i] = 0

    min_presses =  999999
    if debug:
        print(f"# of cases: {len(list(iterate(maximums)))}")
    for x in iterate(maximums):
        x_ = solve(A, x, b, is_free)


        if x_int := is_valid(A, x_, b):
            min_presses = min(min_presses, sum(x_int))
    return min_presses

def iterate(maximums):
    n = len(maximums)
    current = [0] * n

    while True:
        yield current.copy()

        for i in range(n):
            current[i] += 1
            if current[i] <= maximums[i]:
                break
            current[i] = 0
        else:
            return

def is_valid(A: Matrix, x: Vector, b: Vector, tolerance = 1e-3):
    ROWS, COLS = len(A), len(A[0])

    x_int = [round(n) for n in x]

    if any(n < 0 for n in x_int):
        return False

    b_ = [
        sum(A[r][c] * x_int[c] for c in range(COLS))
        for r in range(ROWS)
    ]

    if any(abs(b[i] - b_[i]) > tolerance for i in range(ROWS)):
        return False
    return x_int

if __name__ == '__main__':
    test_count = 0
    for test_machine in read_input("input1"):
        test_count += fewest_presses(test_machine)
    assert test_count == 33, test_count

    machines = read_input()
    count = 0
    n = 0
    total = len(machines)
    start = time.time()
    print(f"{n}/{total}, time elapsed: {time.time() - start}s")
    for machine in machines:
        n += 1
        count += fewest_presses(machine, debug=True)
        print(f"{n}/{total}, time elapsed: {time.time() - start}s")
    print(count)
