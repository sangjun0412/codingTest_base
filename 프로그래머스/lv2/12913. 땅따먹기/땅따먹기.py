"""
행이 10만개..
흠,,,,
dfs로 해보고 일단 안되면 고민하자
"""
answer = 0
def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i -1][:j] + land[i - 1][j+1:])
    
        
    return max(land[len(land) - 1])