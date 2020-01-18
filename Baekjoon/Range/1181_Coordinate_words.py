import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    result.append(str(sys.stdin.readline()[:-1]))

result.sort(key = lambda x: (len(x), ascii(x[0])))

for j in result:
    print(j)