from collections import deque
t = int(input())

for _ in range(t):
    command = list(input())
    n = int(input())
    nl = input()[1:-1].split(',')
    nl = deque(nl)
    flag = 0
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


