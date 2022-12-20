"""
거리두기 수칙을 지켜야함
한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐있다
세로로 n칸 또는 가로로 m칸 이상 비우고 앉아야 함.
최대 몇명 수용이 가능한지
"""
import math
h, w, n, m = map(int, input().split())
a = math.ceil(h/(n+1))
b = math.ceil(w/(m+1))
print(a * b)