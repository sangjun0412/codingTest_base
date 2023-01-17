x = int(input())

for _ in range(x):
    y = str(input())
    z = ""
    cnt=0
    result=0
    for i in y:
        if i =='O':
            cnt +=1
        else:
            cnt =0
        result +=cnt
    print(result)
        