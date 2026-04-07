# Время выполнения: O(n)
# Память: O(n+m)

def is_anagram(st1: str, st2: str) -> bool:
    if len(st1) != len(st2):
        return False

    count1 = {}
    count2 = {}

    for char in st1:
        count1[char] = count1.get(char, 0) + 1
    
    for char in st2:
        count2[char] = count2.get(char, 0) + 1

    return count1 == count2

    
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

    
