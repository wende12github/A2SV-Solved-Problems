import sys
input = sys.stdin.readline

n = int(input())

contest = list(map(int, input().split()))

day_count = 0
contest.sort()

for pro in contest:
    if pro >= day_count + 1:
        day_count += 1
        
print(day_count)
