# Время выполнения: O(n)
# Память: O(n)

def combination_range(nums: list[str]) -> list[str | int]:
    l, r = 0, 0
    result = []
    
    while l < len(nums):
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            r += 1

        if l != r:
            result.extend([nums[l], r - l + 1])
        else:
            result.append(nums[l])
        
        l = r + 1
        r += 1

    return result

print(combination_range(['z', 'z', 'y', 'y', 'y', 'v', 'x', 'x']))