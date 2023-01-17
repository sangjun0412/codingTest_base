from itertools import count


a = int(input())
numbers = map(int, input().split())
counting = 0 

for number in numbers:
    check = 0 
    if(number > 1):
        for j in range(2, number):
            if(number % j == 0):
                check += 1
        if(check == 0):
            counting += 1
print(counting)