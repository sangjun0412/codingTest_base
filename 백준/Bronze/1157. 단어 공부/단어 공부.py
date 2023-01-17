value = input()
upvalue = value.upper()
dic = dict()
for x in upvalue:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
res = [k for k, v in dic.items() if max(dic.values()) == v]

if len(res) == 1:
    print(res[0])
else:
    print("?")