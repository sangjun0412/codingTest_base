n = int(input())
num_list = list(map(int, input().split()))


def digit_sum(x):
    max = 0
    number = 0
    for i in x:
        i = str(i)
        tmp = 0
        for j in i:
            tmp += int(j)
        if max < tmp:
            max = tmp
            number = int(i)
    print(number)

digit_sum(num_list)
