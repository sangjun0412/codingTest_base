import sys
from tabnanny import check

input = sys.stdin.readline

n = int(input())
num = 1

for i in range(1, n + 1):
    num *= i

check_num = str(num)
cnt = 0

for i in range(len(check_num) - 1, 0, -1):
    if check_num[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
