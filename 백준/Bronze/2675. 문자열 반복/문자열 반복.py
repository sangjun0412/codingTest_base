def solve():
    a,b = input().split()
    a = int(a)

    for i in b:
        print(i*a, end="")
    print("")

t = int(input())
for _ in range(t):
    solve()
