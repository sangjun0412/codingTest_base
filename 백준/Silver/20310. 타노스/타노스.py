"""
0과 1 반 날리기
0은 뒤부터 날리기
1은 앞부터 날리기
"""
v = list(input())
zero = v.count('0') // 2 # 날리는 갯수
one = v.count('1') // 2 #날리는 갯수
for _ in range(zero):
    v.pop(-v[::-1].index('0') - 1)
for _ in range(one):
    v.pop(v.index('1'))
for i in v:
    print(i, end='')