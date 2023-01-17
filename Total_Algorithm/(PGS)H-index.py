"""
n편중 h번 이상 인용된 논문 h편 이상
나머지 논문이 h번 이하.
"""
def solution(citations):
    citations.sort(reverse = True)
    for i, x in enumerate(citations):
        if i >= x:
            return i
    return len(citations)