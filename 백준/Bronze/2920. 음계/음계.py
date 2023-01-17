list1 = list(map(int, input().split()))
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
list3 = [8, 7, 6, 5, 4, 3, 2, 1]

if(list1 == list2):
    print("ascending")
elif(list1 == list3):
    print("descending")
else:
    print("mixed")