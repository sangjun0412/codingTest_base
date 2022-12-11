from collections import deque
a = input()
n = int(input())
q = deque(a)

for i in range(n):
    plan = input()
    plan = deque(plan)
    for x in plan:
        if x in q:
            if x != q.popleft():
                print(f'#{i + 1} NO')
                break
    else:
        if len(q) == 0:
            print(f'#{i + 1} YES')
        else:
            print(f'#{i + 1} NO')
