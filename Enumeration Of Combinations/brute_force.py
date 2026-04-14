# Время выполнения: O(n*4^n)
# Память: O(n*4^n)


from collections import deque

def generate_combinations(s: str) -> list[str]:
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    result = deque([''])

    while result and len(result[0]) < len(s):
        prefix = result.popleft()
        digit = s[len(prefix)]

        for letter in phone_map[digit]:
            result.append(prefix + letter)
    
    return list(result)

print(generate_combinations('24'))
