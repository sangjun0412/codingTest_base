n = int(input())
A_list = list(map(int, input().split()))
b, c = map(int, input().split())
change_list = [[0] for i in range(n)]

## 각각의 시험장엔 총감독관은 무조건 한명씩 있어야함
## 총감독관은 B 부감독관은 C

for i, num in enumerate(A_list):
    if num - b >= 0:
        change_list[i] = num - b
    else:
        change_list[i] = 0

cnt = n

for i, num in enumerate(change_list):
    if change_list[i] % c == 0:
        cnt += change_list[i] // c
    else:
        cnt += change_list[i] // c + 1

print(cnt)