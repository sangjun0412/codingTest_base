def solution(s):
    zero = 0
    cnt = 0
    while True:
        if s == '1':
            answer = [cnt, zero]
            break
        tmp = ''
        for x in s:
            if x == '0':
                zero +=1
            else:
                tmp +='1'
        s = bin(len(tmp))[2:]
        cnt+=1
    
    return answer