# Время выполнения: O(n)
# Память: O(n)

def is_overlapping(a: list[int], b: list[int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])

def merge_two(a: list[int], b: list[int]) -> list[int]:
    return [min(a[0], b[0]), max(a[1], b[1])]

def merge(segment: list[list[int]]) -> list[list[int]]:
    segment.sort()
    print(segment)

    result = [segment[0]]

    for i in range(1, len(segment)):
        last = result[-1]
        print(last)
        print('выше last')
        current = segment[i]
        print(current)

        if is_overlapping(last, current):
            result[-1] = merge_two(last, current)
        else:
            result.append(current)
    return result

print(merge([[2,4], [1,3], [5,6], [6,7]]))