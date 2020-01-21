import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    word = str(sys.stdin.readline()[:-1])
    if word in result:
        pass
    else:
        result.append(word)

result.sort(key = lambda x: (len(x), x))

for j in result:
    print(j)