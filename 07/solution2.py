from read_input import read_input

def count_timelines(grid: list[list[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if r + 1 not in range(ROWS):
                break
            if char == 'S':
                dp[r + 1][c] += 1
            elif char == '^':
                if c - 1 in range(COLS):
                    dp[r + 1][c - 1] += dp[r][c]
                if c + 1 in range(COLS):
                    dp[r + 1][c + 1] += dp[r][c]
            else: # char == '.':
                dp[r + 1][c] += dp[r][c]

    return sum(dp[-1])

test_count = count_timelines(read_input("input1"))
assert test_count == 40, test_count

print(count_timelines(read_input()))
