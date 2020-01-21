import sys

N, M = list(map(int, sys.stdin.readline().split()))

number_list = []

for i in range(N):
    number_list.append(i+1)

print(number_list)