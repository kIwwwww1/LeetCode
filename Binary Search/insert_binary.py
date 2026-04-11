# Время выполнения: O(log(n))
# Память: O(1)

def binary_insert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return l

print(binary_insert([0,0,1,1,1,3,3,5,8], 2))