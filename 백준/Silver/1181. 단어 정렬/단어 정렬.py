a = int(input())
list1 = []
for _ in range(a):
    list1.append(input())
list2 = set(list1)
list3 = list(list2)
list3.sort()
list3.sort(key=len)

for i in list3:
    print(i)