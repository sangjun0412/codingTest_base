"""
윳놀이 Y 2명 같은그림찾기 F 3명 원카드 O 4명
플레이할 사람 수 N 게임 종류 주어지고
이름 나열
"""
n, game = map(str, input().split())
n = int(n)
nl = list()


for i in range(n):
    nl.append(input())

nl = list(set(nl))
if game == "Y":
    print(len(nl))
elif game == "F":
    print(len(nl)//2)
elif game == "O":
    print(len(nl)//3)