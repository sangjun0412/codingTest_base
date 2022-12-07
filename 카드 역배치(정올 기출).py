card = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    tmp = card[a-1:b]
    tmp.reverse()
    card = card[:a-1] + tmp + card[b:]
print(*card)