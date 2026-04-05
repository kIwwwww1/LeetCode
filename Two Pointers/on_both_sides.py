# Время выполнения: O(n)
# Память: O(1)

def two_sum(nums: list[int], target: int) -> list[int]:

    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left, right]
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]

print(two_sum([-2, 1, 6, 9, 12, 21], target=18))