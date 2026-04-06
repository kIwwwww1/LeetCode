# Время выполнения: O(n)
# Память: O(n)

def compress_range(nums: list[int]) -> list[int]:
    l, r = 0, 0
    result = []

    while l < len(nums):
        while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
            r += 1
        
        if l != r:
            result.append(f'{nums[l]}->{nums[r]}')
        else:
            result.append(f'{nums[l]}')
        
        l =  r + 1
        r = r + 1

    return result

print(compress_range([1,2,3,5,8,9,14]))