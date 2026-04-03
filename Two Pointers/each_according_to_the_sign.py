def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    l1, l2 = 0, 0
    result = []

    while l1 < len(nums1) and l2 < len(nums2):
        if nums1[l1] < nums2[l2]:
            l1 += 1
        elif nums1[l1] > nums2[l2]:
            l2 += 1
        else:
            result.append(nums1[l1])
            l1 += 1
            l2 += 1

    return result

    # Простой вариант
    # return list(set(nums1) & set(nums2))

print(intersect([1, 3, 5, 5, 10], [2, 3, 10, 11]))