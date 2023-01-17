from collections import deque

test_case = int(input())

for tc in range(test_case):
    n = int(input())
    bit = deque()
    location = deque()
    ct_location = 0
    while n != 0:
        if n % 2 == 0:
            bit.append(0)
        else:
            bit.append(1)
            location.append(ct_location)
        if n == 1:
            n = 0
        else:
            n = n // 2
        ct_location += 1
    for ct in location:
        print(ct, end = ' ')