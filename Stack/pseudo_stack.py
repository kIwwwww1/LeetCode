# Время выполнения: O(n)
# Память: O(1)

def is_valid(s: str) -> bool:
    balance = 0

    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
        
    return True

print(is_valid('()(())'))
print(is_valid('()))'))