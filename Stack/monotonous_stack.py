# Время выполнения: O(n)
# Память: O(n)

def next_greater(nums: list[int]) -> list[int]:
    n = len(nums)
    stack = []
    result = [-1] * n

    for i in range(len(nums) -1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result

print(next_greater([2,5,1,3,0,4]))