answer = 0
def solution(numbers, target):
    
    def dfs(cal, i):
        global answer
        if i == len(numbers):
            if cal == target:
                answer += 1
            return
        else:
            cal1 = cal + numbers[i]
            dfs(cal1, i + 1)
            cal2 = cal - numbers[i]
            dfs(cal2, i + 1)
            
    dfs(0, 0)
        
    
    return answer