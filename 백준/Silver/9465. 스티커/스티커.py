"""
2차원 dp
굳이 디피테이블을 만들지 않아도 되면 만들지 말것.
n = 1일떄를 생각을 꼭해야됨!!
"""
import sys
input = sys.stdin.readline
tc = int(input())

for t in range(tc):
    n = int(input())
    nl = []

    for j in range(2):
        nl.append(list(map(int, input().split())))

    for i in range(1, n):
        if i == 1:
            nl[0][1] = nl[0][1] + nl[1][0]
            nl[1][1] = nl[1][1] + nl[0][0]
        else:
            nl[0][i] = nl[0][i] + max(nl[1][i - 2], nl[1][i - 1])
            nl[1][i] = nl[1][i] + max(nl[0][i - 1], nl[0][i - 2])
    print(max(nl[0][n - 1], nl[1][n - 1]))