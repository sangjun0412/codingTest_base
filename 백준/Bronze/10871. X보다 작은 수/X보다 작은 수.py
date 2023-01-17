a,b = map(int, input().split())
x = list(map(int, input().split()))
for i in range(a):
    if(b>x[i]):
        print(x[i], end=" ")