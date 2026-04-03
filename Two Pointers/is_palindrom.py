def is_palindrom(st: str) -> bool:
    left = 0
    right = len(st) - 1

    while left < right:
        if st[left] != st[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
    # Самый простой способ
    # return st == st[::-1]

print(is_palindrom('шалаш'))