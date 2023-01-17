import sys
input = sys.stdin.readline

n = str(input().rstrip())


while len(n) >= 10:
    print(n[0:10])
    n = n[10:]

print(n)
