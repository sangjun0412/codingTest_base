import sys

input = sys.stdin.readline

m = int(input())
list1 = set()


for _ in range(m):
    raw = str(input().rstrip())
    if " " in raw:
        command, number = raw.split(" ")
        number = int(number)
        if command == "check":
            if number in list1:
                print(1)
            else:
                print(0)
        elif command == "add":
            list1.add(number)
        elif command == "remove":
            try:
                list1.discard(number)
            except:
                pass
        elif command == "toggle":
            if number in list1:
                list1.discard(number)
            else:
                list1.add(number)
    else:
        if raw == "all":
            list1 = set([i for i in range(1, 21)])
        elif raw == "empty":
            list1.clear()
