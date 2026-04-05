def sort_zero(arr: list[int]) -> list[int]:
    slow, fast = 0, 0

    while fast < len(arr):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1

        fast += 1
        
    return arr


print(sort_zero([0,1,0,0,3,12,2]))
