# USACO BRONZE _____ PROBLEM 3

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Q = int(input())

# 1-indexed grid
grid = [[0] * (N + 1) for _ in range(N + 1)]

# square_sum[i][j] = sum of KxK square with top-left at (i, j)
size = N - K + 1
square_sum = [[0] * (size + 1) for _ in range(size + 1)]

max_sum = 0

for _ in range(Q):
    r, c, v = map(int, input().split())
    old = grid[r][c]
    delta = v - old
    grid[r][c] = v

    # Determine affected KxK squares
    r_start = max(1, r - K + 1)
    r_end = min(r, size)
    c_start = max(1, c - K + 1)
    c_end = min(c, size)

    for i in range(r_start, r_end + 1):
        row = square_sum[i]
        for j in range(c_start, c_end + 1):
            row[j] += delta
            if row[j] > max_sum:
                max_sum = row[j]

    print(max_sum)


