class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in  strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            temp = []
            for i in range(26):
                if count[i] != 0:
                    temp.extend([chr(i + ord('a')), str(count[i])])
                    
            groups[''.join(temp)].append(s)

        result.extend(groups.values())
        
        return result
