import sys

n = int(input())

answer = 2

for i in range(n):
    answer += 2 ** i
print(answer ** 2)
