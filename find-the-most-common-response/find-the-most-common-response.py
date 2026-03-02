class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()
        
        for res in responses:
            for response in set(res):
                counter[response] +=1

        max_cnt = max(counter.values())
        most_com = min(response for response, cnt in counter.items() if cnt == max_cnt)

        return most_com
