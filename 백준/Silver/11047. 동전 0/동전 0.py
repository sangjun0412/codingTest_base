n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, -1, -1):
    
    if coins[i] <= k:
        mok = k // coins[i]
        k -= coins[i]*mok
        cnt += mok
   
    if k == 0:
        break

print(cnt)