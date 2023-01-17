arr =[]
for i in range(9):
    arr.append(int(input()))
maxnum= 0
idx = 0
for j in range(9):
    if maxnum < arr[j]:
        idx = j
        maxnum =arr[j]
print(maxnum)
print(idx+1)
