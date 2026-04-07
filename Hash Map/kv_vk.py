# Время выполнения: O(n)
# Память: O(n)

def kv_vk(st: str) -> str:
    counts = {}

    for ch in st:
        counts[ch] = counts.get(ch, 0) + 1

    freq_list = [[] for _ in range(len(st) + 1)] # индекс - частота, значение - символ

    for ch, cout in counts.items():
        freq_list[cout].append(ch)

    result = []

    for cout in range(len(freq_list) -1, 0, -1):
        for char in freq_list[cout]:
            result.append(char * cout)

    return ''.join(result)


print(kv_vk('BABBCBC'))  
