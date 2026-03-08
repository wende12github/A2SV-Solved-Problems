class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False

        pattern_to_words, words_to_pattern = {}, {}
        
        for char, word in zip(pattern, words):
            if char in pattern_to_words and pattern_to_words[char] != word:
                return False

            if word in words_to_pattern and words_to_pattern[word] != char:
                return False

            pattern_to_words[char] = word
            words_to_pattern[word] = char

        return True