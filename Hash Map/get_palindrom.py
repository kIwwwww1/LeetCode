# Время выполнения: O(n)
# Память: O(k)

def get_palindrom(st: str) -> bool:
    count = {}

    for sim in st:
        count[sim] = count.get(sim, 0) + 1

    odd_count = 0

    for ch in count.values():
        if ch % 2 == 1:
            odd_count += 1
    
    return odd_count <= 1

print(get_palindrom('ABC'))
print(get_palindrom('AABBCC'))
print(get_palindrom('AABBCABC'))
print(get_palindrom('ABCABCC'))
