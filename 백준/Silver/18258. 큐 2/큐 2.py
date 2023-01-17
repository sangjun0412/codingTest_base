import sys

N = int(sys.stdin.readline())
queue = []

length = 0

for i in range(N):

    command = sys.stdin.readline().split()


    if(command[0] == 'push'):

        queue.append(command[1])
    

    elif(command[0] == 'pop'):
        if len(queue)-length == 0:
            print(-1)
        else:
            print(queue[length])
            length = length + 1
            

    elif(command[0] == 'front'):

        if len(queue) - length == 0:
            print(-1)
        else:
            print(queue[length])
    elif(command[0] == 'back'):
        if len(queue) - length == 0:
            print(-1)
        else:
            print(queue[-1])
    elif(command[0] == 'size'):
        print(len(queue)-length)
    elif(command[0] == 'empty'):
        if len(queue) - length == 0: 
            print(1)
        else:
            print(0)