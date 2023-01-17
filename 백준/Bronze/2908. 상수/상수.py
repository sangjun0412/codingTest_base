def solve(a,b):
    c=""
    d=""
    for i in a:
        c= i+c
    for j in b:
        d= j+d

    c= int(c)
    d= int(d)
    if(c>d):
        print(c)
    elif(d>c):
        print(d)

a,b = map(str, input().split())
if "0" not in a and b:
    solve(a,b)
