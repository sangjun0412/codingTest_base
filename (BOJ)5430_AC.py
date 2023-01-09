from collections import deque
t = int(input())

for _ in range(t):
    command = list(input())
    n = int(input())
    nl = input()[1:-1].split(',') # 리스트로 들어왔을때 이부분을 주목해야됨
    nl = deque(nl)
    flag = 0 # 그리고 q를 뒤집는게 반복된다면 flag를 활용하여 최소화로 뒤집는걸 해야됨 안그러면 시간초과가 남
    if n == 0:
        nl = deque()
    for x in command:
        if x == "R":
            flag += 1
        elif x == "D":
            if len(nl) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    nl.popleft()
                else:
                    nl.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(nl) + "]")
        else:
            nl.reverse()
            print("[" + ",".join(nl) + "]")


