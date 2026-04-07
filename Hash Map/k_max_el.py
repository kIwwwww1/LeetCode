# Время выполнения: O(n)
# Память: O(n)

def k_max_el(nums: list[int], k: int) -> list[int]:

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    freq_list = [[] for _ in range(len(nums) + 1)]

    for num, count in counts.items():
        freq_list[count].append(num)

    result = []

    for ind in range(len(freq_list) -1, 0, -1):
        for item in freq_list[ind]:
            result.append(item)
            if len(result) == k:
                return result

    return result
    
print(k_max_el([5,8,5,5,4,4,5], 3))