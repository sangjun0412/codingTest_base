"""
수열이 있고
+ - 공백 세가지를 숫자 사이에 삽입하자.
n이 주어졌을때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 찾아라.
경우가 계속 나뉘고 그 경우에 따라서 해야 된다. dfs
ASC 코드 순서에 따라 결과가 0이되는 모든 수식 출력
"""
tc = int(input())

for _ in range(tc):
    n = int(input())
    tmp = []
    operator = []


    def dfs(depth):
        cal_method = [' ', '+', '-']

        if depth == n:
            copy_tmp = tmp[:]
            operator.append(copy_tmp)

            return
        else:
            for i in range(3):
                tmp.append(cal_method[i])
                dfs(depth + 1)
                tmp.pop()
    dfs(1)
    for x in operator:
        tmp = ""
        for j in range(1, n):
            tmp += str(j) + str(x[j - 1])
        tmp += str(n)
        if eval(tmp.replace(' ', '')) == 0:
            print(tmp)
    print()
