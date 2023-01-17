import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
y = list(set(x))
y.sort()

dic = {y[i]: i for i in range(len(y))}

for i in x:
    print(dic[i], end=' ')
