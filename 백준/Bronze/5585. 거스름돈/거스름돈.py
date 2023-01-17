import sys
input = sys.stdin.readline

a = int(input())
a = 1000 - a
cnt = 0
while a != 0:
    if a - 500 >= 0:
        a = a - 500
        cnt += 1
    elif a - 500 < 0 and a - 100 >= 0:
        a = a - 100
        cnt += 1
    elif a - 100 < 0 and a-50 >= 0:
        a = a - 50
        cnt += 1
    elif a - 100 < 0 and a - 10 >= 0:
        a = a - 10
        cnt += 1
    elif a - 10 < 0 and a-5 >= 0:
        a = a - 5
        cnt += 1
    elif a - 5 < 0 and a - 1 >= 0:
        a = a - 1
        cnt += 1

print(cnt)
