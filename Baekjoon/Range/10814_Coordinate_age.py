import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    order = i
    age_str, name = list(map(str, sys.stdin.readline().split()))
    age = int(age_str)
    result.append([order, age, name])

result.sort(key = lambda x: (x[1], x[0]))

for j in result:
    print(j[1], j[2])