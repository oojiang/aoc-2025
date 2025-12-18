from linalg import gaussian_elimination, solve

def test_single_equation():
    A = [[2.0]]
    b = [4.0]

    A, b, is_free = gaussian_elimination(A, b)
    x = [0.0]

    x = solve(A, x, b, is_free)

    assert x == [2.0], x

def test_2x2_unique_solution():
    A = [
        [1.0, 1.0],
        [2.0, -1.0],
    ]
    b = [3.0, 0.0]

    A, b, is_free = gaussian_elimination(A, b)
    x = [0.0, 0.0]

    solve(A, x, b, is_free)

    assert is_free == [False, False], is_free
    assert x == [1.0, 2.0], x

def test_free_variable():
    A = [[1.0, 1.0]]
    b = [2.0]

    A, b, is_free = gaussian_elimination(A, b)

    # Choose y = 1
    x = [0.0, 1.0]

    solve(A, x, b, is_free)

    assert is_free == [False, True], is_free
    assert x == [1.0, 1.0], x   # x = 2 - y

test_single_equation()
test_2x2_unique_solution()
test_free_variable()
