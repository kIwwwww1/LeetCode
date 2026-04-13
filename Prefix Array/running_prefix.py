# Время выполнения: O(n)
# Память: O(1)

def pivot_index(nums: list[int]) -> int:
    total_sum = sum(nums)
    prefix_sum = 0

    for i, num in enumerate(nums):
        suffix_sum = total_sum - prefix_sum - num
        if prefix_sum == suffix_sum:
            return i
        prefix_sum += num

    return -1

print(pivot_index([7,-1,4,10,5,5]))