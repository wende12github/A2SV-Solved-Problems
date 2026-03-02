class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = freq.most_common()
        
        result = []
        for key, val in sorted_chars:
            result.append(key * val)

        return "".join(result)
