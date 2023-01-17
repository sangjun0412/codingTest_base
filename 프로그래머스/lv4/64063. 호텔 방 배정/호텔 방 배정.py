import sys
sys.setrecursionlimit(10000000)

def find(number, parent):
    if number not in parent:
        parent[number] = number + 1
        return number
    empty = find(parent[number], parent)
    parent[number] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    parent = {}
    
    for i in room_number:
        ch_room = find(i, parent)
        answer.append(ch_room)
    return answer