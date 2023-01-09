"""
100이면 팝레프트 하면서 cnt +1 이후,출력 그리고 나서 cnt =0으로 초기화
100이 아니면 모든 프로그래스 + 1
"""
from collections import deque
def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
    return answer