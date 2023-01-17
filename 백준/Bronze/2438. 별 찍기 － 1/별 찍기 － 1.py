def solve():
    N = int(input())
    for x in range(1,N+1):
        for j in range(x):
            print("*",end='')
        print("")
solve()