def query(p, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return 0
    return p[r2][c2] - p[r1-1][c2] - p[r2][c1-1] + p[r1-1][c1-1]

q = int(input())
result = []

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    horizontal = query(prefix_h, r1, c1, r2, c2-1)
    vertical = query(prefix_v, r1, c1, r2-1, c2)

    result.append(str(horizontal + vertical))

print("\n".join(result))