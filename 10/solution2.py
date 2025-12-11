from read_input import Machine, read_input
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def fewest_presses(machine: Machine) -> int:
    _, buttons, goal = machine

    A = np.array([
        [1 if i in button else 0 for button in buttons]
         for i in range(len(goal))
    ])
    b = np.array(goal)

    n = A.shape[1]
    c = np.ones(n)
    constraints = LinearConstraint(A, lb=b, ub=b)
    bounds = Bounds(lb = np.zeros(n), ub=np.full(n, np.inf))
    integrality = np.ones(n, dtype=int)

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    return res.fun

if __name__ == '__main__':
    test_count = 0
    for test_machine in read_input("input1"):
        test_count += fewest_presses(test_machine)
    assert test_count == 33, test_count

    count = 0
    for machine in read_input():
        count += fewest_presses(machine)
    print(count)
