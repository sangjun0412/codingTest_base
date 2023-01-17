while True:
    nl = list(map(int, input().split()))
    nl.sort()
    if nl[0] == 0 and nl[1] == 0 and nl[2] == 0:
        break
    if nl[0] + nl[1] <= nl[2]:
        print("Invalid")
    elif nl[0] == nl[1] and nl[1] == nl[2]:
        print("Equilateral")
    elif nl[0] == nl[1] or nl[1] == nl[2] or nl[0] == nl[2]:
        print("Isosceles")
    else:
        print("Scalene")
