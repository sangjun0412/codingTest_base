n = int(input())
x = list(map(int, input().split(' ')))

if max(x) == 1:
    print(1)
else:
    print(min(x)*max(x))
