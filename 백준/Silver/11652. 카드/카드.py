n = int(input())
dic = {}
for i in range(n):
    x = int(input())
    if x in dic.keys():
        dic[x] += 1
    else:
        dic[x] = 1

a = sorted(dic.items(), key=lambda x:(-x[1],x[0]))

print(a[0][0])