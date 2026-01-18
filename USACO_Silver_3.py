# USACO Silver _____ Problem 3

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    INF = 10**18

    for _ in range(t):
        N = int(data[idx]); K = int(data[idx + 1]); idx += 2
        r = data[idx]; idx += 1
        rb = [c & 1 for c in r]

        off = [0] * (N + 1)

        NK = N - K
        for i in range(1, NK + 1):
            off[i + K] = off[i] ^ (rb[i - 1] ^ rb[i])

        dpmin0, dpmin1 = 0, INF
        dpmax0, dpmax1 = 0, -INF

        for s in range(1, K + 1):
            ones0 = 0
            ln = 0
            for j in range(s, N + 1, K):
                ln += 1
                ones0 += off[j]
            ones1 = ln - ones0

            nmin0 = nmin1 = INF
            nmax0 = nmax1 = -INF

            # from parity 0
            v = dpmin0 + ones0
            if v < nmin0: nmin0 = v
            v = dpmax0 + ones0
            if v > nmax0: nmax0 = v

            v = dpmin0 + ones1
            if v < nmin1: nmin1 = v
            v = dpmax0 + ones1
            if v > nmax1: nmax1 = v

            # from parity 1 (if reachable)
            if dpmin1 != INF:
                v = dpmin1 + ones0
                if v < nmin1: nmin1 = v
                v = dpmax1 + ones0
                if v > nmax1: nmax1 = v

                v = dpmin1 + ones1
                if v < nmin0: nmin0 = v
                v = dpmax1 + ones1
                if v > nmax0: nmax0 = v

            dpmin0, dpmin1 = nmin0, nmin1
            dpmax0, dpmax1 = nmax0, nmax1

        need = rb[0]  # r1
        if need == 0:
            out_lines.append(f"{dpmin0} {dpmax0}")
        else:
            out_lines.append(f"{dpmin1} {dpmax1}")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

