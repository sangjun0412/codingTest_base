s1 = input()
s2 = input()

t1 = dict()
t2 = dict()

c1 = list(set(s1))
c2 = list(set(s2))

for i in range(len(c1)):
    t1[c1[i]] = 0

for j in range(len(c2)):
    t2[c2[j]] = 0


for i in range(len(s1)):
    t2[s2[i]] += 1
    t1[s1[i]] += 1


if t1.items() == t2.items():
    print("YES")
else:
    print("NO")