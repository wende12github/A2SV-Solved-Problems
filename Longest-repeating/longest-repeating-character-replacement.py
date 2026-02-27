class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = long_str = 0
        freq = {}
        n = len(s)

        for right in range(n):
            if not s[right] in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1
            
            count = right - left + 1
            max_val = count - max(freq.values())

            if max_val <= k:
                long_str = max(long_str, count)
            else:
                freq[s[left]] -= 1

                if not freq[s[left]]:
                    freq.pop(s[left])
                left += 1
                
        return long_str
