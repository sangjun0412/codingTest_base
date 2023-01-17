# dungeons -> 앞에꺼가 최소 피로도, 뒤에꺼는 소모 피로도
# 최대 던전의 개수 -> 앞에꺼랑 뒤에꺼 동시에 소팅하고 빼면서 세기
# k 는 현재의 쓸 수 있는 피로도
#인줄 알았으나 완탐
res = 0

def solution(k, dungeons):
    n = len(dungeons)
    
    visit = [0] * (n + 1)
    def dfs(cal, k):
        global res
        if res < cal:
            res = cal

        for i in range(n):  
            if k >= dungeons[i][0] and not visit[i]:
                visit[i] = 1
                tmp = k - dungeons[i][1]
                dfs(cal + 1, tmp)
                visit[i] = 0

    dfs(0, k)
    return res