# Время выполнения: ...
# Память: ...

def delete_intersec(segment: list[list[int]]) -> int:
    segment.sort(key=lambda nums: nums[1])

    count_kept = 0
    last_end = float('-inf')

    for start, end in segment:
        if start >= last_end:
            count_kept += 1
            last_end = end

    return len(segment) - count_kept
    
print(delete_intersec([[4,5], [2,6], [1,3], [6,7]]))