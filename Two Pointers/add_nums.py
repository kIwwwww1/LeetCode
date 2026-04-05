# Время выполнения: O(n+m)
# Память: O(n+m)

def add_nums(nums1: list[int], nums2: list[int]):
    l1, l2 = 0, 0
    result = []

    while l1 < len(nums1) and l2 < len(nums2):
        if nums1[l1] < nums2[l2]:
            result.append(nums1[l1])
            l1 += 1
        else:
            result.append(nums2[l2])
            l2 += 1
        
    result.extend(nums1[l1:])
    result.extend(nums2[l2:])

    return result

print(add_nums([1,3,5,7], [2,4,6,8]))