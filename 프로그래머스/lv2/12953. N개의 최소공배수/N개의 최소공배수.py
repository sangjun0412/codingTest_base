def solution(arr):
    def gcd(a,b):
        while b>0:
            a,b = b, a%b
        return a
    
    tmp = 1
    for x in arr:
        tmp = tmp * x / gcd(x, tmp)
    answer = tmp
    
    return answer