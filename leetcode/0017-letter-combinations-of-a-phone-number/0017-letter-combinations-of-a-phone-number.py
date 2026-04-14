class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        fact = 1
        for digit in digits:
            fact *= len(mapping[digit])

        comb_array = ["" for _ in range(fact)]

        scp = fact
        for digit in digits:
            letters_count = len(mapping[digit])
            letter_q = scp // letters_count
            
            comp_loop = 0
            for ltr in mapping[digit]:
                for h in range(fact // scp):
                    for i in range(letter_q):
                        shifted_i = i + (letter_q * comp_loop) + (scp * h)
                        comb_array[shifted_i] += ltr
                comp_loop += 1

            scp = letter_q

        return comb_array