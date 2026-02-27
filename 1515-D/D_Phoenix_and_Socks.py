t = int(input())

out_lines = []

for _ in range(t):
    n, l, r = map(int, input().split())

    colors = list(map(int, input().split()))

    left_cnt = [0] * (n + 1)
    right_cnt = [0] * (n + 1)

    for i in range(l):
        left_cnt[colors[i]] += 1
    for i in range(l, n):
        right_cnt[colors[i]] += 1

    for c in range(1, n + 1):
        m = min(left_cnt[c], right_cnt[c])
        if m:
            left_cnt[c] -= m
            right_cnt[c] -= m
            l -= m
            r -= m

    if l >= r:
        heavy = left_cnt
        light = right_cnt
    else:
        heavy = right_cnt
        light = left_cnt
        l, r = r, l

    ans = 0

    diff = l - r
    need_pairs = diff // 2
    for c in range(1, n + 1):
        if need_pairs == 0:
            break
        pairs = heavy[c] // 2
        if pairs:
            use = min(pairs, need_pairs)
            heavy[c] -= 2 * use
            l -= 2 * use
            need_pairs -= use
            ans += use

    extra = (l - r) // 2
    ans += extra
    l -= extra
    r += extra

    ans += l

    out_lines.append(ans)
    
    print(ans)
