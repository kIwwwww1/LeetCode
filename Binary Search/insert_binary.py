# Время выполнения: O(log(n))
# Память: O(1)

def binary_insert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)
    
    while r - l > 1:
        m = l + (r - l) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m

    return r

print(binary_insert([0,0,1,1,1,3,3,5,8], 3))