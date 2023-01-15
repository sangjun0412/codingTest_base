n, m =map(int, input().split())

dic = {}

for i in range(n):
    site, pw = map(str, input().split())
    dic[site] = pw

for j in range(m):
    find = input()
    print(dic[find])
