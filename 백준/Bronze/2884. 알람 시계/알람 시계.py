a,b = map(int, input().split())

if(b>=45 and b<60):
    b= b-45
elif(b<45):
    a= a-1
    b= b+15
    if(b==60):
        b=0
    if(a==-1):
        a=23
print(a, b)