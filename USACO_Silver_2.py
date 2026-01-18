# USACO Silver _____ Problem 2

import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []

    for _ in range(T):
        n = int(next(it)); m = int(next(it))

        l = [0] * (n + 1)
        r = [0] * (n + 1)
        for i in range(1, n + 1):
            l[i] = int(next(it))
        for i in range(1, n + 1):
            r[i] = int(next(it))

        g = [[] for _ in range(n + 1)]
        for _ in range(m):
            x = int(next(it)); y = int(next(it)); z = int(next(it))
            g[x].append((y, z))
            if y != x:
                g[y].append((x, z))  # undirected

        vis = bytearray(n + 1)
        sign = [0] * (n + 1)   # +/-1
        offs = [0] * (n + 1)   # integer offset
        ok = True
        ans = 0

        for start in range(1, n + 1):
            if vis[start]:
                continue

            # BFS component, represent a_i = sign[i] * A + offs[i]
            vis[start] = 1
            sign[start] = 1
            offs[start] = 0
            dq = deque([start])
            comp = [start]
            A_fixed = None  # integer A if forced by odd cycle / self constraint

            while dq and ok:
                u = dq.popleft()
                su = sign[u]
                tu = offs[u]
                for v, z in g[u]:
                    if not vis[v]:
                        vis[v] = 1
                        sign[v] = -su
                        offs[v] = z - tu
                        dq.append(v)
                        comp.append(v)
                    else:
                        sv = sign[v]
                        tv = offs[v]
                        coef = su + sv          # 0 or +/-2
                        num = z - tu - tv       # must equal coef * A
                        if coef == 0:
                            if num != 0:
                                ok = False
                                break
                        else:
                            # coef is +/-2, so num must be even
                            if num & 1:
                                ok = False
                                break
                            cand = num // coef
                            if A_fixed is None:
                                A_fixed = cand
                            elif A_fixed != cand:
                                ok = False
                                break

            if not ok:
                break

            if A_fixed is not None:
                A = A_fixed
                cnt = 0
                for i in comp:
                    ai = sign[i] * A + offs[i]
                    if l[i] <= ai <= r[i]:
                        cnt += 1
                ans += cnt
            else:
                for i in comp:
                    if sign[i] == 1:
                        L = l[i] - offs[i]
                        R = r[i] - offs[i]
                    else:
                        L = offs[i] - r[i]
                        R = offs[i] - l[i]
                    pts.append((L, 1))
                    pts.append((R + 1, -1))

                pts.sort()
                cur = 0
                best = 0
                j = 0
                while j < len(pts):
                    x = pts[j][0]
                    delta = 0
                    while j < len(pts) and pts[j][0] == x:
                        delta += pts[j][1]
                        j += 1
                    cur += delta
                    if cur > best:
                        best = cur
                ans += best

        out_lines.append(str(-1 if not ok else ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

