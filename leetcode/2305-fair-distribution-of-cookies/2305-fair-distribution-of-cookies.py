class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.result = float('inf')
        self.max_cookies = [0]*k

        def dfsBacktrack(indx):
            if indx == len(cookies):
                self.result = min(self.result, max(self.max_cookies))
                return

            for i in range(k):
                self.max_cookies[i] += cookies[indx]
                dfsBacktrack(indx + 1)
                self.max_cookies[i] -= cookies[indx]
                
                if self.max_cookies[i] == 0:
                    break

        dfsBacktrack(0)

        return self.result