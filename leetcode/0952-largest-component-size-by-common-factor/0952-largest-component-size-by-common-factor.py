class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[rx] < self.root[ry]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[rx] += 1
    
    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def prime_factors(n):
            prim = set()
            while n % 2 == 0:
                prim.add(2)
                n //= 2
            
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    prim.add(i)
                    n //= i
            
            if n > 2:
                prim.add(n)

            return list(prim)

        unf = UnionFind(len(nums))
        prime = defaultdict(int)
        for i, num in enumerate(nums):
            primes = prime_factors(num)
            for p in primes:
                if p in prime:
                    unf.union(prime[p], i)
                prime[p] = i

        count = Counter()
        for i in range(len(nums)):
            count[unf.find(i)] += 1
            
        return max(count.values())