t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    result = float('inf')

    for i in range(n):
        count_a = 0
        count_b = 0
        count_c = 0

        for j in range(i, min(n, i + 7)):
            if s[j] == 'a':
                count_a += 1
            elif s[j] == 'b':
                count_b += 1
            else:
                count_c += 1

            length = j - i + 1

            if length >= 2:
                if count_a > count_b and count_a > count_c:
                    result = min(result, length)

    if result == float('inf'):
        print(-1)
    else:
        print(result)
