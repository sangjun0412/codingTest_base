n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = list(array)
array.sort()

for i in array:
    print(i)
