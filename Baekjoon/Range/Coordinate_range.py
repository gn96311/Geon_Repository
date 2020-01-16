N = int(input())

result = []
for i in range(N):
    X, Y = list(map(int, input().split()))
    result.append([X,Y])

result.sort(key = lambda x: (x[0], x[1]))
for j in result:
    print(j[0], j[1])

#sys.stdin은 input보다 속도가 빠르다.

#sort 함수에서 key를 설정하면, 특정 기준으로 정렬한다.

'''
import sys

N = int(sys.stdin.readline())
result = []
for i in range(N):
    result.append(list(map(int, sys.stdin.readline().split())))
result.sort(key = lambda x: (x[0], x[1]))
for j in result:
    print(j[0], j[1])
'''