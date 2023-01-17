y =[]
z =[]

for i in range(10):
    x=int(input())
    y.append(x%42)
    if y[i] not in z:
        z.append(y[i])
print(len(z))