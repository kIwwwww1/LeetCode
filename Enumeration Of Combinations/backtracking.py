# Время выполнения: O(n*4^n / √n)
# Память: O(n*4^n / √n)
# Альтернативный вариант
# =========================
# Время выполнения: O(n*2^2*n)
# Память: O(n*2^2*n)

from collections import deque

def generate_brackets(n: int) -> list[str]:
    q = deque([('', 0, 0)])

    while q and len(q[0][0]) < 2 * n:
        prefix, open_used, closed_used = q.popleft()

        if open_used < n:
            q.append((prefix + '(', open_used + 1, closed_used))

        if closed_used < open_used:
            q.append((prefix + ')', open_used, closed_used + 1))

    return [prefix for prefix, _, _ in q]

print(generate_brackets(2))