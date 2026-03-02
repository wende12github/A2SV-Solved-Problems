t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    
    s = input().strip()
    
    move_RL = 0
    first_hit = -1

    for i in range(n):
        if s[i] == 'L':
            move_RL -= 1
        else:
            move_RL += 1

        if x + move_RL == 0:
            first_hit = i + 1
            break

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    move_RL = 0
    cycle_time = -1

    for i in range(n):
        if s[i] == 'L':
            move_RL -= 1
        else:
            move_RL += 1

        if move_RL == 0:
            cycle_time = i + 1
            break

    if cycle_time == -1:
        print(1)
    else:
        remaining = k - first_hit
        result = 1 + remaining // cycle_time
        print(result)
