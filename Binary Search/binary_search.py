# Время выполнения: O(log(n))
# Память: O(1)

def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    while r - l > 1:
        m = l + (r - l) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m
        
    return l if nums[l] == target else -1

print(binary_search([1,2,8,8,9,10,11,12,14], 8))