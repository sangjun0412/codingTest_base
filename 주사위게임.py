n = int(input())
dice = []
for _ in range(n):
    a, b, c = map(int, input().split())
    dice.append((a,b,c))
cmp = -21700000
for a, b, c in dice:
    tmp = 0
    if a == b and b == c:
        tmp = 10000 + a * 1000
    elif a==b:
        tmp = 1000 + a*100
    elif b==c:
        tmp = 1000 +b*100
    elif a==c:
        tmp = 1000 +c*100
    else:
        tmp = max(a,b,c) * 100

    if cmp < tmp:
        cmp = tmp

print(cmp)
