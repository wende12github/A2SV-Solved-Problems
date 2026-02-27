t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    working = set()

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1

        length = j - i

        if length % 2 == 1:
            working.add(s[i])

        i = j

    print("".join(sorted(working)))
