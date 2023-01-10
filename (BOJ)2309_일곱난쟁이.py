nl = list()
for i in range(9):
    nl.append(int(input()))
nl.sort()
cmp = sum(nl) - 100
for i in range(0, 9):
    if (cmp - nl[i]) in nl:
        x = cmp -nl[i]
        nl.remove(nl[i])
        nl.remove(x)
        break
for x in nl:
    print(x)