n = int(input())

alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
answer = 0
tmp = []
al = []

for _ in range(n):
    tmp.append(input())

for x in tmp:
    for i in range(len(x)):
        num = 10 ** (len(x) - i - 1)
        alphabet_dict[x[i]] += num

for v in alphabet_dict.values():
    if v > 0:
        al.append(v)

al.sort(reverse=True)

for i in range(len(al)):
    answer += al[i] * (9 - i)
print(answer)