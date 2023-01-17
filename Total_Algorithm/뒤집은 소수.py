n = int(input())
num_list = list(map(int, input().split()))


def reverse(x):
    rn = ""
    while x > 0:
        rn = rn + str(x % 10)
        x = x//10
    return int(rn)


def isPrime(x):
    ch = [0] * (x + 1)
    for i in range(2, x + 1):
        if ch[i] == 0:
            for j in range(i+i, x + 1, i):
                ch[j] += 1
    if ch[x] == 0:
        return 1
    else:
        return 0


for num in num_list:
    rn = reverse(num)
    if isPrime(rn) and rn != 1:
        print(rn, end=' ')

