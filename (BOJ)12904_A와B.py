"""
두 문자열 s 와 t가 주어졌을 때,
s를 t로 바꾸는 게임
2가지 연산
- 문자열 뒤에 a 추가 -> 맨 뒤 a 삭제
- 문자열을 뒤집고 뒤에 b 추가 -> 비삭제후 문자열 뒤집기
s를 t로 만들수 있는 지 없는 지 확인
첫째 줄에 s, 둘째 줄에 t

"""
s = list(map(str, input()))
t = list(map(str, input()))

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)