n = int(input())

for t in range(n):
    a = input()
    a = a.lower()
    size = len(size)
    for i in range(size):
        if a[i] != a[-1-i]:
            print(f'#{t+1} NO')
            break
    else:
        print(f'#{t+1} YES')

