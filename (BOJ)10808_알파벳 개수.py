from string import ascii_lowercase
a = input()
dic = {}
alphabet = list(ascii_lowercase)
for x in alphabet:
    dic[x] = 0
for x in a:
    dic[x] += 1

for k, v in dic.items():
    print(v, end=' ')
