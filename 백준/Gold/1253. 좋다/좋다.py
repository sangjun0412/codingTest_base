"""
n개의 수 중에서 어떤 수가 다른 두 수의 합으로 나타낼 수 있다면 좋은 수(Good)
n개의 수가 주어지면 그중에 좋은 수가 몇개 인지 출력
수의 위치가 다르면 값이 같아도 다른 수 -> 일단 그러면 num_list를 받아서 오름차순으로 정렬 후 모든 경우의 수를 만들어서 체킹 하는 방식.
모든 조합의 경우의 수를 캐치
"""

n = int(input())
nl = list(map(int, input().split()))
nl.sort()
ans = 0


def two_point(num_list, target):
    global ans
    start, end = 0, len(num_list) - 1 #소팅한 넘리스트의 끝과 끝을 확인하여 체킹
    while start < end:
        tmp = num_list[start] + num_list[end]
        if target == tmp:
            ans += 1
            return
        elif target > tmp:
            start += 1 #작으면 가장 최소값을 높이고
        elif target < tmp:
            end -= 1 #크면 맨 뒤값을 줄인다.


for i in range(n):
    two_point(nl[:i] + nl[i+1:], nl[i]) # 현재 구하려는 타겟지점은 제외해야함

print(ans)