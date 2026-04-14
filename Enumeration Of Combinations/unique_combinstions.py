# Время выполнения: O(n*2^N)
# Память: O(n*2^N)

from collections import deque

def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        new_subsets = []
        for curr in result:
            new_subsets.append(curr + [num])

        result.extend(new_subsets)

    return result

print(subsets([3, 6, 17]))