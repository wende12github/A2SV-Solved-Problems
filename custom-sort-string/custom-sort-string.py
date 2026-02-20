class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        res = []

        for char in order:
            if char in s_count:
                res.append(char*s_count[char])

        for char, count in s_count.items():
            if char not in order:
                res.append(char*count)
            
        return "".join(res)
