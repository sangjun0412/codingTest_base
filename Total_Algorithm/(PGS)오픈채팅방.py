"딕셔너리"
def solution(record):
    answer = []
    n = len(record)
    dic = {}
    for x in record:
        tmp = (x.split(' '))
        if tmp[0] != 'Leave':
            if tmp[1] not in dic:
                dic[tmp[1]] =tmp[2]
            else:
                dic[tmp[1]] =tmp[2]
    for x in record:
        tmp = x.split(' ')
        if tmp[0] == "Enter":
            sentence = str(dic[tmp[1]]) + "님이 들어왔습니다."
            answer.append(sentence)
        elif tmp[0] =="Leave":
            sentence = str(dic[tmp[1]]) + "님이 나갔습니다."
            answer.append(sentence)


    return answer