
def solution(elements):
    answer = set()
    size = len(elements)
    elements = elements * 2
    
    for i in range(size):
        for j in range(size):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)