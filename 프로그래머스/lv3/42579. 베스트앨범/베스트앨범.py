def solution(genres, plays):
    answer = []
    music = {}
    
    temp = []
    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    temp = sorted(temp, key=lambda x:(x[0], -x[1], x[2]))
    for g in temp:
        if g[0] not in music:
            music[g[0]] =g[1]
        else:
            music[g[0]] += g[1]
    music = sorted(music.items(), key=lambda x:-x[1])
    for i in music:
        cnt = 0
        for j in temp:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(j[2])
    
    return answer