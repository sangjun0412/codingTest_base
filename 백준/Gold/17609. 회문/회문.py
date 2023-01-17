"""
회문이면 0
유사회문(하나를 제외하면 회문으로 만들수 있으면) 1
그 외 2
"""
t = int(input())

def check_pseudo(sentence):
    end = len(sentence) - 1
    tmp_sentence = sentence[:]

    for i in range(len(sentence) // 2):
        if sentence[i] != sentence[end - i]:
            sentence.pop(i)
            tmp_sentence.pop(end-i)

            break
    tmp = sentence[::-1]
    tmp2 = tmp_sentence[::-1]

    if tmp == sentence or tmp2 == tmp_sentence:
        return 1
    else:
        return 0


for _ in range(t):
    sentence = list(input())
    tmp = sentence[::-1]
    if sentence == tmp:
        print(0)
    elif check_pseudo(sentence):
        print(1)
    else:
        print(2)

