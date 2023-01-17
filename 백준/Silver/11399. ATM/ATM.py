n = int(input())
P = list(map(int, input().split()))
P.sort()
answer = 0
result = 0
for i in P:
    answer += i
    result += answer
print(result)
