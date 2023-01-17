import sys

m, n, k = map(int, input().split())

secret = list(map(int, input().split()))

compare = list(map(int, input().split()))

start = 0
end = 1
flag = 0
for i in range(len(compare)):
    if compare[i] == secret[0]:
        if compare[i:i+len(secret)] == secret:
            flag = 1
            break
        else:
            continue
if flag==1:
    print("secret")
else:
    print("normal")
