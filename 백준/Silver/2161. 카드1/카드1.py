from collections import deque
n = int(input())
que = deque()
array = list()

for i in range(n):
    que.append(i + 1)

while(len(que) > 1):
    array.append(que.popleft())
    que.append(que.popleft())

array.append(que.pop())

for i in array:
    print(i, end=' ')
