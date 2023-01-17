def solution(n):
    answer = 0
    start = 1
    end = 1
    while start <= end and end <= n:
        tmp = 0
        for i in range(start, end + 1):
            tmp += i
        if tmp == n:
            answer += 1
            end += 1
        elif tmp < n:
            end += 1
        else:
            start +=1
        
    return answer