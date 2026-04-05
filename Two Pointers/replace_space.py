# Время выполнения: O(n)
# Память: O(1)

def replace_space(chars: list[str]) -> list[str]:
    slow, fast = 0, 0
    while fast < len(chars):
        if chars[fast] != " " or (fast == 0 or chars[fast - 1] != " "):
            chars[slow] = chars[fast]
            slow += 1
        fast += 1
    return chars[:slow]

chars = [" ", " ", "h", "i", " ", " ", " ", "!", " "]
print(replace_space(chars)) 
