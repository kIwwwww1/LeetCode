# Время выполнения: O(n*n!)
# Память: O(n*n!)

from collections import deque

def all_combinations(nums: list[int]) -> list[list[int]]:
    q = deque([[]])
    for num in nums:
        for _ in range(len(q)):
            curr_perm = q.popleft()
            for i in range(len(curr_perm) + 1):
                new_perm = curr_perm[:i] + [num] + curr_perm[i:]
                q.append(new_perm)

    return list(q)

print(all_combinations([1,2,3]))
            
