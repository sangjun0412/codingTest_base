sdoku = [list(map(int, input().split())) for _ in range(9)]

#가로

chnum = 0
for i in range(9):
    ch1 = [0] * 10
    ch2 = [0] * 10
    for j in range(9):
        ch1[sdoku[i][j]] = 1
        ch2[sdoku[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) != 9:
        chnum = 1
        break
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        ch3 = [0] * 10
        for k in range(i, i + 3):
            for s in range(j, j + 3):
                ch3[sdoku[k][s]] = 1
        if sum(ch3) != 9:
            chnum = 1
            break

if chnum == 1:
    print("NO")
else:
    print("YES")