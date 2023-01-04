def solution(brown, yellow):
    answer = []
    total = brown + yellow
    candidate = []
    for i in range(1, total // 2 + 1):
        if not total % i:
            if total // i >= i and i > 2:
                candidate.append((total // i, i))
    for x, y in candidate:
        if (x - 2) * (y - 2) == yellow:
            return [x, y]


