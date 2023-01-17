x =input()
list1 = list(map(int, input().split()))
max=-1000000
min=1000000
for i in list1:
    if(max<i):
        max=i
    if(min>i):
        min=i
print(min,max)