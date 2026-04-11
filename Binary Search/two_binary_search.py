# Время выполнения: O(log(n))
# Память: O(1)

def search_first(nums: list[int], target: int) -> int:
    l, r = -1, len(nums) - 1
    while r - l > 1:
        m = l + (r - l) // 2
        if nums[m] < target:
            l = m
        else:
            r = m
    
    return r if nums[r] == target else - 1

def search_last(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)
    while r - l > 1:
        m = l + (r - l) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m

    return l if nums[l] == target else - 1

def search_range(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]
    return [search_first(nums, target), search_last(nums, target)]

print(search_range([0,0,1,1,1,3,3,5,8], 1))