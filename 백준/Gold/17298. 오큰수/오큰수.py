import sys
input = sys.stdin.readline

n = int(input())
a_list =list(map(int, input().split()))

answer = [-1] * n
stack = []


for i in range(n):
    while stack and stack[-1][0] < a_list[i]:
        tmp = stack.pop()
        answer[tmp[1]] = a_list[i]
    stack.append([a_list[i],i])

for i in answer:
    print(i, end=' ')
