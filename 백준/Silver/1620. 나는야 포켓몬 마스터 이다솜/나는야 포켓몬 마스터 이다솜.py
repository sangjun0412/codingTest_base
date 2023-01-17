import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

dogam = [[] for _ in range(n)]
dogam_name = {}

for i in range(n):
    pokemon = str(input().rstrip())
    dogam[i].append(pokemon)
    dogam_name[pokemon] = i + 1

for j in range(m):
    tmp = str(input().rstrip())
    if tmp[0] >= '0' and tmp[0] <= '9':
        for i in (dogam[int(tmp) - 1]):
            print(i)
    else:
        print(dogam_name[tmp])
