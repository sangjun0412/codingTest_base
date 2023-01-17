T = int(input())
for _ in range(T):
    input_data = input()
    a = list(input_data)
    sum = 0
    for i in a:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
