# USACO BRONZE _____ PROBLEM 1

import sys

INF = 10**18

def guaranteed_min_A(A, B, cA, cB, x):
    U = B + x
    qL = B // cB
    qU = U // cB
    delta = cA - cB

    def best_h_for_q(q):
        lo = max(B, q * cB)
        hi = min(U, q * cB + (cB - 1))
        if lo > hi:
            return None
        m = hi
        return cA * q - m

    candidates = []

    if qL == qU:
        h = best_h_for_q(qU)
        candidates.append(h)
    else:
        h1 = best_h_for_q(qL)
        if h1 is not None:
            candidates.append(h1)

        h2 = best_h_for_q(qU - 1)
        if h2 is not None:
            candidates.append(h2)

        h3 = best_h_for_q(qU)
        if h3 is not None:
            candidates.append(h3)

    min_h = min(candidates)

    return A + (B + x) + min_h


def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        A, B, cA, cB, fA = map(int, input().split())

        if A >= fA:
            print(0)
            continue

        if cA == 0:
            print(INF)
            continue

        lo, hi = 0, INF
        while lo < hi:
            mid = (lo + hi) // 2
            if guaranteed_min_A(A, B, cA, cB, mid) >= fA:
                hi = mid
            else:
                lo = mid + 1
        print(lo)

if __name__ == "__main__":
    solve()
