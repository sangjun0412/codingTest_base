import sys
from collections import Counter
N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

# 산술평균
print(round(sum(numbers) / N))

# 중앙값
print(numbers[N // 2])

# 최빈값
count_list = sorted(Counter(numbers).items(), key=lambda x: (-x[1], x[0]))
if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

# 범위 : 최댓값 - 최솟값
print(max(numbers) - min(numbers))
