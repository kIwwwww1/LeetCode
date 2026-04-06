# Время выполнения: O(n)
# Память: O(1)

def k_elements_max_sum(nums: list[int], k: int) -> int:
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    
    curr_sum = window_sum

    for r in range(k, len(nums)):
        l = r - k
        window_sum = window_sum - nums[l] + nums[r]
        curr_sum = max(curr_sum, window_sum)
    
    return curr_sum
    
print(k_elements_max_sum([3,2,0,9,1,2,8,5,2], 5))

