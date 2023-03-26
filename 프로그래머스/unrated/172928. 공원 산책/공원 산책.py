def solution(park, routes):
    answer = []
    start_x = 0
    start_y = 0
    x_size = len(park)
    y_size = len(park[0])
    not_move = []
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if(park[i][j] == "S"):
                start_x = i
                start_y = j
            elif(park[i][j] == "X"):
                not_move.append((i, j))
    for rt in routes:
        x,y = map(str, rt.split(' '))
        y = int(y)
        tmp = 0
        if x == "E":
            tmp = tmp + 1 * y
            flag = 0
            if 0 <= start_y + tmp < y_size:
                for i in range(1,y +1 ):
                    if (start_x , start_y + i) in not_move:
                        flag = 1
                        continue
                if flag == 0:
                    start_y = start_y + tmp
        elif x == "W":
            tmp = tmp - 1 * y
            flag = 0
            if 0 <= start_y + tmp < y_size:
                for i in range(1, y +1):
                    if (start_x , start_y - i) in not_move:
                        flag = 1
                        continue
                if flag == 0:
                    start_y = start_y + tmp
        elif x == "S":
            tmp = tmp + 1 * y
            flag = 0
            if 0 <= start_x + tmp < x_size:
                for i in range(1, y+ 1):
                    if (start_x + i, start_y) in not_move:
                        flag = 1
                        continue
                if flag == 0:
                    start_x = start_x + tmp
        elif x == "N":
            tmp = tmp - 1 * y
            flag = 0
            if 0 <= start_x + tmp < x_size:
                for i in range(1, y+ 1):
                    if (start_x - i, start_y) in not_move:
                        flag = 1
                        continue
                if flag == 0:
                    start_x = start_x + tmp
        
    answer = (start_x, start_y)        

    return answer