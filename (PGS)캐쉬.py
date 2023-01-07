"""
hit -> 1
miss -> 5
LRU
"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque(cities)
    cache = deque()
    if cacheSize == 0:
        return len(cities) * 5
    if cacheSize == 1:
        ch = []
        while q:
            x = q.popleft()
            x = x.lower()
            if ch == []:
                ch.append(x)
                answer += 5
            else:
                if ch[0] == x:
                    answer += 1
                else:
                    ch.pop()
                    ch.append(x)
                    answer += 5
        return answer
    while q:
        x = q.popleft()
        x = x.lower()
        if len(cache) < cacheSize:
            if x not in cache:
                answer += 5
                cache.append(x)
            else:
                cache.remove(x)
                cache.append(x)
                answer += 1
        else:
            if x in cache:
                cache.remove(x)
                cache.append(x)
                answer += 1
            elif x not in cache:
                cache.popleft()
                cache.append(x)
                answer += 5

    return answer