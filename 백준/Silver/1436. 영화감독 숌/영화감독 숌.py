n = int(input())
sixsixsix = 666
count = 0

while True:
    if '666' in str(sixsixsix):
        count += 1

    if count == n:
        print(sixsixsix)
        break
    sixsixsix += 1
