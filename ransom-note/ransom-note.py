class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check_count = {}

        for char in magazine:
            if char not in check_count:
                check_count[char] = 1
            else:
                check_count[char] += 1

        for char in ransomNote:
            if char in check_count and check_count[char] > 0:
                check_count[char] -= 1
            else:
                return False
        
        return True
