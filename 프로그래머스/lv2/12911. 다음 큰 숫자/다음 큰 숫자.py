def solution(n):
    answer = 0
    cnt = 0
    
    def cal(num):
        cnt = 0
        binary = bin(num)[2:]
        for x in str(binary):
            if x == '1':
                cnt += 1
        return cnt
    cnt = cal(n)
    n = n + 1
    while True:
        if cal(n) == cnt:
            answer = n
            break
        n = n + 1
    return answer