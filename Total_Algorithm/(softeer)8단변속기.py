import sys
nl = list(map(int, input().split()))
a = list(range(1,9))
ds = list(range(8,0, -1))
if nl == a:
    print("ascending")
elif nl == ds:
    print("descending")
else:
    print("mixed")
