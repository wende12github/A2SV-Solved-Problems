class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_sum = 0
        chars = Counter(chars)
        
        for word in words:
            copy = chars.copy()

            for char in word:
                if char in copy and copy[char] != 0:
                    copy[char] -= 1
                else:
                    total_sum -= len(word)
                    break
            total_sum += len(word)
            
        return total_sum
