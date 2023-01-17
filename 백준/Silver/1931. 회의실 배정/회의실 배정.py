import sys
input = sys.stdin.readline

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort()

meeting = time[0]
meetingCount = 1

for i in range(1, n):
    if meeting[0] < time[i][0]:
        if meeting[1] <= time[i][0]:
            meeting = time[i]
            meetingCount += 1
        elif meeting[1] >= time[i][1]:
            meeting = time[i]
    elif meeting[0] == meeting[1]:
        meeting = time[i]
        meetingCount += 1

print(meetingCount)
