s = input()

tmp = ''
for i in s:
    if i.isdecimal():
        tmp += i
tmp = int(tmp)
cnt = 1 # 자신의 숫자
for i in range(1, tmp // 2 + 1):
    if tmp % i == 0:
       cnt += 1

print(tmp)
print(cnt)