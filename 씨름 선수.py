n = int(input())
people = []
for _ in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

people.sort(reverse=True)
large = 0
cnt = 0
for x, y in people:
    if large < y:
        large = y
        cnt += 1
print(cnt)