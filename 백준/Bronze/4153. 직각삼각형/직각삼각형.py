while(True):
    a, b, c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    a = a*a
    b = b*b
    c = c*c
    if(a > b and a > c):
        if(a == b+c):
            print("right")
        else:
            print("wrong")
    elif(b > a and b > c):
        if(b == a+c):
            print("right")
        else:
            print("wrong")
    elif(c > a and c > b):
        if(c == a + b):
            print("right")
        else:
            print("wrong")
