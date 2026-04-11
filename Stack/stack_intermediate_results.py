# Время выполнения: O(n)
# Память: O(n)


def is_valid(s: str) -> bool:
    mapping = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>',
    }
    stack = []

    for char in s:
        if char in mapping:
            stack.append(char)
        elif len(stack) == 0:
            return False
        else:
            last_char = stack.pop()
            if mapping[last_char] != char:
                return False

    return len(stack) == 0

print(is_valid('()<[{}]>'))
print(is_valid('()<[}]>'))
print(is_valid(')()<[{}]>'))