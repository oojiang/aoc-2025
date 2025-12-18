from copy import deepcopy

type Vector = list[float]
type Matrix = list[Vector]

'''
Given Ax = b, solve for x.
@param A - The matrix in Ax = b, in RREF.
@param x - The variable vector with all of the free entries already filled in.
@param b - The constant vector in Ax = b.
@param is_free - is_free[c] is True iff column c of A is a free column.

@return x - x, but with the pivot entries filled in.
'''
def solve(A: Matrix, x: Vector, b: Vector, is_free) -> Vector:
    ROWS, COLS = len(A), len(A[0])
    x = list(x)
    assert len(x) == len(is_free) == COLS
    assert len(b) == ROWS

    c = 0
    for r in range(ROWS):
        # Find the pivot column for this row.
        while c in range(COLS) and is_free[c]:
            c += 1
        if c not in range(COLS):
            continue

        # x[c] = b[r] - A[r][1] * x[1] - A[r][2] * x[2] - ...
        x[c] = b[r]
        for c_ in range(COLS):
            if c_ == c:
                continue
            x[c] -= A[r][c_] * x[c_]

        c += 1
    return x

'''
Simplifies A and b, and returns which columns of A are free.
@param A - The matrix in Ax = b.
@param b - The constant vector in Ax = b.

@return A_ - A copy of A, but in RREF.
@return b_ - A vector b_ such that A_x = b_ is equivalent to Ax = b.
@return is_free - is_free[c] is True iff column c of A is a free column.
'''
def gaussian_elimination(A: Matrix, b: Vector) -> tuple[Matrix, Vector, list[bool]]:
    assert len(A) == len(b)

    # Create augmented matrix A by concatenating b.
    A_ = deepcopy(A)
    for i in range(len(A_)):
        A_[i].append(b[i])

    # Do gaussian elimination
    A_, is_free = get_rref(A_)

    # Separate b out from the augmented matrix A_.
    b_ = []
    for i in range(len(A_)):
        b_.append(A_[i].pop())
    is_free.pop()

    return A_, b_, is_free

'''
Destructively mutates A to put it into RREF (Reduced Row Echelon Form)
@return A: Matrix - The mutated A in RREF.
@return is_free: list[bool] - is_free[c] is True iff column c of A is a free column.
'''
def get_rref(A: Matrix) -> tuple[Matrix, list[bool]]:
    ROWS, COLS = len(A), len(A[0])
    is_free = [False] * COLS
    pivot_row = 0
    for pivot_col in range(COLS - 1): # COLS - 1 because the last column is b.
        # Find the first row with an entry in the pivot column.
        #   Then, rearrange the rows to maintain the "staircase".
        for r in range(pivot_row, ROWS):
            if A[r][pivot_col]:
                A[r], A[pivot_row] = A[pivot_row], A[r]
                break
        else:
            # If there is no pivot entry, then this column is free.
            is_free[pivot_col] = True
            continue

        # Reduce the pivot row so that the pivot entry is 1.
        for c in reversed(range(COLS)):
            A[pivot_row][c] = A[pivot_row][c] / A[pivot_row][pivot_col]

        # Zero every entry in the pivot column except the pivot entry.
        for r in range(ROWS):
            if r == pivot_row:
                continue
            coeff = A[r][pivot_col]
            for c in range(COLS):
                A[r][c] = A[r][c] - coeff * A[pivot_row][c]

        pivot_row += 1
    return A, is_free
