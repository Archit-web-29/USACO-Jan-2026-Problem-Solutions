# USACO BROZNE _____ PROBLEM 2

import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        num_test_cases = int(next(iterator))
        k_parameter = int(next(iterator))
    except StopIteration:
        return

    for _ in range(num_test_cases):
        try:
            FjString = int(next(iterator)) 
            S = next(iterator)
        except StopIteration:
            break
            
        N = FjString
        
        if N % 2 != 0:
            print("-1")
            continue
            
        half_len = (3 * N) // 2
        if S[:half_len] == S[half_len:]:
            print("1")
            print(" ".join(["1"] * (3 * N)))
            continue
        
        print("2")
        ans = [0] * (3 * N)
        
        subsequences = [
            (0, 1, 2),
            (0, 1), (0, 2), (1, 2),
            (0,), (1,), (2,)
        ]
        
        for i in range(N // 2):
            block1_start = 3 * i
            block2_start = 3 * (i + N // 2)
            
            idx_map_1 = {}
            idx_map_2 = {}
            
            for j in range(3):
                idx_map_1[S[block1_start + j]] = block1_start + j
                idx_map_2[S[block2_start + j]] = block2_start + j
            
            block_pairs = []
            for char in "COW":
                block_pairs.append((idx_map_1[char], idx_map_2[char]))
            

            block_pairs.sort(key=lambda x: x[0])
            
            best_sub = []
            
            for sub in subsequences:
                is_increasing = True
                for k in range(len(sub) - 1):
                    if block_pairs[sub[k]][1] >= block_pairs[sub[k+1]][1]:
                        is_increasing = False
                        break
                
                if is_increasing:
                    best_sub = sub
                    break
            
            lis_indices = set(best_sub)
            for p_idx, pair in enumerate(block_pairs): 
                if p_idx in lis_indices:
                    ans[pair[0]] = 1
                    ans[pair[1]] = 1
                else:
                    ans[pair[0]] = 2
                    ans[pair[1]] = 2
                    
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()
