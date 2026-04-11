# Время выполнения: O(n)
# Память: O(n)


class PrefixArray:
    def __init__(self, nums: list[int]) -> None:
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
        
    def sum(self, l: int, r: int) -> int:
        return self.prefix[r + 1] - self.prefix[l]

pref = PrefixArray([1,4,5,-3,7,2])
print(pref.sum(1, 5))


        