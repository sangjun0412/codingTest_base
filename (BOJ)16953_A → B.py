a, b = map(int, input().split())
answer = 1

while (b != a):
    answer += 1
    tmp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if tmp == b:
        print(-1)
        break
else:
    print(answer)
