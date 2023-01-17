k = int(input())
x = []
for _ in range(k):
    x.append(int(input()))
x.sort()

max = x[-1]
for i in range(k):
    var = x[i]*(k-i)
    if(max < var):
        max = var

print(max)
