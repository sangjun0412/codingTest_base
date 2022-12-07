n = int(input())
ch = [0] * (n + 1)
for i in range(2, n + 1): #첫 소수의 배수를 전부다 체크해서, 시간초과를 막음
    if ch[i] == 0:
        for j in range(i+i, n+1, i):
            ch[j] += 1

cnt = 0
for k in range(2, n + 1):
    if ch[k] == 0:
        cnt += 1
print(cnt)