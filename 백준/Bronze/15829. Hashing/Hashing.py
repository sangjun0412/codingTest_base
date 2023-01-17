from string import ascii_lowercase
L = int(input())
list_alphabet = list(ascii_lowercase)
x = list(input())
result = 0
for i in range(L):
    result += (list_alphabet.index(x[i])+1)*(31**i)
print(result)
